import numpy as np


def generation(seq=''):
    arr = np.array(list(seq))

    for i in range(0, 10):
        buffer = np.array(arr)
        for j in range(-1, len(seq) - 1):
            a = arr[j - 1] == '1'
            b = arr[j] == '1'
            c = arr[j + 1] == '1'
            if (a and b and c) or (a and b and not c) or (a and not b and c) or (not a and not b and not c):
                buffer[j + 1] = '0'
            else:
                buffer[j + 1] = '1'
        arr = np.array(buffer)

    return ''.join(arr)


print(
    generation("1001000101111100000101111001011011101101101111110111110000000000000011000001011001100011111101001001"))