# Complete Deployment Guide: Halimi's Lira Counter on Hugging Face

This is the **only guide you need** to deploy the complete web application (frontend + backend) on Hugging Face Spaces.

## What You're Deploying

- ✅ Complete web application (frontend + backend)
- ✅ Runs entirely on Hugging Face
- ✅ Accessible from any browser worldwide
- ✅ No mobile app installation needed
- ✅ Beautiful Gradio interface

## Step 1: Create New Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in:
   - **Space name**: `halimis-lira-counter`
   - **SDK**: Select **"Gradio"** (NOT Docker)
   - **Hardware**: CPU Basic (free) or upgrade if needed
   - **Visibility**: Public
4. Click **"Create Space"**

Your Space URL will be: `https://huggingface.co/spaces/moizncai/halimis-lira-counter`

## Step 2: Clone and Prepare Files

Open terminal/command prompt and run:

```bash
# Clone your GitHub repo
git clone https://github.com/moiz-q/halimis-lira-counter.git
cd halimis-lira-counter

# Clone your new Hugging Face Space
cd ..
git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
cd halimis-lira-counter
```

## Step 3: Copy Required Files

From the GitHub repo, copy these files to your HF Space:

```bash
# Copy the Gradio app (rename to app.py)
cp ../halimis-lira-counter/huggingface_space/app_gradio.py app.py

# Copy requirements
cp ../halimis-lira-counter/huggingface_space/requirements.txt .

# Copy the model file
cp ../halimis-lira-counter/best.pt .

# Copy README
cp ../halimis-lira-counter/huggingface_space/README_GRADIO.md README.md
```

**Required files in your HF Space:**
- `app.py` (the Gradio application)
- `requirements.txt` (dependencies)
- `README.md` (Space description)
- `best.pt` (YOLO model file)

## Step 4: Handle Large Model File (if needed)

If `best.pt` is larger than 100MB, use Git LFS:

```bash
# Install Git LFS (if not already installed)
git lfs install

# Track .pt files
git lfs track "*.pt"

# Add and commit
git add .gitattributes
git add best.pt
```

## Step 5: Commit and Push

```bash
# Add all files
git add .

# Commit
git commit -m "Initial deployment: Complete Gradio web app"

# Push to Hugging Face
git push
```

## Step 6: Wait for Build

- Go to your Space page: https://huggingface.co/spaces/moizncai/halimis-lira-counter
- Watch the build logs (click "Logs" tab)
- Build takes 5-15 minutes
- Status will change from "Building" to "Running" when ready

## Step 7: Access Your Web App

Once built, your app is live at:
**https://moizncai-halimis-lira-counter.hf.space**

Open this URL in any browser to use the app!

## How to Use the Web App

1. **Upload Image**: Click the upload area and select an image with Turkish Lira bills
2. **Adjust Confidence**: Use the slider to set detection sensitivity (default: 0.25)
3. **Detect**: Click "🔍 Detect Cash" button
4. **View Results**: 
   - See annotated image with bounding boxes
   - Read detailed breakdown with totals

## File Structure in HF Space

Your Space should have exactly these files:
```
halimis-lira-counter/
├── app.py              # Main Gradio application
├── requirements.txt    # Python dependencies
├── README.md          # Space description
└── best.pt            # YOLO model (may use Git LFS)
```

## Troubleshooting

### Build Fails
- Check the "Logs" tab in your Space
- Ensure all files are in the root directory
- Verify `app.py` exists and is named correctly
- Check that `requirements.txt` has all dependencies

### Model File Too Large
- Use Git LFS (see Step 4)
- Or compress the model if possible
- Or use a model hosting service and load from URL

### App Not Loading
- Wait for build to complete (check status)
- Refresh the page
- Check browser console for errors
- Verify the Space is set to "Gradio" SDK

### Slow Performance
- Free tier uses CPU (slower)
- Upgrade to GPU in Space settings for faster inference
- Or optimize model size

## Updating Your Deployment

To update the app:

```bash
cd halimis-lira-counter  # Your HF Space directory

# Make changes to files
# Then:
git add .
git commit -m "Update: [describe changes]"
git push
```

Hugging Face will automatically rebuild.

## What You Get

✅ **Complete Web Application**: Frontend + Backend in one  
✅ **Global Access**: Anyone can use it via web browser  
✅ **No Installation**: Just share the link  
✅ **Mobile Friendly**: Works on phones, tablets, desktops  
✅ **Free Hosting**: Runs on Hugging Face free tier  
✅ **Automatic Updates**: Rebuilds on every push  

## API Access (Optional)

If you also want API endpoints for the mobile app, you can:
1. Keep this Space as web app
2. Create a second Space with Docker SDK for API-only
3. Or add Flask routes to the Gradio app (more complex)

## Summary

**One command to deploy:**
```bash
# After cloning both repos:
cp ../halimis-lira-counter/huggingface_space/app_gradio.py app.py && \
cp ../halimis-lira-counter/huggingface_space/requirements.txt . && \
cp ../halimis-lira-counter/huggingface_space/README_GRADIO.md README.md && \
cp ../halimis-lira-counter/best.pt . && \
git add . && \
git commit -m "Deploy complete web app" && \
git push
```

**That's it!** Your app will be live at: https://moizncai-halimis-lira-counter.hf.space

---

**Need help?** Check the build logs in your Space or the Hugging Face documentation.

