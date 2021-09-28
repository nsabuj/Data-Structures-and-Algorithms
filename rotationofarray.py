import numpy as np


def rotaLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    result = rotaLeft(['a','b','c','d','e'],2)
    print(result)