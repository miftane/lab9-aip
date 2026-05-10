# 9.2.py
from PIL import Image

image_path = "image.jpg"
img = Image.open(image_path)

new_size = (img.width // 3, img.height // 3)
small_img = img.resize(new_size)
small_img.save("small.jpg")
print("Сохранено уменьшенное изображение: small.jpg")

horizontal_flip = img.transpose(Image.FLIP_LEFT_RIGHT)
horizontal_flip.save("horizontal_flip.jpg")
print("Сохранено горизонтальное зеркало: horizontal_flip.jpg")

vertical_flip = img.transpose(Image.FLIP_TOP_BOTTOM)
vertical_flip.save("vertical_flip.jpg")
print("Сохранено вертикальное зеркало: vertical_flip.jpg")
