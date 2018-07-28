# sends 500 (by default) frames to the NDS and saves stats in file,
# can be visualized by running python stats_graphs.py
import ctypes
import os
import socket
import struct
import time
from subprocess import call

import PIL
import numpy
from PIL import Image
from PIL import Image

# How it works:
# NDS opens port 8080, python script connects PC to it, then:
#   python makes screenshot,
#   resizes it to 256px or 128px (depends how smooth transmition you want - 256px takes ~ 0.6s on frame, 128px - ~0.3s)
#   calls grit to make a 16 bit raw binary version
#   sends image size to the NDS
#   sends image
#   receives ACK character from NDS
#   repeat

# Fast screen capture method thanks to:
# https://stackoverflow.com/a/16141058

# does not need to be same value as in DS program - if NDS expects 256 but receives 128 the image will be
# printed 2 times and a bit distorted
base_width = 128
nintendo_ip = "10.42.0.251"
nintendo_port = 8080
buff_size = 65536
LibName = 'prtscn.so'

nds_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
nds_client.connect((nintendo_ip, nintendo_port))

packet_times = []
decompress_times = []
screenshot_times = []
max_packets = 500


def grab_screen(x1, y1, x2, y2):
    w, h = x2 - x1, y2 - y1
    size = w * h
    objlength = size * 3

    grab.getScreen.argtypes = []
    result = (ctypes.c_ubyte * objlength)()

    grab.getScreen(x1, y1, w, h, result)
    return Image.frombuffer('RGB', (w, h), result, 'raw', 'RGB', 0, 1)


while max_packets > 0:

    max_packets -= 1

    # capture screen
    timestamp_total = time.time()
    AbsLibPath = os.path.dirname(os.path.abspath(__file__)) + os.path.sep + LibName
    grab = ctypes.CDLL(AbsLibPath)
    im = grab_screen(0, 0, 1440, 900)
    # resize it
    w_percent = (base_width / float(im.size[0]))
    h_size = int((float(im.size[1]) * float(w_percent)))
    im = im.resize((base_width, h_size), PIL.Image.ANTIALIAS)
    im.save("resized_image.bmp")
    timestamp_grit = time.time()
    # call grit to make it raw, lz77 compressed binary that NDS can understand
    call(["grit", "resized_image.bmp"])
    print("Grit time C: " + str(time.time() - timestamp_grit))
    time_screenshot = time.time() - timestamp_total
    screenshot_times.append(time_screenshot)
    print("Time of generating file (C-lib method): " + str(time_screenshot))
    # read size and send it
    fUploadFile = open("resized_image.img.bin", "rb")
    size = os.path.getsize("resized_image.img.bin")
    print("Size: " + str(size))

    # https://docs.python.org/2/library/struct.html
    # <H is little endian unsigned short
    val = struct.pack('<H', size)
    nds_client.send(val)
    nds_client.recv(1)  # ack

    # send file
    sRead = fUploadFile.read(buff_size)
    timestamp = time.time()
    while sRead:
        nds_client.send(sRead)
        sRead = fUploadFile.read(buff_size)
    print("Sending Completed, time: " + str(time.time() - timestamp))
    ack = time.time()
    # read ack
    nds_client.recv(1)  # ack
    decompress_time = time.time() - ack
    print("Ack time: " + str(decompress_time))
    total_time = time.time() - timestamp_total
    print("Total time: " + str(total_time))
    packet_times.append(total_time)
    decompress_times.append(decompress_time)

numpy.savetxt("packet_times", packet_times, fmt='%1.5f')
numpy.savetxt("decompress_times", decompress_times, fmt='%1.5f')
numpy.savetxt("screenshot_times", screenshot_times, fmt='%1.5f')
