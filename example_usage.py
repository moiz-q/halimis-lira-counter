"""
Simple example of using the Lira cash detection function.
"""
from detect_lira import detect_and_calculate_cash

# Example usage
if __name__ == '__main__':
    # Path to your model and image
    model_path = 'best.pt'
    image_path = 'your_image.jpg'  # Replace with your image path
    
    try:
        # Run detection
        results = detect_and_calculate_cash(model_path, image_path)
        
        # Access results
        print(f"\nTotal amount detected: {results['total_amount']} Lira")
        print(f"Number of detections: {len(results['detections'])}")
        
        # Save output image
        output_path = 'output_detection.jpg'
        import cv2
        cv2.imwrite(output_path, results['output_image'])
        print(f"\nOutput image saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

