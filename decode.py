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


def detect_stride(vec):
    return len([x for x in vec if x == vec[0]])


def decode_image(image):
    """
    Decode image
    """
    image = image.convert('RGB')
    data = np.array(image)
    row = list(data[0, :, 0])  # 0, :, 0 for red pixels
    stride = detect_stride(row)
    index_map = [row[x] for x in range(0, len(row), stride)]
    return decode(index_map)


if __name__ == '__main__':
    SOURCE = sys.argv[1]
    DATA = decode_image(Image.open(SOURCE))
    print(DATA)
