#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
__author__ = 'thinkalonely'
__mtime__ = '2018/5/21'
# code is far away from bugs with the god animal protecting
  I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from PIL import Image
import random

mw = 100
ms = 20

toImage = Image.new('RGB', (2000, 2000))

names = []
with open("C:/Users/hoo/desktop/pic.txt", "r") as f:
    for line in f:
        line = line.strip()
        names.append(line)

for y in range(1, 21):
    if y in [1, 7]:
        for x in range(1, 21):
            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                if x in list(range(2, 7)) or x in list(range(9, 14)) or x in list(range(16, 20)):
                    toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass
    elif y in [2, 3]:
        for x in range(1, 21):
            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                if x in [2, 13, 16, 19]:
                    toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass
    elif y == 4:
        for x in range(1, 21):
            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                if x not in [1, 7, 8, 14, 15, 17, 18, 20]:
                    toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass
    elif y in [5, 6]:
        for x in range(1, 21):
            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                if x in [6, 9, 16, 19]:
                    toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass

for x in range(1, 21):
    if x in [2, 4, 6, 11, 17]:
        for y in range(13, 18):

            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass
    if x in [3, 5, 12, 18]:
        y = 13
        try:
            fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
            fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
            toImage.paste(fromImage, ((x - 1) * mw, y * mw))
        except IOError:
            pass
    if x in [10, 16]:
        for y in (13, 17):
            try:
                fromImage = Image.open("C:/Users/hoo/Pictures/%s" % random.sample(names, 1)[0])
                fromImage = fromImage.resize((100, 100), Image.ANTIALIAS)
                toImage.paste(fromImage, ((x - 1) * mw, y * mw))
            except IOError:
                pass
toImage.show()
toImage.save('C:/Users/hoo/Desktop/ta.jpg')
