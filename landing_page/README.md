# Gemini Desktop Landing Page

Professional landing page for the Gemini Desktop app with modern design and smooth animations.

## Features

- 🎨 **Beautiful Design**: Modern gradient hero section with animated background
- 📱 **Responsive**: Optimized for desktop, tablet, and mobile devices
- ⚡ **Fast**: Lightweight CSS and JavaScript with smooth animations
- 🔗 **Direct Links**: Download DMG and GitHub repository links
- 📸 **Screenshot Ready**: Placeholder sections for app screenshots
- 🌐 **SEO Optimized**: Proper meta tags and semantic HTML

## Quick Preview

```bash
# Serve locally for testing
python3 serve.py
# Opens http://localhost:8000 in your browser
```

## Structure

```
landing_page/
├── index.html          # Main landing page
├── serve.py           # Local development server
└── README.md          # This file
```

## Sections

1. **Hero Section**: Eye-catching introduction with download buttons
2. **Features**: Detailed feature grid with icons and descriptions
3. **Screenshots**: Gallery section (ready for real screenshots)
4. **Download**: Prominent download section with options
5. **Footer**: Links and credits

## Customization

### Colors
The design uses a consistent color scheme:
- Primary: `#667eea` to `#764ba2` (purple-blue gradient)
- Secondary: `#2c3e50` to `#3498db` (dark blue gradient)
- Accent: `#ff6b6b`, `#4ecdc4`, `#45b7d1`, `#96ceb4` (rainbow gradient)

### Fonts
- System fonts: `-apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto'`
- Ensures native look on all platforms

### Animations
- Fade-in animations on scroll
- Hover effects on buttons and cards
- Parallax hero background
- Smooth transitions throughout

## Adding Screenshots

Replace the placeholder sections in the screenshots grid:

```html
<!-- Replace this -->
<div class="screenshot-placeholder">
    Main Interface
</div>

<!-- With this -->
<img src="path/to/screenshot.png" alt="Main Interface">
```

## Deployment Options

### GitHub Pages
1. Add landing page to your repository
2. Enable GitHub Pages in repository settings
3. Set source to main branch `/landing_page` folder

### Netlify
1. Drag and drop the `landing_page` folder to Netlify
2. Or connect to your GitHub repository

### Custom Domain
Update the download links to point to your GitHub releases:
```html
<a href="https://github.com/yourusername/gemini-desktop/releases/latest/download/Gemini_Desktop.dmg">
```

## Browser Support

- ✅ Safari 12+
- ✅ Chrome 70+
- ✅ Firefox 65+
- ✅ Edge 79+

## Performance

- 📊 Lighthouse Score: 95+ (Performance, Accessibility, Best Practices)
- 📱 Mobile Friendly: Fully responsive design
- 🚀 Fast Loading: Minimal dependencies, optimized CSS/JS