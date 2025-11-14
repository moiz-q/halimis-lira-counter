# Quick Start Guide

## 🚀 Get Your Mobile App Running in 5 Minutes

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Start the API Server
```bash
python api_server.py
```
You should see: `Starting Flask API server...` and `API will be available at http://localhost:8080`

**Important:** Note your computer's IP address:
- **Windows:** Open Command Prompt and run `ipconfig`, look for "IPv4 Address"
- **Mac/Linux:** Run `ifconfig` or `ip addr`, look for your WiFi IP

### Step 3: Setup Mobile App
Open a **new terminal window** and run:
```bash
cd mobile-app
npm install
```

### Step 4: Update API URL
Edit `mobile-app/App.js` and change this line:
```javascript
const API_URL = 'http://localhost:8080';
```
To use your computer's IP address:
```javascript
const API_URL = 'http://192.168.1.XXX:8080'; // Replace XXX with your IP (port is 8080)
```

### Step 5: Start the Mobile App

**Option A: Tunnel Mode (Easiest - works even on different networks)**
```bash
npm run start:tunnel
```
This uses Expo's servers to connect, so it works even if your phone and computer aren't on the same WiFi.

**Option B: Regular Mode (requires same WiFi network)**
```bash
npm start
```

**If you get connection errors, use tunnel mode (Option A)!**

### Step 6: Run on Your Phone
1. Install **Expo Go** app:
   - [iOS App Store](https://apps.apple.com/app/expo-go/id982107779)
   - [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)

2. Make sure your phone and computer are on the **same WiFi network**

3. Scan the QR code that appears in the terminal:
   - **iOS:** Use the Camera app
   - **Android:** Use the Expo Go app

### Step 7: Test It!
1. Open the app on your phone
2. Tap "Take Photo" or "Choose from Gallery"
3. Select/take a photo of Turkish Lira bills
4. Wait for detection results!

## Troubleshooting

### "Failed to download remote update" error?
**✅ Use tunnel mode instead:**
```bash
npm run start:tunnel
```
This is the easiest fix! See `mobile-app/TROUBLESHOOTING.md` for more solutions.

### Can't connect to API?
- ✅ Make sure API server is running (`python api_server.py`)
- ✅ Check that IP address in `App.js` matches your computer's IP
- ✅ Ensure phone and computer are on same WiFi (or use tunnel mode)
- ✅ Try disabling firewall temporarily to test

### Camera not working?
- Grant camera permissions when prompted
- Check phone settings: Settings > Apps > Expo Go > Permissions

### Still having issues?
Check `mobile-app/TROUBLESHOOTING.md` for detailed troubleshooting.

