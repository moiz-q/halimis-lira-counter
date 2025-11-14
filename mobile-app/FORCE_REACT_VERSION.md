# Force React 19.1.1 to Fix Version Mismatch

## The Problem
npm keeps installing React 19.2.0 instead of 19.1.1, causing version mismatch with react-native-renderer.

## Solution: Force the exact version

1. **Delete everything first:**
   ```bash
   cd mobile-app
   rmdir /s /q node_modules
   del package-lock.json
   ```

2. **Install with force and legacy-peer-deps:**
   ```bash
   npm install react@19.1.1 --save-exact --legacy-peer-deps
   npm install react-native@0.79.3 --save-exact --legacy-peer-deps
   npm install --legacy-peer-deps
   ```

3. **Clear cache and restart:**
   ```bash
   npx expo start --clear
   ```

## Alternative: If still not working

Try downgrading Expo or using npm 8 instead of npm 10:

```bash
# Check npm version
npm -v

# If npm 10+, try with legacy behavior
npm config set legacy-peer-deps true

# Then reinstall
cd mobile-app
rmdir /s /q node_modules
del package-lock.json
npm install
```

The `overrides` field in package.json should force React 19.1.1, but npm 10+ sometimes ignores it. The `--save-exact` flag ensures no version updates.

