# Deploying to Hugging Face Spaces

This guide will help you deploy the Halimi's Lira Counter API to Hugging Face Spaces so it can be accessed globally.

## Prerequisites

1. A Hugging Face account (sign up at https://huggingface.co)
2. Git installed on your computer
3. The `best.pt` model file

## Step 1: Prepare Files

1. Copy the files from `huggingface_space/` directory:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `Dockerfile`
   - `best.pt` (your YOLO model)

## Step 2: Create a Hugging Face Space

1. Go to https://huggingface.co/spaces
2. Click **"Create new Space"**
3. Fill in the details:
   - **Space name**: `halimis-lira-counter` (or your preferred name)
   - **SDK**: Select **"Docker"**
   - **Visibility**: Public or Private (your choice)
4. Click **"Create Space"**

## Step 3: Upload Files

### Option A: Using Git (Recommended)

1. **Clone your space repository:**
   ```bash
   git clone https://huggingface.co/spaces/YOUR_USERNAME/halimis-lira-counter
   cd halimis-lira-counter
   ```

2. **Copy all files:**
   ```bash
   # Copy from the huggingface_space directory
   cp ../huggingface_space/* .
   cp ../best.pt .
   ```

3. **Commit and push:**
   ```bash
   git add .
   git commit -m "Initial deployment"
   git push
   ```

### Option B: Using Web Interface

1. Go to your Space page
2. Click **"Files and versions"** tab
3. Click **"Add file"** → **"Upload file"**
4. Upload each file:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `Dockerfile`
   - `best.pt`

## Step 4: Wait for Build

- Hugging Face will automatically build your Space
- This can take 5-10 minutes
- You'll see build logs in the Space page
- Once built, your API will be live at: `https://YOUR_USERNAME-halimis-lira-counter.hf.space`

## Step 5: Update Mobile App

1. Open `mobile-app/App.js`
2. Update the `API_URL`:
   ```javascript
   const API_URL = 'https://YOUR_USERNAME-halimis-lira-counter.hf.space';
   ```
   Replace `YOUR_USERNAME` with your actual Hugging Face username.

3. The API endpoints will be:
   - Health: `https://YOUR_USERNAME-halimis-lira-counter.hf.space/health`
   - Detect: `https://YOUR_USERNAME-halimis-lira-counter.hf.space/detect`

## Step 6: Test the API

You can test the API using curl or Postman:

```bash
# Health check
curl https://YOUR_USERNAME-halimis-lira-counter.hf.space/health

# Detect (you'll need to base64 encode an image)
curl -X POST https://YOUR_USERNAME-halimis-lira-counter.hf.space/detect \
  -H "Content-Type: application/json" \
  -d '{"image": "base64_encoded_image", "conf": 0.25}'
```

## Troubleshooting

### Build Fails
- Check the build logs in your Space
- Ensure `best.pt` is uploaded (it might be large, so use Git LFS if needed)
- Verify all files are in the root directory

### Model File Too Large
If `best.pt` is too large for Git:
1. Use Git LFS (Large File Storage):
   ```bash
   git lfs install
   git lfs track "*.pt"
   git add .gitattributes
   git add best.pt
   git commit -m "Add model with LFS"
   git push
   ```

### API Not Responding
- Check the Space logs
- Verify the Dockerfile is correct
- Make sure port 7860 is exposed

### CORS Issues
- The API already has CORS enabled
- If issues persist, check Hugging Face Space settings

## Alternative: Using Gradio (Easier but less flexible)

If Docker deployment is complex, you can also create a Gradio interface:

1. Create a new Space with **"Gradio"** SDK
2. Use Gradio's API mode
3. This is simpler but less customizable

## Cost

- **Free tier**: Hugging Face Spaces are free for public spaces
- **Hardware**: Free tier includes CPU, upgrade to GPU if needed
- **Limitations**: Free tier has usage limits, but should be fine for personal use

## Updating the Deployment

To update your Space:
1. Make changes to files locally
2. Commit and push to the Space repository
3. Hugging Face will automatically rebuild

```bash
git add .
git commit -m "Update API"
git push
```

Your API will be globally accessible once deployed! 🚀

