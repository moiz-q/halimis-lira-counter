"""
Complete Flask application serving both frontend and backend.
Frontend: Expo web build
Backend: YOLO detection API
"""
import os
import io
import base64
import cv2
import numpy as np
from flask import Flask, request, jsonify, send_from_directory, send_file
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image

app = Flask(__name__, static_folder='web', static_url_path='')
CORS(app)

# Load model
MODEL_PATH = 'best.pt'
model = None

def load_model():
    """Load YOLO model once at startup."""
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
    image_bytes = base64.b64decode(base64_string)
    image = Image.open(io.BytesIO(image_bytes))
    
    # Convert to OpenCV format
    image_np = np.array(image)
    if len(image_np.shape) == 2:  # Grayscale
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_GRAY2BGR)
    elif image_np.shape[2] == 4:  # RGBA
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGBA2BGR)
    else:  # RGB
        image_bgr = cv2.cvtColor(image_np, cv2.COLOR_RGB2BGR)
    
    return image_bgr

def image_to_base64(image):
    """Convert OpenCV image to base64 string."""
    # Convert BGR to RGB
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    pil_image = Image.fromarray(image_rgb)
    
    # Save to bytes
    buffered = io.BytesIO()
    pil_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    
    return f"data:image/png;base64,{img_str}"

@app.route('/')
def index():
    """Serve the main Expo web app."""
    return send_from_directory('web', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    """Serve static files from Expo web build."""
    return send_from_directory('web', path)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({
        'status': 'healthy',
        'message': 'Halimi\'s Lira Counter API is running',
        'model_loaded': model is not None
    })

@app.route('/detect', methods=['POST'])
def detect():
    """
    Detect cash in uploaded image.
    Expects JSON: {"image": "base64_string", "confidence": 0.25}
    Returns JSON with detections and annotated image.
    """
    try:
        # Load model if not already loaded
        load_model()
        
        # Get request data
        data = request.get_json()
        
        if not data or 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        # Get confidence threshold
        conf_threshold = data.get('confidence', 0.25)
        
        # Convert base64 to image
        image_base64 = data['image']
        image = base64_to_image(image_base64)
        
        # Run detection
        results = model(image, conf=conf_threshold)
        
        # Class names
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
                    
                    # Get bounding box
                    x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                    
                    detections.append({
                        'denomination': denomination,
                        'confidence': confidence,
                        'bbox': [float(x1), float(y1), float(x2), float(y2)]
                    })
        
        # Calculate total
        total_amount = 0
        breakdown = {}
        for denomination in class_names:
            count = counts[denomination]
            if count > 0:
                value = int(denomination)
                subtotal = value * count
                total_amount += subtotal
                breakdown[denomination] = {
                    'count': count,
                    'subtotal': subtotal
                }
        
        # Draw annotations on image
        output_image = image.copy()
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
        
        # Draw total on image
        total_text = f"Total: {total_amount} Lira"
        cv2.putText(output_image, total_text, (20, 50),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)
        
        # Convert annotated image to base64
        annotated_image_base64 = image_to_base64(output_image)
        
        # Return response
        return jsonify({
            'success': True,
            'total_amount': total_amount,
            'total_bills': sum(counts.values()),
            'breakdown': breakdown,
            'detections': detections,
            'annotated_image': annotated_image_base64
        })
    
    except Exception as e:
        print(f"Error in detection: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

if __name__ == '__main__':
    # Load model at startup
    load_model()
    
    # Run Flask app
    port = int(os.environ.get('PORT', 7860))
    print(f"Starting server on port {port}...")
    print(f"Frontend: http://localhost:{port}/")
    print(f"API: http://localhost:{port}/detect")
    app.run(host='0.0.0.0', port=port, debug=False)

