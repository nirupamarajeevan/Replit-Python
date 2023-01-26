from PIL import Image
img = Image.open('E:\python_ztm\image-playground\photo.png')
img.thumbnail((400, 400))
img.save('profile.png')
print(img.size)