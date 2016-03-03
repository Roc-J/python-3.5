from PIL import Image,ImageFilter

#打开一个jpg图像文件，注意是当前路径
im = Image.open('thumbnail.jpg')

#获得尺寸大小
w,h=im.size
print('Original image size : %sx%s' %(w,h))

im.thumbnail((w*2,h*2))
print('Resize image to :%sx%s' %(w*2,h*2))

im2 = im.filter(ImageFilter.BLUR)
im2.save('thumbnail.jpg','jpeg')
