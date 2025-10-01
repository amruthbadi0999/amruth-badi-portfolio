# 🌟 Amruth Badi - Personal Portfolio Website

![Python 3.8+](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white&style=for-the-badge)
![Flask 3.0.0](https://img.shields.io/badge/Flask-3.0.0-000000?logo=flask&logoColor=white&style=for-the-badge)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white&style=for-the-badge)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white&style=for-the-badge)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black&style=for-the-badge)

### 🚀 Live Website
[![Netlify](https://img.shields.io/badge/Deployed%20on-Netlify-00C7B7?logo=netlify&logoColor=white&style=for-the-badge)](https://your-portfolio-url.netlify.app)

## 📋 About

A modern, responsive personal portfolio website showcasing the professional journey, skills, projects, and achievements of **Amruth Badi** - a passionate BCA student and aspiring Full Stack Developer from KLE Society's PC Jabin Science College, Dharwad.

## ✨ Features

### 🎨 **Design & UI/UX**
- 🌑 **Permanent Dark Theme** - Sleek black aesthetic with gradient accents
- 📱 **Fully Responsive Design** - Optimized for all devices and screen sizes
- 🎭 **Smooth Animations** - Engaging hover effects and transitions
- 🎯 **Modern Layout** - Clean, professional design with intuitive navigation

### 🏠 **Homepage Sections**
- 👋 **Hero Section** - Dynamic introduction with tagline "Building ideas into reality ✨"
- 👤 **About Me** - Professional background and current status
- 🛠️ **Skills Showcase** - Interactive skill cards with progress bars
- 🏆 **Awards & Achievements** - 6 achievement cards with hover effects
- 📍 **Location Map** - Embedded Google Maps of college location
- 🎮 **Interactive Mini-Programs** - Quiz, Typing Test, Tic-Tac-Toe, Login System

### 📄 **Additional Pages**
- 📋 **Resume Page** - Comprehensive professional resume with animations
- 🛠️ **Services Page** - Areas of expertise and service offerings
- 📞 **Contact Page** - Professional contact form with validation
- 🎯 **Interactive Games** - Multiple mini-applications for engagement

### 🚀 **Technical Features**
- ⬆️ **Back to Top Button** - Smooth scroll functionality
- 🧭 **Quick Navigation** - Consistent navigation across all pages
- 📧 **Contact Form** - Functional form with Flask backend
- 🎨 **Gradient Styling** - Professional color schemes throughout
- 📱 **Mobile Optimization** - Touch-friendly interface

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.8+ installed:

```bash
python --version
# or
python3 --version
```

### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/amruthbadi0999/BADI0999.git
cd BADI0999
```

2. **Create a virtual environment:**

```bash
python -m venv venv
# or
python3 -m venv venv
```

3. **Activate the virtual environment:**

**Windows:**
```bash
venv\Scripts\activate
```

**macOS/Linux:**
```bash
source venv/bin/activate
```

4. **Install dependencies:**

```bash
pip install -r requirements.txt
```

5. **Run the application:**

```bash
python app.py
# or
python3 app.py
```

6. **Open your browser and visit:**
```
http://127.0.0.1:5000
```

## 🛠️ Technologies & Stack

### **Backend**
- **Flask 3.0.0** - Python web framework
- **Werkzeug 3.0.1** - WSGI utility library
- **Python 3.8+** - Core programming language

### **Frontend**
- **HTML5** - Semantic markup structure
- **CSS3** - Advanced styling with animations
- **JavaScript (ES6+)** - Interactive functionality
- **Ion Icons** - Modern icon library

### **Deployment**
- **Netlify/Vercel** - Serverless deployment platforms
- **Git** - Version control system

## 📁 Project Structure

```plaintext
BADI0999/
├── app.py                    # Flask application entry point
├── requirements.txt          # Python dependencies
├── vercel.json              # Vercel deployment config
├── netlify.toml             # Netlify deployment config
├── _redirects               # Netlify redirects
├── README.md                # Project documentation
├── DEPLOYMENT.md            # Deployment guide
├── PROJECT_SUMMARY.md       # Project overview
├── LICENSE                  # MIT license
├── submissions.txt          # Form submissions storage
├── static/                  # Static assets
│   ├── assets/
│   │   ├── css/            # Stylesheets
│   │   ├── js/             # JavaScript files
│   │   └── images/         # Image assets
│   └── favicon.svg         # Website favicon
└── templates/              # HTML templates
    ├── index.html          # Homepage (main portfolio)
    ├── Resume.html         # Professional resume page
    ├── Services.html       # Services and expertise
    ├── Contact.html        # Contact form page
    ├── thank-you.html      # Form submission confirmation
    ├── quiz.html           # Interactive quiz game
    ├── typing-test.html    # Typing speed test
    ├── tic-tac-toe.html    # Tic-tac-toe game
    ├── password-generator.html # Password generator
    ├── bgcolorchangeJS.html    # Background changer
    └── loginJS.html        # Login system demo
```

## 🎯 Key Features Implementation

### **Responsive Design**
- Mobile-first approach with CSS Grid and Flexbox
- Breakpoint optimization for tablets and desktops
- Touch-friendly interface elements

### **Interactive Elements**
- Smooth scroll navigation between sections
- Animated skill progress bars
- Hover effects on cards and buttons
- Form validation and submission handling

### **Performance Optimization**
- Optimized images and assets
- Efficient CSS animations
- Minimal JavaScript for fast loading
- Clean, semantic HTML structure

### **Professional Sections**
- **Skills**: Frontend (85%), Backend (70%), Leadership (95%), Hardware (75%)
- **Awards**: 6 achievement cards with image placeholders
- **Contact**: Professional contact form with validation
- **Games**: Interactive mini-applications for engagement

## 🎮 Interactive Mini-Programs

1. **📝 Quiz Application** - Knowledge testing with multiple choice questions
2. **⌨️ Typing Test** - Speed and accuracy measurement tool
3. **🎯 Tic-Tac-Toe** - Classic game implementation
4. **🔐 Login System** - User authentication demo

## 📧 Contact Form Features

- **Real-time Validation** - Client-side form validation
- **Professional Design** - Matches overall website aesthetic
- **Backend Processing** - Flask-powered form handling
- **Submission Storage** - Form data saved to submissions.txt
- **Thank You Page** - Confirmation after successful submission

## 🚀 Deployment

### Netlify Deployment (Recommended)

**Prerequisites:**
- GitHub account
- Netlify account

**Steps:**
1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Deploy to Netlify"
   git push origin main
   ```

2. **Deploy on Netlify:**
   - Go to [netlify.com](https://netlify.com)
   - Click "New site from Git"
   - Connect your GitHub repository: `https://github.com/amruthbadi0999/BADI0999`
   - Netlify will auto-detect settings from `netlify.toml`
   - Click "Deploy site"

3. **Custom Domain (Optional):**
   - In Netlify dashboard, go to "Domain settings"
   - Add your custom domain
   - Configure DNS settings

**Current Live Site:** [https://badis-portfolio.netlify.app/](https://badis-portfolio.netlify.app/)

### Local Development
```bash
# Clone the repository
git clone https://github.com/amruthbadi0999/BADI0999.git
cd BADI0999

# Install dependencies
pip install -r requirements.txt

# Run locally (for testing)
cd netlify/functions
python app.py
```

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md).heme**: Professional black aesthetic with gradient accents
- **Minimalism**: Clean, uncluttered design focusing on content
- **Accessibility**: High contrast ratios and semantic HTML
- **Performance**: Optimized for fast loading and smooth interactions
- **Responsiveness**: Seamless experience across all devices

- **Lighthouse Score**: 95+ (Performance, Accessibility, Best Practices, SEO)
- **Mobile Friendly**: 100% responsive design
- **Load Time**: < 2 seconds on average connection
- **Cross-browser**: Compatible with all modern browsers

## 🤝 Contributing

Feel free to fork this project and customize it for your needs. If you find any bugs or have suggestions:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📄 License

This project is open-source and available under the [MIT License](./LICENSE).

## 👨‍💻 About the Developer

**Amruth Badi** - BCA Student & Aspiring Full Stack Developer

- 🎓 **Education**: KLE Society's PC Jabin Science College, Dharwad
- 🏆 **Leadership**: Rotaract Club President (2025-26)
- 🌍 **Experience**: Inter District Youth Exchange Host
- 📧 **Email**: appleamruthbadi@gmail.com
- 📱 **Phone**: +91 9480939288
- 📍 **Location**: Dharwad, Karnataka, India

### 🔗 Connect with Me

- 📧 [Email](mailto:appleamruthbadi@gmail.com)
- 📱 [WhatsApp](https://wa.me/919480939288)
- 📘 [Facebook](https://www.facebook.com/amrut.n.badi)
- 📸 [Instagram](https://www.instagram.com/amruth.badii_10/)
- 💼 [LinkedIn](https://www.linkedin.com/in/amruth-badi/)
- 💻 [GitHub](https://github.com/amruthbadi0999)

---

## 🌐 Live Demo

**🚀 Portfolio Website**: [https://badis-portfolio.netlify.app/](https://badis-portfolio.netlify.app/)

**🚀 Status**: Open to Work Opportunities

Built with 💖 and ☕ by [Amruth Badi](https://github.com/amruthbadi0999)
