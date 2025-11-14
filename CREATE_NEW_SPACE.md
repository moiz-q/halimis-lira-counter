# Create New Docker Space - Quick Guide

## Step 1: Create New Space

1. Go to: https://huggingface.co/new-space

2. Fill in:
   - **Owner**: moizncai
   - **Space name**: `halimis-lira-counter-app` (or delete old one and reuse the name)
   - **License**: MIT
   - **Select SDK**: **Docker** ⬅️ IMPORTANT!
   - **Space hardware**: CPU basic - 2 vCPU - 16GB (free)
   - **Visibility**: Public

3. Click **"Create Space"**

## Step 2: Push Your Code

Once created, you'll get a new URL. Then run:

```bash
cd hf-complete-deploy

# Remove old remote
git remote remove origin

# Add new remote (replace with your new Space URL)
git remote add origin https://huggingface.co/spaces/moizncai/halimis-lira-counter-app

# Push to new Space
git push origin main --force
```

## Step 3: Wait for Build

The Space will automatically build and deploy!

Your new app URL will be:
**https://moizncai-halimis-lira-counter-app.hf.space**

---

## Alternative: Delete and Reuse Old Name

If you want to keep the same name:

1. Go to old Space settings: https://huggingface.co/spaces/moizncai/halimis-lira-counter/settings
2. Scroll to bottom → Click **"Delete this space"**
3. Confirm deletion
4. Create new Space with **same name** but **Docker SDK**
5. Push code as above

This way you keep the same URL!

