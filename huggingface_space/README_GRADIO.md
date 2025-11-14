---
title: Halimi's Lira Counter
emoji: 💰
colorFrom: purple
colorTo: pink
sdk: gradio
sdk_version: 4.0.0
app_file: app_gradio.py
pinned: false
license: mit
---

# 🇹🇷 Halimi's Lira Counter

A beautiful web application for detecting and counting Turkish Lira cash bills using YOLO11m deep learning model.

## 🎯 Features

- **Web Interface**: Complete web UI that runs entirely on Hugging Face
- **Real-time Detection**: Uses YOLO11m to detect Turkish Lira denominations
- **Visual Annotations**: Shows bounding boxes and labels on detected bills
- **Detailed Breakdown**: Displays count and total for each denomination
- **Adjustable Confidence**: Customize detection sensitivity

## 💵 Supported Denominations

- 5 Lira
- 10 Lira
- 20 Lira
- 50 Lira
- 100 Lira
- 200 Lira

## 🚀 Usage

1. Upload an image containing Turkish Lira bills
2. Adjust the confidence threshold (default: 0.25)
3. Click "Detect Cash" to process
4. View the annotated image and detailed breakdown

## 📊 Output

The app provides:
- **Annotated Image**: Original image with bounding boxes and labels
- **Results Text**: Detailed breakdown showing:
  - Total amount in Lira
  - Number of bills detected
  - Breakdown by denomination

## 🛠️ Technical Details

- **Model**: YOLO11m
- **Framework**: Gradio
- **Backend**: Python, Ultralytics
- **Deployment**: Hugging Face Spaces

## 📝 Notes

- For best results, ensure bills are clearly visible and well-lit
- The model works best with bills laid flat and not overlapping
- Confidence threshold can be adjusted based on image quality

---

**Deployed on Hugging Face Spaces** - Accessible globally! 🌍

