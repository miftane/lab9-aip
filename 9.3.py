# 9.3.py
import os
from PIL import Image, ImageFilter

# Создаем папку для результатов
output_dir = "filtered_images"
os.makedirs(output_dir, exist_ok=True)

for i in range(1, 6):
    filename = f"{i}.jpg"
    if os.path.exists(filename):
        img = Image.open(filename)
        filtered_img = img.filter(ImageFilter.CONTOUR)
        output_path = os.path.join(output_dir, f"filtered_{i}.jpg")
        filtered_img.save(output_path)
        print(f"Обработан файл: {filename}")
    else:
        print(f"Файл {filename} не найден")
