# 9.1.py
from PIL import Image


image_path = "image.jpg"

try:
    img = Image.open(image_path)
    print(f"Размер: {img.size} (ширина x высота)")
    print(f"Формат: {img.format}")
    print(f"Цветовая модель: {img.mode}")
    img.show()
except FileNotFoundError:
    print("Файл не найден")
