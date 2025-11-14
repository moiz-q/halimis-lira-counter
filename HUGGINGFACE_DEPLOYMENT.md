# Deploying to Hugging Face Spaces

This guide will help you deploy the Halimi's Lira Counter API to Hugging Face Spaces so it can be accessed globally.

## Prerequisites

1. A Hugging Face account (sign up at https://huggingface.co)
2. Git installed on your computer
3. The code is already on GitHub: https://github.com/moiz-q/halimis-lira-counter

## Step 1: Prepare Files

1. Copy the files from `huggingface_space/` directory:
   - `app.py`
   - `requirements.txt`
   - `README.md`
   - `Dockerfile`
   - `best.pt` (your YOLO model)

## Step 2: Create a Hugging Face Space

✅ **Space already created!**
- **Space URL**: https://huggingface.co/spaces/moizncai/halimis-lira-counter
- **Username**: moizncai

## Step 3: Upload Files

### Option A: Using Git from GitHub (Recommended)

1. **Clone the GitHub repository:**
   ```bash
   git clone https://github.com/moiz-q/halimis-lira-counter.git
   cd halimis-lira-counter
   ```

2. **Clone your Hugging Face Space repository:**
   ```bash
   git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
   cd halimis-lira-counter
   ```

3. **Copy files from GitHub repo:**
   ```bash
   # Copy from the huggingface_space directory
   cp ../halimis-lira-counter/huggingface_space/* .
   cp ../halimis-lira-counter/best.pt .
   ```

4. **Commit and push:**
   ```bash
   git add .
   git commit -m "Initial deployment from GitHub"
   git push
   ```

### Option A2: Direct Clone from GitHub

Alternatively, you can clone directly from GitHub and copy files:

```bash
# Clone GitHub repo
git clone https://github.com/moiz-q/halimis-lira-counter.git
cd halimis-lira-counter

# Clone HF Space
cd ..
git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
cd halimis-lira-counter

# Copy files
cp ../halimis-lira-counter/huggingface_space/* .
cp ../halimis-lira-counter/best.pt .

# Push to HF
git add .
git commit -m "Deploy from GitHub"
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
- Once built, your API will be live at: `https://moizncai-halimis-lira-counter.hf.space`

## Step 5: Update Mobile App

1. Open `mobile-app/App.js`
2. Update the `API_URL`:
   ```javascript
   const API_URL = 'https://moizncai-halimis-lira-counter.hf.space';
   ```

3. The API endpoints will be:
   - Health: `https://moizncai-halimis-lira-counter.hf.space/health`
   - Detect: `https://moizncai-halimis-lira-counter.hf.space/detect`

## Step 6: Test the API

You can test the API using curl or Postman:

```bash
# Health check
curl https://moizncai-halimis-lira-counter.hf.space/health

# Detect (you'll need to base64 encode an image)
curl -X POST https://moizncai-halimis-lira-counter.hf.space/detect \
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

