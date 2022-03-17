import math


def ip_to_int32(ip):
    # Without bitwise operators
    bits = []
    for n in ip.split('.'):
        bit = ''
        intN = int(n)
        while len(bit) < 8:
            r = intN % 2
            bit = str(r) + bit
            intN = intN // 2
        bits.append(bit)
    res, i = 0, 0
    while i < 32:
        res += int(bits[i // 8][i % 8]) * math.pow(2, (31 - i))
        i += 1
    return res


print(ip_to_int32('128.32.10.1'))
