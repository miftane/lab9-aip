# 9.4.py
import os
from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_path, output_path, text="© My Watermark"):
    img = Image.open(input_path).convert("RGBA")
    
    txt = Image.new('RGBA', img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(txt)
    
    try:
        font = ImageFont.truetype("arial.ttf", 36)
    except:
        font = ImageFont.load_default()
    
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    position = (img.width - text_width - 10, img.height - text_height - 10)
    
    draw.text(position, text, fill=(255, 255, 255, 128), font=font)
    
    watermarked = Image.alpha_composite(img, txt)
    watermarked = watermarked.convert("RGB")
    watermarked.save(output_path)
    print(f"Водяной знак добавлен: {output_path}")

for i in range(1, 6):
    filename = f"{i}.jpg"
    if os.path.exists(filename):
        add_watermark(filename, f"watermarked_{i}.jpg")
