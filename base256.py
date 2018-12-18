#!/usr/bin/env python3
# usage: python3 base256.py text

import sys
import math
from PIL import Image, ImageDraw

encodingBit = 8  # 2^8 = 256
pixelWidth = 10
pixelHeight = 50


def encode(text):
    return [int(x) for x in text.encode('utf8')]


def decode(indexMap):
    return bytes(indexMap).decode('utf8')


def createImage(data, outfile='output.png'):
    img = Image.new('RGB', (len(data) * pixelWidth, pixelHeight), color='black')
    draw = ImageDraw.Draw(img)
    for i, n in enumerate(data):
        draw.rectangle(
            (i * pixelWidth, 0, i * pixelWidth + pixelWidth, pixelHeight),
            fill=(n, 0, 0))
    img.save(outfile)


def createDuplexImage(data, outfile='output.png'):
    rowLength = math.ceil(len(data) / 3)
    img = Image.new('RGB', (rowLength * pixelWidth, pixelHeight), color='black')
    draw = ImageDraw.Draw(img)
    for i, n in enumerate(data):
        rgbIndex = math.floor(i / rowLength)
        rowIndex = i % rowLength
        print(rgbIndex, rowIndex)
        pixel = list(img.getpixel((rowIndex, 0)))
        pixel[rgbIndex] = n
        print(pixel)
        draw.rectangle((rowIndex * pixelWidth, 0,
                        rowIndex * pixelWidth + pixelWidth, pixelHeight),
                       fill=tuple(pixel))
    img.save(outfile)


if __name__ == '__main__':
    print('Base' + str(2**encodingBit))
    source = sys.argv[1]
    print(source)
    encoded = encode(source)
    createImage(encoded)
    decoded = decode(encoded)
    print('復元テスト: ' + decoded)
