# Quick Fix for Runtime Error

## Run these commands in order:

```bash
cd mobile-app

# 1. Remove old dependencies
rmdir /s /q node_modules
del package-lock.json

# 2. Install with Expo (ensures correct versions)
npx expo install --fix

# 3. Clear cache and start
npx expo start --tunnel --clear
```

**On Mac/Linux, use:**
```bash
cd mobile-app
rm -rf node_modules package-lock.json
npx expo install --fix
npx expo start --tunnel --clear
```

The key is using `expo install --fix` instead of `npm install` - this ensures React Native and all packages match Expo SDK 54!

