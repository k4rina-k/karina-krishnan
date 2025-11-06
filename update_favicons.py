#!/usr/bin/env python3
"""
Script to update all HTML files with the new square favicon references
"""

import os
import re

def update_favicon_references():
    # Define the replacement mappings
    replacements = [
        (r'href="assets/images/KK\.png\?v=4"', 'href="assets/images/KK_favicon_16.png"', 'sizes="16x16"'),
        (r'href="assets/images/KK\.png\?v=4"', 'href="assets/images/KK_favicon_32.png"', 'sizes="32x32"'),
        (r'href="assets/images/KK\.png\?v=4"', 'href="assets/images/KK_favicon_48.png"', 'sizes="48x48"'),
    ]
    
    # Find all HTML files
    html_files = []
    for file in os.listdir('.'):
        if file.endswith('.html') and file != 'index':  # Skip 'index' since we already updated it
            html_files.append(file)
    
    for html_file in html_files:
        print(f"Updating {html_file}...")
        
        with open(html_file, 'r') as f:
            content = f.read()
        
        # Update each size specifically
        # 16x16
        content = re.sub(
            r'<link rel="icon" type="image/png" sizes="16x16" href="assets/images/KK\.png\?v=4">',
            '<link rel="icon" type="image/png" sizes="16x16" href="assets/images/KK_favicon_16.png">',
            content
        )
        
        # 32x32
        content = re.sub(
            r'<link rel="icon" type="image/png" sizes="32x32" href="assets/images/KK\.png\?v=4">',
            '<link rel="icon" type="image/png" sizes="32x32" href="assets/images/KK_favicon_32.png">',
            content
        )
        
        # 48x48
        content = re.sub(
            r'<link rel="icon" type="image/png" sizes="48x48" href="assets/images/KK\.png\?v=4">',
            '<link rel="icon" type="image/png" sizes="48x48" href="assets/images/KK_favicon_48.png">',
            content
        )
        
        # shortcut icon
        content = re.sub(
            r'<link rel="shortcut icon" href="assets/images/KK\.png\?v=4" type="image/png">',
            '<link rel="shortcut icon" href="assets/images/favicon.ico" type="image/x-icon">',
            content
        )
        
        # apple-touch-icon
        content = re.sub(
            r'<link rel="apple-touch-icon" sizes="180x180" href="assets/images/KK\.png\?v=4">',
            '<link rel="apple-touch-icon" sizes="180x180" href="assets/images/KK_favicon_256.png">',
            content
        )
        
        # Write the updated content back
        with open(html_file, 'w') as f:
            f.write(content)
        
        print(f"✓ Updated {html_file}")
    
    print(f"\nUpdated {len(html_files)} HTML files with new favicon references!")

if __name__ == "__main__":
    update_favicon_references()
