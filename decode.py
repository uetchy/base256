"""
Decode script
"""
import sys
from PIL import Image
import numpy as np


def decode(index_map):
  """
  Decode string
  """
  return bytes(index_map).decode('utf8')


def decode_image(image, stride=30):
  """
  Decode image
  """
  data = np.array(image)
  row = list(data[0, :, 0])  # 0, :, 0 for red pixels
  index_map = [row[x] for x in range(0, len(row), stride)]
  print(index_map)
  return decode(index_map)


if __name__ == '__main__':
  SOURCE = sys.argv[1]
  STRIDE = int(sys.argv[2])
  DATA = decode_image(Image.open(SOURCE), STRIDE)
  print(DATA)
