---
title: Halimi's Lira Counter API
emoji: 💰
colorFrom: purple
colorTo: pink
sdk: docker
pinned: false
license: mit
---

# Halimi's Lira Counter API

A Flask API server for detecting and counting Turkish Lira cash bills using YOLO11m model.

## API Endpoints

### Health Check
```
GET /health
```

### Detect Cash
```
POST /detect
Content-Type: application/json

{
  "image": "base64_encoded_image_string",
  "conf": 0.25
}
```

## Response Format

```json
{
  "success": true,
  "total_amount": 190,
  "total_bills": 4,
  "counts": {
    "10": 0,
    "100": 1,
    "20": 2,
    "200": 0,
    "5": 0,
    "50": 1
  },
  "detections": [...],
  "annotated_image": "base64_encoded_image"
}
```

## Usage

The API is accessible at: `https://YOUR-USERNAME-halimis-lira-counter.hf.space`

Update your mobile app's `API_URL` to point to this URL.

