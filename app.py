from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

# Initialize the Flask app
app = Flask(__name__)

# Route to serve the homepage (index.html)
@app.route('/')
def home():
    return render_template('index.html')


# Dynamic route to serve other HTML pages (like Contact.html, Resume.html, etc.)
@app.route('/<page>')
def route_page(page):
    try:
        return render_template(page)
    except:
        return "Page not found", 404


# Route to handle form submission from Contact.html
@app.route('/submit-form', methods=['POST'])
def submit_form():
    # Extract data from the form fields using 'name' attributes
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')
    website = request.form.get('website', '')
    message = request.form['message']

    # Save the form data into a text file with a timestamp
    with open('submissions.txt', 'a') as f:
        f.write(f"\n--- {datetime.now()} ---\n")
        f.write(f"Name: {name}\n")
        f.write(f"Email: {email}\n")
        f.write(f"Phone: {phone}\n")
        f.write(f"Website: {website}\n")
        f.write(f"Message: {message}\n")
    # Redirect to a thank-you route after submission
    return redirect(url_for('thank_you'))


# Route to show a thank-you message after form submission
@app.route('/thank-you')
def thank_you():
    return render_template('thank-you.html')


# Routes for interactive mini-programs
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/typing-test')
def typing_test():
    return render_template('typing-test.html')

@app.route('/tic-tac-toe.html')
def tic_tac_toe():
    return render_template('tic-tac-toe.html')

@app.route('/password-generator.html')
def password_generator():
    return render_template('password-generator.html')

@app.route('/bgcolorchangeJS.html')
def background_changer():
    return render_template('bgcolorchangeJS.html')

@app.route('/login')
def login():
    return render_template('loginJS.html')

if __name__ == '__main__':
    app.run(debug=True)
