---
title: Halimi's Lira Counter
emoji: 💰
colorFrom: purple
colorTo: pink
sdk: docker
app_port: 7860
pinned: false
license: mit
---

# 🇹🇷 Halimi's Lira Counter

A Progressive Web App (PWA) for detecting and counting Turkish Lira cash bills using YOLO11m deep learning model.

## 🌐 Access the App

**Web App:** https://moizncai-halimis-lira-counter.hf.space

**Install on Phone:**
1. Open the link on your phone
2. Tap menu (⋮) → "Add to Home Screen"
3. Launch like a native app!

## 🎯 Features

- 📱 **Progressive Web App**: Install on any phone
- 📷 **Image Upload**: Take or choose photos
- 🤖 **AI Detection**: YOLO11m model
- 💵 **6 Denominations**: 5, 10, 20, 50, 100, 200 Lira
- 🖼️ **Visual Annotations**: Bounding boxes and labels
- 📊 **Detailed Breakdown**: Count and total per denomination
- 🌍 **Global Access**: Works anywhere in the world

## 🚀 How to Use

1. **Open the app** in your browser
2. **Take or upload** a photo of Turkish Lira bills
3. **Tap "Detect Cash"** to analyze
4. **View results** with annotated image and totals

## 📱 Install as Native App

### On iPhone:
1. Open Safari → Visit the app URL
2. Tap Share button (⬆️)
3. Tap "Add to Home Screen"
4. Tap "Add"

### On Android:
1. Open Chrome → Visit the app URL
2. Tap menu (⋮)
3. Tap "Install app" or "Add to Home Screen"
4. Tap "Install"

## 🛠️ Technical Stack

- **Frontend**: React Native (Expo) compiled to web
- **Backend**: Flask API
- **Model**: YOLO11m
- **Deployment**: Hugging Face Spaces (Docker)
- **Hosting**: Free tier

## 💵 Supported Denominations

- 5 Lira
- 10 Lira
- 20 Lira
- 50 Lira
- 100 Lira
- 200 Lira

## 📝 API Endpoints

### `GET /health`
Health check endpoint.

### `POST /detect`
Detect cash in image.

**Request:**
```json
{
  "image": "base64_encoded_image",
  "confidence": 0.25
}
```

**Response:**
```json
{
  "success": true,
  "total_amount": 150,
  "total_bills": 3,
  "breakdown": {
    "50": {"count": 2, "subtotal": 100},
    "10": {"count": 5, "subtotal": 50}
  },
  "annotated_image": "base64_encoded_image"
}
```

## 🌟 Why PWA?

- ✅ No app store approval needed
- ✅ Works on all devices
- ✅ Instant updates
- ✅ Smaller size than native apps
- ✅ One codebase for all platforms

## 🔒 Privacy

- No data stored or logged
- All processing happens on server
- Images not saved
- No tracking or analytics

---

**Deployed on Hugging Face Spaces** - Free, fast, global access! 🌍

