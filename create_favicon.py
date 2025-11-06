#!/usr/bin/env python3
"""
Script to create a properly sized square favicon from KK.png
This will prevent the squishing issue by creating a square version
with the original logo centered on a transparent background.
"""

try:
    from PIL import Image, ImageDraw
    import os
    
    def create_square_favicon():
        # Load the original image
        original_path = "assets/images/KK.png"
        if not os.path.exists(original_path):
            print(f"Error: {original_path} not found")
            return
            
        # Load original image
        img = Image.open(original_path)
        print(f"Original image size: {img.size}")
        
        # Create different sized square favicons
        sizes = [16, 32, 48, 64, 128, 256, 512]
        
        for size in sizes:
            # Create a square transparent background
            square_img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
            
            # Calculate scaling to fit the logo within the square while maintaining aspect ratio
            img_aspect = img.width / img.height
            if img_aspect > 1:  # Landscape (wider than tall)
                # Scale based on width, add padding top/bottom
                new_width = int(size * 0.8)  # Leave 10% margin on each side
                new_height = int(new_width / img_aspect)
            else:  # Portrait or square
                # Scale based on height, add padding left/right
                new_height = int(size * 0.8)
                new_width = int(new_height * img_aspect)
            
            # Resize the original image
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Calculate position to center the image
            x = (size - new_width) // 2
            y = (size - new_height) // 2
            
            # Paste the resized image onto the square background
            square_img.paste(resized_img, (x, y), resized_img if resized_img.mode == 'RGBA' else None)
            
            # Save the favicon
            favicon_path = f"assets/images/KK_favicon_{size}.png"
            square_img.save(favicon_path, "PNG")
            print(f"Created {favicon_path}")
        
        # Create a main favicon.ico file (multi-size)
        favicon_ico_path = "assets/images/favicon.ico"
        # For the .ico, we'll use the 32x32 version
        square_32 = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
        img_32 = img.resize((26, int(26 / img_aspect)), Image.Resampling.LANCZOS)
        x_32 = (32 - 26) // 2
        y_32 = (32 - int(26 / img_aspect)) // 2
        square_32.paste(img_32, (x_32, y_32), img_32 if img_32.mode == 'RGBA' else None)
        square_32.save(favicon_ico_path, "ICO")
        print(f"Created {favicon_ico_path}")
        
        print("\nFavicon creation complete!")
        print("\nTo use these new favicons, update your HTML files to reference:")
        print("- assets/images/KK_favicon_16.png for 16x16")
        print("- assets/images/KK_favicon_32.png for 32x32") 
        print("- assets/images/KK_favicon_48.png for 48x48")
        print("- assets/images/favicon.ico for the main favicon")
        
    if __name__ == "__main__":
        create_square_favicon()
        
except ImportError:
    print("Pillow (PIL) library not found.")
    print("Install it with: pip install Pillow")
    print("\nAlternatively, you can:")
    print("1. Use an online favicon generator like favicon.io")
    print("2. Upload your KK.png file")
    print("3. Download the generated square favicon files")
    print("4. Replace the current favicon references in your HTML files")
