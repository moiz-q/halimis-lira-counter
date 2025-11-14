# Halimi's Lira Counter Mobile App

React Native mobile app built with Expo for detecting and counting Turkish Lira cash bills.

## Setup

1. Install dependencies:
```bash
cd mobile-app
npm install
```

2. Update the API URL in `App.js`:
   - For local development: Change `API_URL` to your computer's IP address (e.g., `http://192.168.1.100:8080`)
   - Find your IP: 
     - Windows: `ipconfig` (look for IPv4 Address)
     - Mac/Linux: `ifconfig` or `ip addr`

3. Make sure the API server is running (see main README.md)

## Running the App

### Using Expo Go (Easiest)

1. Install Expo Go on your phone:
   - [iOS App Store](https://apps.apple.com/app/expo-go/id982107779)
   - [Google Play Store](https://play.google.com/store/apps/details?id=host.exp.exponent)

2. Start the development server:

**Option A: Tunnel Mode (Recommended - works on any network)**
```bash
npm run start:tunnel
```

**Option B: Regular Mode (requires same WiFi)**
```bash
npm start
```

**If you get connection errors, use tunnel mode!**

3. Scan the QR code with:
   - **iOS**: Camera app
   - **Android**: Expo Go app

### Building Standalone App

To create a standalone app:

```bash
# Install EAS CLI
npm install -g eas-cli

# Login to Expo
eas login

# Build for Android
eas build --platform android

# Build for iOS (requires Apple Developer account)
eas build --platform ios
```

## Features

- 📷 Take photos with camera
- 🖼️ Select images from gallery
- 💰 Automatic cash detection
- 📊 Detailed breakdown by denomination
- 🖼️ Annotated image with bounding boxes

## Troubleshooting

### Can't connect to API server
- Make sure your phone and computer are on the same WiFi network
- Check that the API server is running (`python api_server.py`)
- Verify the IP address in `App.js` matches your computer's IP
- Try disabling firewall temporarily to test

### Camera not working
- Make sure you've granted camera permissions
- On iOS, check Settings > Privacy > Camera

### Image picker not working
- Make sure you've granted photo library permissions
- On iOS, check Settings > Privacy > Photos

