# Troubleshooting Guide

## Error: "java.io.ioexception: failed to download remote update"

This error means Expo Go can't connect to your development server. Try these solutions:

### Solution 1: Use Tunnel Mode (Recommended)

Tunnel mode uses Expo's servers to connect, so it works even if your devices aren't on the same network:

```bash
npm run start:tunnel
```

Then scan the QR code again. This is the easiest solution!

**Note:** Tunnel mode requires an Expo account (free). You'll be prompted to login if needed.

### Solution 2: Check Network Connection

1. **Verify same WiFi network:**
   - Make sure your phone and computer are on the **exact same WiFi network**
   - Some routers have separate 2.4GHz and 5GHz networks - use the same one

2. **Try LAN mode explicitly:**
   ```bash
   npm run start:lan
   ```

3. **Check your computer's IP:**
   - Windows: Run `ipconfig` in Command Prompt
   - Look for "IPv4 Address" under your WiFi adapter
   - Make sure it's not `127.0.0.1` or `localhost`

### Solution 3: Firewall Settings

Your firewall might be blocking the connection:

**Windows:**
1. Open Windows Defender Firewall
2. Click "Allow an app through firewall"
3. Find "Node.js" and make sure both Private and Public are checked
4. If Node.js isn't listed, click "Allow another app" and add it

**Mac:**
1. System Preferences > Security & Privacy > Firewall
2. Click "Firewall Options"
3. Make sure Node.js is allowed

### Solution 4: Use Your Computer's IP Directly

Instead of scanning the QR code, try:

1. Start Expo: `npm start`
2. In Expo Go app, manually enter the connection URL
3. The URL format is: `exp://YOUR_IP:8081`
   - Example: `exp://192.168.1.100:8081`

### Solution 5: Restart Everything

Sometimes a simple restart fixes it:

1. Stop the Expo server (Ctrl+C)
2. Close Expo Go app completely
3. Restart: `npm start`
4. Reopen Expo Go and scan QR code again

### Solution 6: Check Expo CLI Version

Make sure you have the latest Expo CLI:

```bash
npm install -g expo-cli@latest
```

Or use npx (no installation needed):

```bash
npx expo start --tunnel
```

## Other Common Issues

### "Network request failed" when calling API

- Make sure `api_server.py` is running
- Check that `API_URL` in `App.js` uses your computer's IP (not `localhost`)
- Ensure phone and computer are on same network
- Try temporarily disabling firewall to test

### Camera not working

- Grant camera permissions when prompted
- Check phone settings: Settings > Apps > Expo Go > Permissions > Camera

### App crashes on startup

- Check the terminal for error messages
- Make sure all dependencies are installed: `npm install`
- Try clearing Expo cache: `npx expo start -c`

## Still Having Issues?

1. Check the Expo documentation: https://docs.expo.dev/
2. Try the Expo forums: https://forums.expo.dev/
3. Make sure you're using the latest version of Expo Go app

