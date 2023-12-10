from PIL import Image

img = Image.open("downloads/imagen/proyecto sena/algo serio.jpg")
imgGray = img.convert("L")
imgGray.save("test_gray.jpg")