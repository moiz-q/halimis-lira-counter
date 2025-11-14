"""
Hugging Face Space with Gradio web interface for Halimi's Lira Counter.
This provides a complete web UI that runs entirely on Hugging Face.
"""
import gradio as gr
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os

# Load the model once at startup
MODEL_PATH = 'best.pt'
model = None

def load_model():
    """Load the YOLO model."""
    global model
    if model is None:
        print(f"Loading YOLO model from {MODEL_PATH}...")
        model = YOLO(MODEL_PATH)
        print("Model loaded successfully!")
    return model

def detect_cash(image, conf_threshold=0.25):
    """
    Detect cash in uploaded image.
    
    Args:
        image: PIL Image or numpy array
        conf_threshold: Confidence threshold for detections
    
    Returns:
        tuple: (annotated_image, results_text)
    """
    try:
        # Load model if not already loaded
        model = load_model()
        
        # Convert PIL to numpy array if needed
        if isinstance(image, Image.Image):
            image_array = np.array(image)
            # Convert RGB to BGR for OpenCV
            if len(image_array.shape) == 3:
                image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
            else:
                image_bgr = image_array
        else:
            image_bgr = image
        
        # Run inference
        results = model(image_bgr, conf=conf_threshold)
        
        # Class names: '10', '100', '20', '200', '5', '50'
        class_names = ['10', '100', '20', '200', '5', '50']
        
        # Count each denomination
        counts = {denomination: 0 for denomination in class_names}
        detections = []
        
        # Process detections
        for result in results:
            boxes = result.boxes
            for box in boxes:
                # Get class ID and confidence
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                
                # Get class name
                if class_id < len(class_names):
                    denomination = class_names[class_id]
                    counts[denomination] += 1
                    
                    # Get bounding box coordinates
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    
                    detections.append({
                        'denomination': denomination,
                        'confidence': confidence,
                        'bbox': [float(x1), float(y1), float(x2), float(y2)]
                    })
        
        # Calculate total amount
        total_amount = 0
        breakdown_lines = []
        for denomination in sorted(class_names, key=lambda x: int(x)):
            count = counts[denomination]
            if count > 0:
                value = int(denomination)
                subtotal = value * count
                total_amount += subtotal
                breakdown_lines.append(f"  {denomination} Lira: {count} bill(s) = {subtotal} Lira")
        
        # Draw detections on image
        output_image = image_bgr.copy()
        for det in detections:
            x1, y1, x2, y2 = [int(coord) for coord in det['bbox']]
            denomination = det['denomination']
            confidence = det['confidence']
            
            # Draw bounding box
            cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 3)
            
            # Draw label
            label = f"{denomination} Lira ({confidence:.2f})"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.7, 2)
            cv2.rectangle(output_image, (x1, y1 - label_size[1] - 15), 
                         (x1 + label_size[0] + 10, y1), (0, 255, 0), -1)
            cv2.putText(output_image, label, (x1 + 5, y1 - 8), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        
        # Draw total amount on image
        total_text = f"Total: {total_amount} Lira"
        cv2.putText(output_image, total_text, (20, 50), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        
        # Convert BGR back to RGB for display
        output_image_rgb = cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB)
        
        # Create results text
        results_text = f"""
🇹🇷 HALIMI'S LIRA COUNTER - RESULTS

{'='*50}
TOTAL AMOUNT: {total_amount} Lira
Total Bills Detected: {sum(counts.values())}
{'='*50}

Breakdown by Denomination:
{chr(10).join(breakdown_lines) if breakdown_lines else '  No bills detected'}

{'='*50}
"""
        
        return output_image_rgb, results_text
        
    except Exception as e:
        error_text = f"Error processing image: {str(e)}"
        return None, error_text

# Create Gradio interface
def create_interface():
    """Create and return the Gradio interface."""
    
    with gr.Blocks(
        theme=gr.themes.Soft(
            primary_hue="purple",
            secondary_hue="pink",
        ),
        title="🇹🇷 Halimi's Lira Counter"
    ) as demo:
        gr.Markdown(
            """
            # 🇹🇷 Halimi's Lira Counter
            
            Detect and count Turkish Lira cash bills using AI!
            
            **Instructions:**
            1. Upload an image of Turkish Lira bills
            2. Adjust confidence threshold if needed (default: 0.25)
            3. Click "Detect Cash" to process
            4. View results with annotated image and breakdown
            
            **Supported Denominations:** 5, 10, 20, 50, 100, 200 Lira
            """
        )
        
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(
                    type="pil",
                    label="Upload Image of Turkish Lira Bills"
                )
                conf_slider = gr.Slider(
                    minimum=0.1,
                    maximum=1.0,
                    value=0.25,
                    step=0.05,
                    label="Confidence Threshold"
                )
                detect_btn = gr.Button(
                    "🔍 Detect Cash",
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column():
                image_output = gr.Image(
                    label="Annotated Image with Detections",
                    type="numpy"
                )
                results_output = gr.Textbox(
                    label="Detection Results",
                    lines=15,
                    interactive=False
                )
        
        # Examples
        gr.Examples(
            examples=[],
            inputs=image_input,
            label="Example Images (add your own examples)"
        )
        
        # Connect the function
        detect_btn.click(
            fn=detect_cash,
            inputs=[image_input, conf_slider],
            outputs=[image_output, results_output]
        )
        
        gr.Markdown(
            """
            ---
            **Note:** This app uses YOLO11m model to detect Turkish Lira denominations.
            For best results, ensure bills are clearly visible and well-lit.
            """
        )
    
    return demo

# Launch the interface
if __name__ == "__main__":
    demo = create_interface()
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False
    )

