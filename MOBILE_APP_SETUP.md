# Mobile App Setup Guide

## Quick Start

### Option 1: API-Based (Recommended - Easiest)

This approach uses your existing Python code via a Flask API server.

#### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### Step 2: Start the API Server
```bash
python api_server.py
```
The server will run on `http://localhost:8080`

**Important**: For mobile devices to connect, you need to use your computer's IP address instead of `localhost`. Find your IP:
- **Windows**: Run `ipconfig` and look for "IPv4 Address"
- **Mac/Linux**: Run `ifconfig` or `ip addr`

Then update the `API_URL` in `mobile-app/App.js` to use your IP (e.g., `http://192.168.1.100:8080`)

#### Step 3: Setup Mobile App
```bash
cd mobile-app
npm install
```

#### Step 4: Run the App
```bash
npm start
```

Then scan the QR code with Expo Go app on your phone.

---

## Architecture

### API Server (`api_server.py`)
- Flask REST API
- Accepts base64-encoded images
- Returns detection results with annotated images
- Runs on port 8080

### Mobile App (`mobile-app/`)
- React Native with Expo
- Camera and image picker integration
- Sends images to API server
- Displays results with breakdown

---

## Network Configuration

### For Local Development:

1. **Find your computer's IP address:**
   ```bash
   # Windows
   ipconfig
   
   # Mac/Linux
   ifconfig
   # or
   ip addr
   ```

2. **Update `mobile-app/App.js`:**
   ```javascript
   const API_URL = 'http://YOUR_IP_ADDRESS:8080';
   // Example: const API_URL = 'http://192.168.1.100:8080';
   ```

3. **Ensure same WiFi network:**
   - Your phone and computer must be on the same WiFi network
   - Or use your computer as a mobile hotspot

4. **Firewall:**
   - You may need to allow port 8080 through your firewall
   - Windows: Windows Defender Firewall > Allow an app
   - Mac: System Preferences > Security & Privacy > Firewall

### For Production:

Deploy the API server to a cloud service (Heroku, AWS, Google Cloud, etc.) and update the `API_URL` in the mobile app.

---

## Testing

1. Start the API server: `python api_server.py`
2. Test the API endpoint:
   ```bash
   curl http://localhost:8080/health
   ```
   Should return: `{"status":"healthy","model_loaded":true}`

3. Run the mobile app and test with a sample image

---

## Alternative: On-Device Detection (Advanced)

If you want the app to work offline without an API server, you would need to:
1. Convert the YOLO model to TensorFlow Lite or ONNX
2. Use React Native ML libraries (e.g., `@tensorflow/tfjs-react-native`)
3. Implement the detection logic in JavaScript/TypeScript

This is more complex but enables offline functionality.

