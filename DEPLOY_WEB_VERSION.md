# Deploy Complete Web Version on Hugging Face

This guide shows you how to deploy the **complete web application** (frontend + backend) on Hugging Face Spaces using Gradio.

## Why Gradio?

- ✅ **Simpler**: No Docker needed, just Python
- ✅ **Complete**: Frontend + Backend in one file
- ✅ **Beautiful**: Built-in modern UI
- ✅ **Free**: Works on Hugging Face free tier
- ✅ **Global**: Accessible from anywhere via web browser

## Quick Deployment

### Option 1: Use Gradio Version (Recommended)

1. **Go to your Hugging Face Space:**
   https://huggingface.co/spaces/moizncai/halimis-lira-counter

2. **Update the Space settings:**
   - Go to **Settings** → **SDK**
   - Change from **Docker** to **Gradio**
   - Save

3. **Upload files using Git:**

   ```bash
   # Clone your HF Space
   git clone https://huggingface.co/spaces/moizncai/halimis-lira-counter
   cd halimis-lira-counter
   
   # Clone GitHub repo (if not already done)
   git clone https://github.com/moiz-q/halimis-lira-counter.git ../halimis-repo
   
   # Copy Gradio files
   cp ../halimis-repo/huggingface_space/app_gradio.py app.py
   cp ../halimis-repo/huggingface_space/README_GRADIO.md README.md
   cp ../halimis-repo/huggingface_space/requirements.txt .
   cp ../halimis-repo/best.pt .
   
   # Commit and push
   git add .
   git commit -m "Switch to Gradio web interface"
   git push
   ```

4. **Wait for build** (5-10 minutes)

5. **Access your web app:**
   https://moizncai-halimis-lira-counter.hf.space

## What You Get

- 🌐 **Web Interface**: Beautiful UI accessible from any browser
- 📱 **Mobile Friendly**: Works on phones, tablets, and desktops
- 🎨 **Modern Design**: Purple/pink gradient theme matching your mobile app
- ⚡ **Fast**: Direct model inference, no API calls needed
- 🔒 **Secure**: Everything runs on Hugging Face servers

## Files Needed

For Gradio deployment, you only need:
- `app.py` (the Gradio app - rename from `app_gradio.py`)
- `requirements.txt` (with Gradio instead of Flask)
- `README.md` (with Gradio metadata)
- `best.pt` (your YOLO model)

## Comparison

### Current Setup (Docker + Mobile App)
- ✅ Backend on Hugging Face
- ❌ Frontend runs on your device (Expo)
- ❌ Requires mobile app installation

### New Setup (Gradio Web App)
- ✅ Backend on Hugging Face
- ✅ Frontend on Hugging Face
- ✅ Works in any web browser
- ✅ No installation needed
- ✅ Shareable link

## Migration Steps

1. **Keep both versions** (you can have both!)
   - Current Docker API: Still works for mobile app
   - New Gradio app: For web users

2. **Or switch completely:**
   - Update Space to use Gradio
   - Mobile app can still use the API endpoints if you keep Flask running

## Best of Both Worlds

You can actually run **both**:
- Keep `app.py` as Flask API (for mobile app)
- Add `app_gradio.py` as Gradio interface (for web)
- Use Gradio's `launch()` with `share=True` to get a public URL

Or create **two separate Spaces**:
1. API Space: `moizncai/halimis-lira-counter-api` (Docker)
2. Web Space: `moizncai/halimis-lira-counter` (Gradio)

## Testing

Once deployed, test at:
```
https://moizncai-halimis-lira-counter.hf.space
```

Upload an image and click "Detect Cash"!

---

**Recommendation**: Use Gradio for simplicity. It's easier to deploy, maintain, and share! 🚀

