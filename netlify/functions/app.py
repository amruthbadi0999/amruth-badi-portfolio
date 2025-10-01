from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os
import serverless_wsgi

# Initialize the Flask app
app = Flask(__name__, 
           template_folder='../../templates',
           static_folder='../../static')

# Main routes
@app.route('/')
def home():
    """Serve the homepage"""
    return render_template('index.html')

@app.route('/Contact.html')
def contact():
    """Serve the contact page"""
    return render_template('Contact.html')

@app.route('/Resume.html')
def resume():
    """Serve the resume page"""
    return render_template('Resume.html')

@app.route('/Services.html')
def services():
    """Serve the services page"""
    return render_template('Services.html')

@app.route('/thank-you')
def thank_you():
    """Show thank-you message after form submission"""
    return render_template('thank-you.html')

# Interactive mini-programs routes
@app.route('/quiz')
def quiz():
    """Interactive quiz application"""
    return render_template('quiz.html')

@app.route('/typing-test')
def typing_test():
    """Typing speed test application"""
    return render_template('typing-test.html')

@app.route('/tic-tac-toe.html')
def tic_tac_toe():
    """Tic-tac-toe game"""
    return render_template('tic-tac-toe.html')

@app.route('/password-generator.html')
def password_generator():
    """Password generator tool"""
    return render_template('password-generator.html')

@app.route('/bgcolorchangeJS.html')
def background_changer():
    """Background color changer demo"""
    return render_template('bgcolorchangeJS.html')

@app.route('/login')
def login():
    """Login system demo"""
    return render_template('loginJS.html')

# Form handling
@app.route('/submit-form', methods=['POST'])
def submit_form():
    """Handle contact form submission"""
    try:
        # Extract form data
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        phone = request.form.get('phone', '')
        website = request.form.get('website', '')
        message = request.form.get('message', '')
        
        # Validate required fields
        if not name or not email or not message:
            return "Missing required fields", 400
        
        # Save form data with timestamp
        submission_data = f"""
--- {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---
Name: {name}
Email: {email}
Phone: {phone}
Website: {website}
Message: {message}
"""
        
        # For serverless, we'll just return success (file writing may not work)
        # In production, you'd want to use a database or external service
        return redirect(url_for('thank_you'))
    
    except Exception as e:
        return f"Error processing form: {str(e)}", 500

# Error handlers
@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return render_template('index.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """Handle 500 errors"""
    return "Internal server error", 500

# Netlify serverless function handler
def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)

if __name__ == '__main__':
    # For local development
    app.run(debug=True, host='0.0.0.0', port=8000)
