# Complete Deployment Guide: Halimi's Lira Counter on Hugging Face

**One guide. Everything you need. No clutter.**

## What You're Deploying

Complete web application (frontend + backend) that runs entirely on Hugging Face Spaces. Accessible from any browser worldwide.

## Step 1: Create New Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name**: `halimis-lira-counter`
   - **SDK**: Select **"Gradio"**
   - **Hardware**: CPU Basic (free)
   - **Visibility**: Public
4. Click **"Create Space"**

Your Space URL: `https://huggingface.co/spaces/moizncai/halimis-lira-counter`

## Step 2: Clone Repositories

```bash
# Clone GitHub repo (has all the code)
git clone https://github.com/moiz-q/halimis-lira-counter.git
cd halimis-lira-counter

# Clone your Hugging Face Space (where you'll deploy)
cd ..
git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
cd halimis-lira-counter
```

## Step 3: Copy Required Files

Copy these 4 files from GitHub repo to HF Space:

```bash
# From the huggingface_space directory
cp ../halimis-lira-counter/huggingface_space/app_expo_web.py app.py
cp ../halimis-lira-counter/huggingface_space/requirements.txt .
cp ../halimis-lira-counter/best.pt .
cp ../halimis-lira-counter/huggingface_space/README_GRADIO.md README.md
```

**Your HF Space should have:**
- `app.py` (the Gradio application)
- `requirements.txt` (dependencies)
- `README.md` (Space description)
- `best.pt` (YOLO model)

## Step 4: Handle Large Model File (if needed)

If `best.pt` is larger than 100MB:

```bash
git lfs install
git lfs track "*.pt"
git add .gitattributes best.pt
```

## Step 5: Deploy

```bash
# Add all files
git add .

# Commit
git commit -m "Deploy complete web app"

# Push to Hugging Face
git push
```

## Step 6: Wait for Build

1. Go to: https://huggingface.co/spaces/moizncai/halimis-lira-counter
2. Click **"Logs"** tab to watch build progress
3. Wait 5-15 minutes
4. Status changes to **"Running"** when ready

## Step 7: Use Your App

Your app is live at: **https://moizncai-halimis-lira-counter.hf.space**

Open in any browser:
1. Upload image with Turkish Lira bills
2. Adjust confidence slider (default: 0.25)
3. Click "🔍 Detect Cash"
4. View annotated image and breakdown

## Troubleshooting

**Build fails?**
- Check Logs tab for errors
- Ensure all 4 files are in root directory
- Verify `app.py` exists (not `app_gradio.py`)

**Model too large?**
- Use Git LFS (see Step 4)
- Or compress model if possible

**App not loading?**
- Wait for build to complete
- Refresh browser
- Check Space status is "Running"

## Updating

To update your app:

```bash
cd halimis-lira-counter  # Your HF Space directory
# Make changes to files
git add .
git commit -m "Update: [describe changes]"
git push
```

Auto-rebuilds on push.

## What You Get

✅ Complete web app (frontend + backend)  
✅ Global access via browser  
✅ No installation needed  
✅ Works on phones, tablets, desktops  
✅ Free hosting  
✅ Beautiful UI with gradients  

## Optional: Add Expo Web Version

If you want your exact Expo mobile app UI on web too:

1. Build Expo for web: `cd mobile-app && npx expo export -p web`
2. Copy `web-build/` folder to HF Space
3. Serve alongside Gradio (requires Flask integration)

See `BUILD_EXPO_WEB.md` for details.

---

**That's it!** One guide. Everything you need. Your app is live at:
**https://moizncai-halimis-lira-counter.hf.space**
