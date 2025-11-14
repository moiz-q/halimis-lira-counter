# Complete Deployment Guide - Phone App on Hugging Face

**Everything in one place. Globally accessible. Free.**

This deploys your complete phone app (frontend + backend) to Hugging Face Spaces.

---

## Quick Overview

1. Build Expo app for web
2. Copy files to HF Space
3. Push to Hugging Face
4. Share the URL

**Time:** ~15 minutes  
**Cost:** Free

---

## Step 1: Build Expo for Web

```bash
cd mobile-app

# Install dependencies (if not done)
npm install

# Build for web
npx expo export -p web
```

This creates `mobile-app/web-build/` with your app.

---

## Step 2: Prepare HF Space Directory

```bash
# Go to project root
cd ..

# Create deployment directory
mkdir hf-complete-deploy
cd hf-complete-deploy
```

---

## Step 3: Copy All Files

```bash
# Copy Expo web build (rename to 'web')
cp -r ../mobile-app/web-build ./web

# Copy model file
cp ../best.pt .

# Copy Flask app (from huggingface_space folder)
cp ../huggingface_space/app_complete.py app.py

# Copy requirements
cp ../huggingface_space/requirements_complete.txt requirements.txt

# Copy Dockerfile
cp ../huggingface_space/Dockerfile_complete Dockerfile

# Copy README
cp ../huggingface_space/README_complete.md README.md

# Copy PWA manifest
cp ../huggingface_space/manifest.json ./web/
```

**Your directory should have:**
```
hf-complete-deploy/
├── app.py                  # Flask server (frontend + backend)
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker config
├── README.md              # Space description
├── best.pt                # YOLO model
└── web/                   # Expo web build
    ├── index.html
    ├── manifest.json      # PWA config
    └── ... (other web files)
```

---

## Step 4: Update API URL in Web Build

The Expo build needs to know where the API is. Since everything is on the same server, update the API URL:

```bash
# On Windows (PowerShell):
cd web
(Get-Content -Path index.html) -replace 'https://moizncai-halimis-lira-counter.hf.space', '' | Set-Content -Path index.html

# On Mac/Linux:
cd web
sed -i 's|https://moizncai-halimis-lira-counter.hf.space|/detect|g' index.html
cd ..
```

Or manually edit `web/index.html` and search for the API URL, change it to `/detect` (relative path).

---

## Step 5: Deploy to Hugging Face

### First Time Setup

```bash
# Go back to parent directory
cd ..

# Clone your HF Space (delete old one first if it exists)
git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
cd halimis-lira-counter

# Remove old files
rm -rf *

# Copy new files
cp -r ../hf-complete-deploy/* .

# If model is large (>100MB), use Git LFS
git lfs install
git lfs track "*.pt"
git add .gitattributes
```

### Commit and Push

```bash
# Add all files
git add .

# Commit
git commit -m "Deploy complete PWA with frontend and backend"

# Push to Hugging Face
git push
```

---

## Step 6: Wait for Build

1. Go to: https://huggingface.co/spaces/moizncai/halimis-lira-counter
2. Click **"Logs"** tab
3. Watch build progress (10-15 minutes)
4. Status changes to **"Running"** when ready

---

## Step 7: Access Your App

**Your app is live at:**
https://moizncai-halimis-lira-counter.hf.space

### On Computer:
- Open URL in browser
- Upload image and detect cash

### On Phone:
1. Open URL in browser (Safari/Chrome)
2. Use the app
3. Optional: **Install as app:**
   - **iPhone:** Safari → Share → "Add to Home Screen"
   - **Android:** Chrome → Menu → "Install app"
4. Launch from home screen like native app

---

## What You Get

✅ **Complete phone app** - Your exact Expo UI  
✅ **Frontend on HF** - Served by Flask  
✅ **Backend on HF** - Same server  
✅ **One URL** - Easy to share  
✅ **Installable** - Acts like native app  
✅ **Global access** - Works worldwide  
✅ **Free hosting** - HF free tier  
✅ **Auto HTTPS** - Secure by default  

---

## Share with Others

Just send them the URL:
**https://moizncai-halimis-lira-counter.hf.space**

They can:
- Use it in browser immediately
- Install it as an app on their phone
- Access it from anywhere

---

## Troubleshooting

### Build fails
- Check "Logs" tab in HF Space
- Ensure all files are in root directory
- Verify `Dockerfile`, `app.py`, and `best.pt` exist

### App loads but API fails
- Check that API URL in web build is correct
- Should be `/detect` (relative) or full HF Space URL
- Check browser console for errors

### Model file too large
- Use Git LFS: `git lfs track "*.pt"`
- Or use smaller model if available

### App not installable
- Ensure `manifest.json` is in `/web/` folder
- Check that HF Space serves it at root URL
- Try different browser

### Camera not working on web
- Web camera API is limited
- Use file upload instead (already in your app)
- Or use `<input type="file" capture="camera">` in HTML

---

## Updating Your App

To update:

```bash
cd halimis-lira-counter  # Your HF Space directory

# Make changes (rebuild Expo if needed)
# Copy new web-build to ./web/

# Commit and push
git add .
git commit -m "Update: [describe changes]"
git push
```

HF automatically rebuilds.

---

## Performance Optimization

**If app is slow:**
1. Go to HF Space settings
2. Upgrade hardware (from CPU to GPU)
3. Costs money but much faster detection

**Free tier is usually fine for personal use.**

---

## Summary Commands

**Full deployment in one go:**

```bash
# Build web
cd mobile-app && npx expo export -p web && cd ..

# Prepare files
mkdir hf-complete-deploy && cd hf-complete-deploy
cp -r ../mobile-app/web-build ./web
cp ../best.pt .
cp ../huggingface_space/app_complete.py app.py
cp ../huggingface_space/requirements_complete.txt requirements.txt
cp ../huggingface_space/Dockerfile_complete Dockerfile
cp ../huggingface_space/README_complete.md README.md
cp ../huggingface_space/manifest.json ./web/
cd ..

# Deploy to HF
git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
cd halimis-lira-counter
rm -rf * && cp -r ../hf-complete-deploy/* .
git lfs install && git lfs track "*.pt"
git add . && git commit -m "Deploy complete PWA" && git push
```

---

**That's it! Your phone app is now globally accessible at:**
**https://moizncai-halimis-lira-counter.hf.space**

Share the link. Anyone can use it. Anyone can install it. All for free. 🚀

