# Deploy to Custom Domain: lira.amqdev.com

You have several options to host your app on your custom domain. Here are the best approaches:

---

## Option 1: Vercel (Recommended - Easiest & Free)

**Pros:** Free, easy setup, automatic HTTPS, custom domains, fast CDN

### Steps:

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy the web build:**
   ```bash
   cd hf-complete-deploy/web
   vercel
   ```
   - Follow prompts (use defaults)
   - This creates a Vercel project

3. **Add custom domain:**
   - Go to: https://vercel.com/dashboard
   - Click your project → Settings → Domains
   - Add: `lira.amqdev.com`

4. **Update DNS in GoDaddy:**
   - Go to GoDaddy DNS settings for `amqdev.com`
   - Add CNAME record:
     - **Name:** `lira`
     - **Value:** `cname.vercel-dns.com`
     - **TTL:** 1 hour

5. **Update API URL in app:**
   - Keep API on Hugging Face
   - Or deploy backend to Vercel too (see below)

**Time:** ~10 minutes  
**Cost:** Free

---

## Option 2: Netlify (Also Free & Easy)

**Pros:** Free, drag-and-drop deploy, custom domains

### Steps:

1. **Install Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Deploy:**
   ```bash
   cd hf-complete-deploy/web
   netlify deploy --prod
   ```

3. **Add custom domain:**
   - Go to: https://app.netlify.com
   - Site settings → Domain management
   - Add custom domain: `lira.amqdev.com`

4. **Update DNS:**
   - Netlify will show you the DNS records to add
   - Add CNAME in GoDaddy pointing to Netlify

**Time:** ~10 minutes  
**Cost:** Free

---

## Option 3: Cloudflare Pages (Free, Fast CDN)

**Pros:** Free, global CDN, easy custom domains

### Steps:

1. **Push to GitHub** (if not already):
   ```bash
   git add .
   git commit -m "Add web build"
   git push
   ```

2. **Connect to Cloudflare Pages:**
   - Go to: https://dash.cloudflare.com
   - Pages → Create a project
   - Connect GitHub repo
   - Build settings:
     - **Build command:** (leave empty, already built)
     - **Build output directory:** `hf-complete-deploy/web`

3. **Add custom domain:**
   - Pages → Your project → Custom domains
   - Add: `lira.amqdev.com`

4. **Update DNS:**
   - Cloudflare will auto-configure if you use their nameservers
   - Or add CNAME in GoDaddy

**Time:** ~15 minutes  
**Cost:** Free

---

## Option 4: Keep Everything on Hugging Face + Reverse Proxy

**Pros:** Everything stays on HF, just add domain

### Steps:

1. **Check if HF Pro supports custom domains:**
   - Hugging Face Pro might support custom domains
   - Check: https://huggingface.co/pricing

2. **Or use Cloudflare as reverse proxy:**
   - Add domain to Cloudflare
   - Create Page Rule:
     - URL: `lira.amqdev.com/*`
     - Forward to: `https://moizncai-halimis-lira-counter-app.hf.space`
   - This masks the HF URL

**Time:** ~5 minutes  
**Cost:** Free (Cloudflare) or HF Pro cost

---

## Option 5: Deploy Full Stack to Vercel (Frontend + Backend)

**Pros:** Everything in one place, custom domain, free tier

### Steps:

1. **Create `vercel.json` in project root:**
   ```json
   {
     "version": 2,
     "builds": [
       {
         "src": "hf-complete-deploy/web/**",
         "use": "@vercel/static"
       },
       {
         "src": "hf-complete-deploy/app.py",
         "use": "@vercel/python"
       }
     ],
     "routes": [
       {
         "src": "/detect",
         "dest": "hf-complete-deploy/app.py"
       },
       {
         "src": "/(.*)",
         "dest": "hf-complete-deploy/web/$1"
       }
     ]
   }
   ```

2. **Deploy:**
   ```bash
   vercel
   ```

3. **Add custom domain** (same as Option 1)

**Note:** Vercel's Python runtime might need adjustments for YOLO model. May need to use serverless functions differently.

---

## Recommended Approach

**For simplicity:** Use **Option 1 (Vercel)** for frontend, keep API on Hugging Face

**For everything together:** Use **Option 3 (Cloudflare Pages)** with reverse proxy to HF API

---

## Quick Setup (Vercel - Recommended)

```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Deploy frontend
cd hf-complete-deploy/web
vercel

# 3. Add domain in Vercel dashboard
# 4. Update DNS in GoDaddy (CNAME: lira -> cname.vercel-dns.com)
# 5. Update API_URL in App.js to point to HF API
```

---

## Update API URL After Domain Setup

Once you have `lira.amqdev.com` working, you can:

1. **Keep API on HF** (easiest):
   - Update `API_URL` in `App.js` to: `''` (relative) or HF URL
   - Frontend on your domain, API calls go to HF

2. **Or deploy API to subdomain**:
   - Use `api.amqdev.com` for backend
   - Update `API_URL` to: `https://api.amqdev.com`

---

## DNS Configuration in GoDaddy

1. Log in to GoDaddy
2. Go to DNS Management for `amqdev.com`
3. Add CNAME record:
   - **Type:** CNAME
   - **Name:** `lira`
   - **Value:** (provided by hosting service)
   - **TTL:** 1 hour
4. Save and wait 5-30 minutes for propagation

---

## Which Should You Choose?

- **Want easiest?** → Vercel (Option 1)
- **Want free + fast?** → Cloudflare Pages (Option 3)
- **Want drag-and-drop?** → Netlify (Option 2)
- **Want everything on HF?** → Check HF Pro custom domains

**My recommendation:** Start with **Vercel** - it's the easiest and works great!

---

Let me know which option you prefer and I'll help you set it up step by step! 🚀

