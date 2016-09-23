# -*- coding: utf-8 -*-
# 2016/9/22 16:18
"""
-------------------------------------------------------------------------------
Function:   test your pytesser3
Version:    1.0
Author:     SLY
Contact:    slysly759@gmail.com 
 
-------------------------------------------------------------------------------
"""

from pytesser3 import image_to_string
from PIL import Image
import requests
def get_code():
        url = 'http://www.rongtudai.com/validimg.html'
        f=requests.get(url)
        print(f)
        with open("code.jpg", "wb") as code:
            code.write(f.content)
        img = Image.open('code.jpg')
        img = img.convert("RGBA")
        pixdata = img.load()
        for y in range(img.size[1]):
             for x in range(img.size[0]):
                if pixdata[x, y][0] < 90:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][1] < 136:
                    pixdata[x, y] = (0, 0, 0, 255)
        for y in range(img.size[1]):
            for x in range(img.size[0]):
                if pixdata[x, y][2] > 0:
                    pixdata[x, y] = (255, 255, 255, 255)
        img.save('newcode.jpg')
        img = Image.open('newcode.jpg')
        vcode =image_to_string(img)
        return vcode
print(get_code())