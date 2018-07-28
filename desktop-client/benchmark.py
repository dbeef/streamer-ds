import ctypes
import os
import time
from subprocess import call

import PIL
from PIL import Image
from PIL import Image

base_width = 256

###########################################################

timestamp_total = time.time()
call(["xwd", "-root", "-silent", "-out", "resized_image.xwd"])
call(["mogrify", "-format", "bmp", "-resize", "256", "resized_image.xwd"])
call(["grit", "resized_image.bmp"])
print("Time of generating file using mogrify: " + str(time.time() - timestamp_total))

###########################################################

timestamp_total = time.time()
call(["xwd", "-root", "-silent", "-out", "resized_image.xwd"])
call(["mogrify", "-format", "bmp", "resized_image.xwd"])
img = Image.open("resized_image.bmp")
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), PIL.Image.ANTIALIAS)
img.save("resized_image.bmp")
call(["grit", "resized_image.bmp"])
print("Time of generating file in python: " + str(time.time() - timestamp_total))

###########################################################

timestamp_total = time.time()
call(["gnome-screenshot", "-f", "input.bmp"])
img = Image.open("input.bmp")
wpercent = (base_width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((base_width, hsize), PIL.Image.ANTIALIAS)
img.save("resized_image.bmp")
call(["grit", "resized_image.bmp"])
print("Time of generating file using gnome-screenshot: " + str(time.time() - timestamp_total))

###########################################################

LibName = 'prtscn.so'
AbsLibPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + LibName
grab = ctypes.CDLL(AbsLibPath)


def grab_screen(x1, y1, x2, y2):
    w, h = x2 - x1, y2 - y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte * objlength)()

    grab.getScreen(x1, y1, w, h, result)
    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)


if __name__ == '__main__':
    timestamp_total = time.time()
    im = grab_screen(0, 0, 1440, 900)
    wpercent = (base_width / float(im.size[0]))
    hsize = int((float(im.size[1]) * float(wpercent)))
    im = im.resize((base_width, hsize), PIL.Image.ANTIALIAS)
    im.save("resized_image.bmp")
    timestamp_grit = time.time()
    call(["grit", "resized_image.bmp"])
    print("Grit time: " + str(time.time() - timestamp_grit))
    print("Time of generating file with C lib: " + str(time.time() - timestamp_total))

