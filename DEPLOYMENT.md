# 🚀 Deployment Guide

## Netlify Deployment (Current Setup)

### Method 1: GitHub Integration (Recommended)

1. **Push to GitHub:**
```bash
git add .
git commit -m "Deploy to Netlify"
git push origin main
```

2. **Connect to Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository
   - Configure build settings:
     - Build command: `pip install -r requirements.txt`
     - Publish directory: `/`
     - Functions directory: `netlify/functions`

3. **Deploy automatically** - Every push triggers deployment

### Method 2: Netlify CLI

1. **Install Netlify CLI:**
```bash
npm install -g netlify-cli
```

2. **Login and deploy:**
```bash
netlify login
netlify deploy --prod
```

## Vercel Deployment (Alternative)

### Method 1: Vercel CLI

1. **Install Vercel CLI:**
```bash
npm i -g vercel
```

2. **Login to Vercel:**
```bash
vercel login
```

3. **Deploy from project directory:**
```bash
vercel
```

4. **Follow the prompts:**
   - Set up and deploy? `Y`
   - Which scope? Select your account
   - Link to existing project? `N`
   - What's your project's name? `portfolio-website`
   - In which directory is your code located? `./`

### Method 2: GitHub Integration

1. **Push to GitHub:**
```bash
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/portfolio-website.git
git push -u origin main
```

2. **Connect to Vercel:**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository
   - Configure build settings (auto-detected)
   - Deploy!

## Environment Variables

No environment variables required for basic deployment.

## Build Configuration

The `vercel.json` file is already configured for Flask deployment:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

## Custom Domain (Optional)

1. **In Vercel Dashboard:**
   - Go to your project
   - Click "Domains"
   - Add your custom domain
   - Follow DNS configuration instructions

## Troubleshooting

### Common Issues:

1. **Build Fails:**
   - Check Python version compatibility
   - Verify requirements.txt is correct
   - Ensure all files are committed

2. **Static Files Not Loading:**
   - Verify file paths in templates
   - Check static folder structure
   - Ensure proper Flask static configuration

3. **Form Submission Issues:**
   - Check form action URLs
   - Verify Flask routes are correct
   - Test locally first

### Support

If you encounter issues:
1. Check Vercel deployment logs
2. Test locally with `python app.py`
3. Verify all dependencies are in requirements.txt
4. Check file permissions and paths
