#!/usr/bin/env python3
# usage: python3 base256.py text

import sys
from PIL import Image, ImageDraw

encodingBit = 8  # 2^8 = 256
pixelWidth = 10
pixelHeight = 100


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


if __name__ == '__main__':
    print('Base' + str(2**encodingBit))
    source = sys.argv[1]
    print(source)
    encoded = encode(source)
    createImage(encoded)
    decoded = decode(encoded)
    print('復元テスト: ' + decoded)
