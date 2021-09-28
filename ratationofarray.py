import numpy as np


def rotaLeft(a, d):
    return a[d:] + a[:d]


if __name__ == '__main__':
    result = rotaLeft([1,2,3,4,5],2)
    print(result)