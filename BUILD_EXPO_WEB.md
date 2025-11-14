# Build Expo App for Web and Deploy to Hugging Face

Yes! You can run your Expo app on Hugging Face. Here's how to convert it to web and deploy.

## Step 1: Build Expo App for Web

```bash
cd mobile-app

# Install dependencies (if not already done)
npm install

# Build for web
npx expo export -p web
```

This creates a `web-build/` folder with static HTML/JS files.

## Step 2: Update API URL for Web

Before building, update `mobile-app/App.js`:

```javascript
// For Hugging Face deployment
const API_URL = 'https://moizncai-halimis-lira-counter.hf.space';
```

## Step 3: Deploy to Hugging Face

### Option A: Static HTML Space (Simplest)

1. Create a new Space with **"Static"** SDK
2. Upload the contents of `web-build/` folder
3. Done! Your Expo app is live

### Option B: Integrate with Gradio (Current Space)

Add the web build to your existing Gradio Space:

1. Copy `web-build/` to your HF Space
2. Serve static files alongside Gradio
3. Access via: `https://moizncai-halimis-lira-counter.hf.space/web/`

## Step 4: Update for Web Compatibility

Some Expo features don't work on web:
- Camera: Use file upload instead
- Native modules: May need web alternatives

The app should mostly work, but camera might need adjustment.

## Quick Deploy Command

```bash
# Build web version
cd mobile-app
npx expo export -p web

# Copy to HF Space
cd ..
cd halimis-lira-counter  # Your HF Space
cp -r ../halimis-lira-counter/mobile-app/web-build/* ./web/

# Commit and push
git add web/
git commit -m "Add Expo web build"
git push
```

## Result

Your Expo app will be accessible at:
- Gradio interface: `https://moizncai-halimis-lira-counter.hf.space`
- Expo web app: `https://moizncai-halimis-lira-counter.hf.space/web/` (if integrated)

---

**Note:** The Gradio version is simpler and works great. But if you want your exact Expo UI, this is how to do it!

