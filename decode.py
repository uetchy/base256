import sys
from PIL import Image
import numpy as np


def decode(indexMap):
    return bytes(indexMap).decode('utf8')


def decodeImage(image, stride=30):
    data = np.array(image)
    row = list(data[0, :, 0])  # 0, :, 0 for red pixels
    indexMap = [row[x] for x in range(0, len(row), stride)]
    print(indexMap)
    return decode(indexMap)


if __name__ == '__main__':
    source = sys.argv[1]
    stride = int(sys.argv[2])
    data = decodeImage(Image.open(source), stride)
    print(data)