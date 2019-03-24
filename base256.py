#!/usr/bin/env python3
"""
usage: python3 base256.py text
"""

import sys
import math
import random
from PIL import Image, ImageDraw

ENCODING_BIT = 8  # 2^8 = 256
PIXEL_WIDTH = 10
PIXEL_HEIGHT = 50


def encode(text):
  """
  Encode to base64
  """

  return [int(x) for x in text.encode('utf8')]


def decode(index_map):
  """
  Decode from base64
  """
  return bytes(index_map).decode('utf8')


def create_image(data, outfile='output.png'):
  """
  Generate and save image
  """
  img = Image.new('RGB', (len(data) * PIXEL_WIDTH, PIXEL_HEIGHT), color='black')
  draw = ImageDraw.Draw(img)
  for i, grad in enumerate(data):
    draw.rectangle((i * PIXEL_WIDTH, 0, i * PIXEL_WIDTH + PIXEL_WIDTH, PIXEL_HEIGHT),
                   fill=(grad, 0, 0))
  img.save(outfile)


def random_filler(_):
  """
  Random Filter
  """
  filler = lambda: math.floor(random.random() * 2) * 125
  return (filler(), filler(), filler())


def yellow_filler(grad):
  """
  Yellow Filter
  """
  return (grad, grad, 0)


def create_square_image(data, outfile='output.png'):
  """
  Generate square image
  """

  image_length = math.ceil(math.sqrt(len(data)))
  pixel_length = 128
  length = image_length * pixel_length

  img = Image.new('RGB', (length, length), color='black')
  draw = ImageDraw.Draw(img)
  for i, grad in enumerate(data):
    row_index = math.floor(i / image_length)
    column_index = i % image_length
    draw.rectangle(
        ((column_index * pixel_length, row_index * pixel_length),
         (column_index * pixel_length + pixel_length, row_index * pixel_length + pixel_length)),
        fill=yellow_filler(grad))
  img.save(outfile)


def create_duplex_image(data, outfile='output.png'):
  """
  Create duplex image
  """

  row_length = math.ceil(len(data) / 3)
  img = Image.new('RGB', (row_length * PIXEL_WIDTH, PIXEL_HEIGHT), color='black')
  draw = ImageDraw.Draw(img)
  for i, grad in enumerate(data):
    rgb_index = math.floor(i / row_length)
    row_index = i % row_length
    print(rgb_index, row_index)
    pixel = list(img.getpixel((row_index, 0)))
    pixel[rgb_index] = grad
    print(pixel)
    draw.rectangle(
        (row_index * PIXEL_WIDTH, 0, row_index * PIXEL_WIDTH + PIXEL_WIDTH, PIXEL_HEIGHT),
        fill=tuple(pixel))
  img.save(outfile)


if __name__ == '__main__':
  print('Base' + str(2**ENCODING_BIT))
  SOURCE = sys.argv[1]
  print(SOURCE)
  with open(SOURCE) as f:
    SOURCE = ''.join(f.readlines())
  ENCODED = encode(SOURCE)
  create_square_image(ENCODED)
  DECODED = decode(ENCODED)
  print('復元テスト: ' + DECODED)
