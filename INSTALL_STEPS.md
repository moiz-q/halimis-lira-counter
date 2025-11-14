# Installation Steps (Fix Dependency Conflicts)

## Step 1: Clean Everything
```bash
cd mobile-app
rmdir /s /q node_modules
del package-lock.json
```

## Step 2: Install with Legacy Peer Deps (to resolve conflicts)
```bash
npm install --legacy-peer-deps
```

## Step 3: Let Expo Fix All Versions
```bash
npx expo install --fix
```

## Step 4: Start with Clear Cache
```bash
npx expo start --tunnel --clear
```

## Alternative: If Step 2-3 don't work, try this:

```bash
# Clean
rmdir /s /q node_modules
del package-lock.json

# Install expo first
npm install expo@~54.0.0 --legacy-peer-deps

# Then let expo install fix everything
npx expo install --fix

# Start
npx expo start --tunnel --clear
```

The `--legacy-peer-deps` flag tells npm to ignore peer dependency conflicts, which is needed because Expo SDK 54 uses React 19, but some packages might still expect React 18.

