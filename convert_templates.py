#!/usr/bin/env python3
"""
Convert Flask templates to static HTML files for Netlify deployment
"""
import os
import re

def convert_flask_to_static(input_file, output_file):
    """Convert Flask template to static HTML"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace Flask url_for static file references
    content = re.sub(
        r"{{ url_for\('static', filename='([^']+)'\) }}", 
        r'static/\1', 
        content
    )
    
    # Replace Flask template links
    content = re.sub(r'href="/"', 'href="index.html"', content)
    content = re.sub(r'href="/#([^"]+)"', r'href="index.html#\1"', content)
    
    # Fix navigation links
    nav_replacements = {
        'href="Contact.html"': 'href="Contact.html"',
        'href="Resume.html"': 'href="Resume.html"', 
        'href="Services.html"': 'href="Services.html"',
        'action="/thank-you.html"': 'action="thank-you.html"'
    }
    
    for old, new in nav_replacements.items():
        content = content.replace(old, new)
    
    # Write static HTML file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ Converted {input_file} → {output_file}")

def main():
    """Convert all Flask templates to static HTML"""
    templates_dir = "templates"
    
    # Files to convert
    files_to_convert = [
        "index.html",
        "Resume.html", 
        "Services.html"
    ]
    
    for filename in files_to_convert:
        input_path = os.path.join(templates_dir, filename)
        output_path = filename
        
        if os.path.exists(input_path):
            convert_flask_to_static(input_path, output_path)
        else:
            print(f"❌ File not found: {input_path}")
    
    print("\n🎉 Conversion complete! Your site is ready for Netlify deployment.")
    print("\n📋 Next steps:")
    print("1. git add .")
    print("2. git commit -m 'Convert to static HTML for Netlify'")
    print("3. git push")
    print("4. Update Netlify settings: Publish directory = '/' (root)")

if __name__ == "__main__":
    main()
