from PIL import Image
# import sys
# args = sys.argv
# print(args)

im = Image.open('jiyin.jpg')
#print(im.format, im.size, im.mode)
im.thumbnail((200, 100))
im.save('thumb.jpg', 'JPEG')