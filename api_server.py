"""
Flask API server for Turkish Lira cash detection.
This server handles image uploads and returns detection results.
"""
from flask import Flask, request, jsonify
from flask_cors import CORS
import cv2
import numpy as np
from ultralytics import YOLO
import base64
import io
from PIL import Image
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for mobile app

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

def base64_to_image(base64_string):
    """Convert base64 string to OpenCV image."""
    # Remove data URL prefix if present
    if ',' in base64_string:
        base64_string = base64_string.split(',')[1]
    
    # Decode base64
    image_data = base64.b64decode(base64_string)
    
    # Convert to PIL Image
    pil_image = Image.open(io.BytesIO(image_data))
    
    # Convert to RGB if necessary
    if pil_image.mode != 'RGB':
        pil_image = pil_image.convert('RGB')
    
    # Convert to numpy array
    image_array = np.array(pil_image)
    
    # Convert RGB to BGR for OpenCV
    image_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
    
    return image_bgr

def image_to_base64(image):
    """Convert OpenCV image to base64 string."""
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Convert to PIL Image
    pil_image = Image.fromarray(image_rgb)
    
    # Convert to base64
    buffer = io.BytesIO()
    pil_image.save(buffer, format='JPEG')
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    
    return image_base64

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'healthy', 'model_loaded': model is not None})

@app.route('/detect', methods=['POST'])
def detect_cash():
    """
    Detect cash in uploaded image.
    Expects JSON with 'image' field containing base64 encoded image.
    """
    try:
        # Load model if not already loaded
        model = load_model()
        
        # Get image from request
        data = request.get_json()
        if not data or 'image' not in data:
            return jsonify({'error': 'No image provided'}), 400
        
        base64_image = data['image']
        conf_threshold = data.get('conf', 0.25)
        
        # Convert base64 to OpenCV image
        image = base64_to_image(base64_image)
        
        # Run inference
        results = model(image, conf=conf_threshold)
        
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
                        'confidence': float(confidence),
                        'bbox': [float(x1), float(y1), float(x2), float(y2)]
                    })
        
        # Calculate total amount
        total_amount = 0
        for denomination, count in counts.items():
            value = int(denomination)
            total_amount += value * count
        
        # Draw detections on image
        output_image = image.copy()
        for det in detections:
            x1, y1, x2, y2 = [int(coord) for coord in det['bbox']]
            denomination = det['denomination']
            confidence = det['confidence']
            
            # Draw bounding box
            cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Draw label
            label = f"{denomination} Lira ({confidence:.2f})"
            label_size, _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.6, 2)
            cv2.rectangle(output_image, (x1, y1 - label_size[1] - 10), 
                         (x1 + label_size[0], y1), (0, 255, 0), -1)
            cv2.putText(output_image, label, (x1, y1 - 5), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        # Draw total amount on image
        total_text = f"Total: {total_amount} Lira"
        cv2.putText(output_image, total_text, (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        
        # Convert output image to base64
        output_image_base64 = image_to_base64(output_image)
        
        # Prepare response
        response = {
            'success': True,
            'total_amount': total_amount,
            'total_bills': sum(counts.values()),
            'counts': counts,
            'detections': detections,
            'annotated_image': output_image_base64
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Check if model file exists
    if not os.path.exists(MODEL_PATH):
        print(f"Warning: Model file {MODEL_PATH} not found!")
        print("Please ensure best.pt is in the same directory.")
    
    # Run the server
    PORT = 8080  # Changed from 5000 to avoid conflicts
    print("Starting Flask API server...")
    print(f"API will be available at http://localhost:{PORT}")
    print("Make sure to update the API_URL in the mobile app to match your server IP")
    app.run(host='0.0.0.0', port=PORT, debug=True)

