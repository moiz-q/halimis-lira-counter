# Fix "Network request failed" Error

## The app works! Now connect it to the API:

### Step 1: Find your computer's IP address

**Windows:**
```bash
ipconfig
```
Look for "IPv4 Address" under your WiFi adapter (e.g., 192.168.1.100)

**Mac/Linux:**
```bash
ifconfig
```
Look for your WiFi IP address

### Step 2: Update API_URL in App.js

Open `mobile-app/App.js` and change line 20:

```javascript
// Change this:
const API_URL = 'http://localhost:8080';

// To this (use YOUR IP):
const API_URL = 'http://192.168.1.XXX:8080';
```

Replace `192.168.1.XXX` with your actual IP address.

### Step 3: Start the API Server

In a NEW terminal window:
```bash
cd D:\Moiz_Stuffs\Lira_Counter
python api_server.py
```

You should see: `API will be available at http://localhost:8080`

### Step 4: Test the App

1. Make sure your phone and computer are on the **same WiFi network**
2. Take a photo in the app
3. The API should process it and show results!

## Troubleshooting

**Still getting Network request failed?**
- ✅ Check API server is running (`python api_server.py`)
- ✅ Verify phone and computer are on same WiFi
- ✅ Check Windows Firewall isn't blocking port 8080
- ✅ Try temporarily disabling firewall to test

**API server not starting?**
- Make sure you installed: `pip install -r requirements.txt`
- Check that `best.pt` (YOLO model) is in the folder

