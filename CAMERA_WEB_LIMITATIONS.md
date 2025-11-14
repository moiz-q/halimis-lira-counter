# Camera Web Limitations & Solutions

## Issues with Web Camera

### 1. Blurry Camera on Web Browsers

**Why it happens:**
- Web browsers have limited access to camera hardware
- Browser camera API doesn't support the same quality settings as native apps
- Most browsers use lower resolution for `getUserMedia()` (MediaStream API)
- Quality is often capped at 720p or 1080p depending on browser

**Current settings (already applied):**
```javascript
videoQuality="1080p"  // In CameraView
quality: 1.0          // Maximum quality in takePictureAsync
```

**Browser limitations:**
- Chrome/Edge: Usually 720p-1080p
- Firefox: Similar limitations
- Safari (iOS): More restricted on web
- Native apps (Expo Go): Full camera access ✅

**Solutions:**

1. **Best**: Use the file upload (gallery) instead
   - This gives you full image quality
   - Users can take photo with native camera app first
   - Then upload it

2. **Alternative**: Native app build
   - Build with EAS (Expo Application Services)
   - Install actual app on phone
   - Gets full native camera quality

3. **Accept the limitation**:
   - Web camera is inherently lower quality
   - Still works for detection, just not as sharp
   - Trade-off for web accessibility

### 2. Screen Goes White After Camera Capture

**Fixed with better error handling**

Added try-catch in camera capture handler to show actual error instead of white screen.

**If still happening:**
- Check browser console for errors (F12)
- Look for specific error message
- May be due to base64 conversion on large images

## Recommendations

### For Best Quality:
1. **Use Gallery Upload** — Full camera quality
2. Take photo with native camera app first
3. Upload it to the web app

### For Convenience:
1. **Keep using web camera** — Works but lower quality
2. Make sure lighting is good
3. Hold still when capturing
4. Get close to bills

### For Perfect Experience:
1. **Build native app**:
   ```bash
   cd mobile-app
   eas build --platform android
   ```
2. Install on phone
3. Full native camera access

## Why Gallery Upload Works Better

- Uses photos taken with native camera app
- Full resolution (often 12MP+)
- Better focus and stabilization
- Post-processing by camera app
- No web browser limitations

## Browser Camera API Constraints

The MediaStream API (used by web browsers) has these limits:
- Resolution: Usually 1280x720 or 1920x1080 max
- Frame rate: 30fps typical
- No manual focus control
- No exposure control
- Limited zoom
- Auto settings only

Native camera apps have:
- Full sensor resolution (12MP, 48MP, etc.)
- Manual controls
- HDR, night mode, etc.
- Better image processing

## Bottom Line

**For best results on web:** Use the "Choose Gallery" button instead of camera. Take photos with your phone's native camera app first, then upload them.

**For native-quality camera:** Build and install the native app version using EAS.

