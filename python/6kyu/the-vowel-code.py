def encode(st):
    res = ''
    for c in st:
        if c == 'a':
            res += '1'
        elif c == 'e':
            res += '2'
        elif c == 'i':
            res += '3'
        elif c == 'o':
            res += '4'
        elif c == 'u':
            res += '5'
        else:
            res += c
    return res


print(encode('hello'))


def decode(st):
    res = ''
    for c in st:
        if c == '1':
            res += 'a'
        elif c == '2':
            res += 'e'
        elif c == '3':
            res += 'i'
        elif c == '4':
            res += 'o'
        elif c == '5':
            res += 'u'
        else:
            res += c
    return res


print(decode('h2ll4'))
