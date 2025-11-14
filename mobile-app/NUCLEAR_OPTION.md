# Nuclear Option - Start from Scratch

If nothing else works, use Expo's built-in template with SDK 54:

## Option 1: Let Expo Create Everything

```bash
# Go back to parent directory
cd ..

# Create a fresh Expo app
npx create-expo-app@latest lira-counter-app --template blank

# Copy just the App.js file
cd lira-counter-app
```

Then copy the contents from `mobile-app/App.js` to the new project.

## Option 2: Use SDK 51 Instead (More Stable)

If SDK 54 keeps causing issues, downgrade to SDK 51 which is more stable:

1. Change package.json:
```json
"expo": "~51.0.0"
```

2. Clean install:
```bash
rmdir /s /q node_modules
del package-lock.json
npm install --legacy-peer-deps
```

SDK 51 uses React 18 which is more stable and has fewer dependency conflicts.

## Why This Happens

Expo SDK 54 is very new (released recently) and some packages haven't caught up yet. Using stable versions or letting Expo manage everything avoids these issues.

