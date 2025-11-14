# 🇹🇷 Halimi's Lira Counter

A professional mobile application for detecting and counting Turkish Lira cash bills using YOLO11m deep learning model.

## 📱 Features

- **Real-time Detection**: Uses YOLO11m model to detect Turkish Lira denominations (5, 10, 20, 50, 100, 200 Lira)
- **Mobile App**: Beautiful React Native app with Expo
- **API Server**: Flask REST API for image processing
- **Global Deployment**: Ready for Hugging Face Spaces deployment

## 🎯 Detected Denominations

- 5 Lira
- 10 Lira
- 20 Lira
- 50 Lira
- 100 Lira
- 200 Lira

## 🚀 Quick Start

### Local Development

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the API server:**
   ```bash
   python api_server.py
   ```

3. **Run the mobile app:**
   ```bash
   cd mobile-app
   npm install
   npm run start:tunnel
   ```

See `QUICK_START.md` for detailed instructions.

## 📂 Project Structure

```
.
├── api_server.py          # Flask API server
├── detect_lira.py         # Standalone detection script
├── best.pt                # YOLO11m model weights
├── mobile-app/            # React Native mobile app
│   ├── App.js            # Main app component
│   └── package.json      # Dependencies
├── huggingface_space/     # Files for HF Spaces deployment
└── requirements.txt       # Python dependencies
```

## 🌐 Deployment

### Deploy to Hugging Face Spaces

The project is ready for global deployment on Hugging Face Spaces. See `HUGGINGFACE_DEPLOYMENT.md` for complete instructions.

**GitHub Repository**: https://github.com/moiz-q/halimis-lira-counter

## 📱 Mobile App

The mobile app features:
- 📷 Camera integration for taking photos
- 🖼️ Gallery picker for selecting images
- 💰 Automatic cash detection and counting
- 📊 Detailed breakdown by denomination
- 🎨 Modern gradient UI design

## 🔧 API Endpoints

- `GET /health` - Health check
- `POST /detect` - Detect cash in image (expects base64 encoded image)

## 📝 Usage Example

```python
from detect_lira import detect_and_calculate_cash

results = detect_and_calculate_cash('best.pt', 'image.jpg')
print(f"Total: {results['total_amount']} Lira")
```

## 🛠️ Technologies

- **Backend**: Python, Flask, Ultralytics YOLO
- **Mobile**: React Native, Expo
- **Model**: YOLO11m
- **Deployment**: Hugging Face Spaces

## 📄 License

MIT License

## 👤 Author

Halimi's Lira Counter

---

**Note**: Make sure to update the `API_URL` in `mobile-app/App.js` to point to your deployed API server.
