#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# @Time : 11/27/2018 17:07
# @Author : mingfei.net@gmail.com
# @FileName : pillow_test.py
# @GitHub : https://github.com/thu/Python-Demo-B

from PIL import Image, ImageFilter, ImageDraw, ImageFont

image = Image.open('test.jpg')

# width, height = image.size
#
# print(width, height)
#
# image.thumbnail((width // 10, height // 10))
#
# image.save('thumbnail.jpg')
#
# image = Image.open('test.jpg')
#
# blur = image.filter(ImageFilter.GaussianBlur(radius=10))
#
# blur.save('blur.jpg')

draw = ImageDraw.Draw(image)

# use a bitmap font
# font = ImageFont.load("arial.pil")

# draw.text((10, 10), "hello", font=font)

# use a truetype font
font = ImageFont.truetype("arial.ttf", 150)

draw.text((10, 25), "world", font=font)

image.save('string.jpg')
