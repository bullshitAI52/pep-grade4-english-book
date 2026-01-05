#!/usr/bin/env python3
import os
from PIL import Image

# Get all image files
image_files = []

# Add the 1-X.webp files first
for i in [1, 2, 3]:
    filename = f"1-{i}.webp"
    if os.path.exists(filename):
        image_files.append(filename)

# Add 四年X.webp files (1 to 87)
for i in range(1, 88):
    filename = f"四年{i}.webp"
    if os.path.exists(filename):
        image_files.append(filename)

print(f"Found {len(image_files)} images to combine")

# Convert all images to RGB mode and store them
images = []
for img_file in image_files:
    print(f"Processing {img_file}...")
    img = Image.open(img_file)
    # Convert RGBA to RGB if needed (PDF doesn't support transparency)
    if img.mode in ('RGBA', 'LA', 'P'):
        rgb_img = Image.new('RGB', img.size, (255, 255, 255))
        if img.mode == 'P':
            img = img.convert('RGBA')
        rgb_img.paste(img, mask=img.split()[-1] if img.mode in ('RGBA', 'LA') else None)
        images.append(rgb_img)
    elif img.mode != 'RGB':
        images.append(img.convert('RGB'))
    else:
        images.append(img)

# Save as PDF
output_file = "四年级英语pep下册.pdf"
if images:
    # Save first image and append the rest
    images[0].save(
        output_file,
        save_all=True,
        append_images=images[1:],
        resolution=100.0,
        quality=95
    )
    print(f"\nSuccessfully created {output_file} with {len(images)} pages")
else:
    print("No images found!")
