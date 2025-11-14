# Fix for "PlatformConstants could not be found" Error

This error occurs due to version mismatches. Follow these steps:

## Solution:

1. **Delete node_modules and package-lock.json:**
   ```bash
   cd mobile-app
   rmdir /s /q node_modules
   del package-lock.json
   ```
   (On Mac/Linux: `rm -rf node_modules package-lock.json`)

2. **Install using Expo's install command (this ensures correct versions):**
   ```bash
   npx expo install --fix
   ```
   
   This will automatically install the correct React Native version and all compatible packages.

3. **Clear Expo cache and restart:**
   ```bash
   npx expo start --clear
   ```

4. **If still having issues, try:**
   ```bash
   npx expo start --tunnel --clear
   ```

## Why This Happens:

- Manually specifying React Native versions can cause mismatches
- Expo SDK 54 requires specific React Native version that `expo install` knows about
- Using `npm install` instead of `expo install` can install incompatible versions

## Alternative Quick Fix:

If the above doesn't work, you can also try:
```bash
cd mobile-app
rmdir /s /q node_modules
npm install
npx expo install expo react react-native --fix
npx expo start --clear
```

The key is using `expo install --fix` which ensures all versions are compatible!

