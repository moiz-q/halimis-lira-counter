import cv2
from ultralytics import YOLO
import argparse
from pathlib import Path

def detect_and_calculate_cash(model_path, image_path, conf_threshold=0.25):
    """
    Detect Turkish Lira cash denominations in an image and calculate total amount.
    
    Args:
        model_path: Path to the YOLO model weights file (best.pt)
        image_path: Path to the input image
        conf_threshold: Confidence threshold for detections (default: 0.25)
    
    Returns:
        dict: Dictionary containing detection results and total amount
    """
    # Load the YOLO11m model
    print(f"Loading model from {model_path}...")
    model = YOLO(model_path)
    
    # Read the input image
    print(f"Processing image: {image_path}")
    image = cv2.imread(str(image_path))
    
    if image is None:
        raise ValueError(f"Could not read image from {image_path}")
    
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
            
            # Get class name (should match class_names)
            if class_id < len(class_names):
                denomination = class_names[class_id]
                counts[denomination] += 1
                
                # Get bounding box coordinates
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy()
                
                detections.append({
                    'denomination': denomination,
                    'confidence': confidence,
                    'bbox': [int(x1), int(y1), int(x2), int(y2)]
                })
    
    # Calculate total amount
    total_amount = 0
    for denomination, count in counts.items():
        value = int(denomination)
        total_amount += value * count
    
    # Print results
    print("\n" + "="*50)
    print("DETECTION RESULTS")
    print("="*50)
    print(f"\nTotal bills detected: {sum(counts.values())}")
    print("\nBreakdown by denomination:")
    for denomination in sorted(class_names, key=lambda x: int(x)):
        count = counts[denomination]
        if count > 0:
            value = int(denomination)
            subtotal = value * count
            print(f"  {denomination} Lira: {count} bill(s) = {subtotal} Lira")
    
    print(f"\n{'='*50}")
    print(f"TOTAL AMOUNT: {total_amount} Lira")
    print(f"{'='*50}\n")
    
    # Draw detections on image
    output_image = image.copy()
    for det in detections:
        x1, y1, x2, y2 = det['bbox']
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
    
    return {
        'counts': counts,
        'detections': detections,
        'total_amount': total_amount,
        'output_image': output_image
    }


def main():
    parser = argparse.ArgumentParser(description='Detect Turkish Lira cash and calculate total amount')
    parser.add_argument('--model', type=str, default='best.pt', 
                       help='Path to YOLO model weights file (default: best.pt)')
    parser.add_argument('--image', type=str, required=True,
                       help='Path to input image')
    parser.add_argument('--output', type=str, default=None,
                       help='Path to save output image with detections (optional)')
    parser.add_argument('--conf', type=float, default=0.25,
                       help='Confidence threshold for detections (default: 0.25)')
    
    args = parser.parse_args()
    
    # Check if files exist
    if not Path(args.model).exists():
        raise FileNotFoundError(f"Model file not found: {args.model}")
    
    if not Path(args.image).exists():
        raise FileNotFoundError(f"Image file not found: {args.image}")
    
    # Run detection
    results = detect_and_calculate_cash(args.model, args.image, args.conf)
    
    # Save output image if specified
    if args.output:
        cv2.imwrite(args.output, results['output_image'])
        print(f"Output image saved to: {args.output}")
    else:
        # Display image
        cv2.imshow('Lira Cash Detection', results['output_image'])
        print("Press any key to close the window...")
        cv2.waitKey(0)
        cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

