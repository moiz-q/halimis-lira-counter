# Turkish Lira Cash Counter

This project uses a YOLO11m model to detect Turkish Lira cash denominations in images and calculate the total amount.

## Classes Detected

The model detects the following Turkish Lira denominations:
- 5 Lira
- 10 Lira
- 20 Lira
- 50 Lira
- 100 Lira
- 200 Lira

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
```bash
python detect_lira.py --image path/to/your/image.jpg
```

### With Custom Model Path
```bash
python detect_lira.py --model best.pt --image path/to/your/image.jpg
```

### Save Output Image
```bash
python detect_lira.py --image path/to/your/image.jpg --output output.jpg
```

### Adjust Confidence Threshold
```bash
python detect_lira.py --image path/to/your/image.jpg --conf 0.3
```

## Arguments

- `--image` (required): Path to the input image file
- `--model`: Path to the YOLO model weights file (default: `best.pt`)
- `--output`: Path to save the output image with detections (optional)
- `--conf`: Confidence threshold for detections (default: 0.25)

## Output

The script will:
1. Display detection results in the console showing:
   - Number of bills detected for each denomination
   - Subtotal for each denomination
   - Total amount in Turkish Lira
2. Show/display an image with bounding boxes around detected bills
3. Optionally save the annotated image if `--output` is specified

## Example Output

```
==================================================
DETECTION RESULTS
==================================================

Total bills detected: 5

Breakdown by denomination:
  10 Lira: 2 bill(s) = 20 Lira
  20 Lira: 1 bill(s) = 20 Lira
  50 Lira: 1 bill(s) = 50 Lira
  100 Lira: 1 bill(s) = 100 Lira

==================================================
TOTAL AMOUNT: 190 Lira
==================================================
```

## Mobile App (React Native/Expo)

This project includes a mobile app built with Expo/React Native that you can run on your phone!

### Quick Start

1. **Start the API Server:**
   ```bash
   python api_server.py
   ```
   Note: For mobile devices, find your computer's IP address and update `API_URL` in `mobile-app/App.js`

2. **Setup Mobile App:**
   ```bash
   cd mobile-app
   npm install
   npm start
   ```

3. **Run on Your Phone:**
   - Install [Expo Go](https://expo.dev/client) on your phone
   - Scan the QR code shown in the terminal
   - Make sure your phone and computer are on the same WiFi network

See `MOBILE_APP_SETUP.md` for detailed setup instructions.

### Features
- 📷 Take photos with camera
- 🖼️ Select images from gallery  
- 💰 Automatic cash detection
- 📊 Detailed breakdown by denomination
- 🖼️ Annotated image with bounding boxes

