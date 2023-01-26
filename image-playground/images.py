# import PIL
from PIL import Image, ImageFilter
img = Image.open('E:\python_ztm\image-playground\pokedex\pikachu.jpg')
# filtered_img = img.filter(ImageFilter.SMOOTH)
# filtered_img.save("smooth.png", "png")
filterimg = img.convert('L')
# filterimg.rotate(180)
# filterimg.resize((300, 300))
# filterimg.crop((100, 200, 200, 100 ))
filterimg.show()
