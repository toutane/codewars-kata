import timeit

def find_position(c):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    i = 0
    while i < 26 and alphabet[i] != c:
        i += 1
    if i < 26:
        return str(i + 1) + " "
    else:
        return ""

def alphabet_position(text):
    res = ""
    for c in text:
        res = res + find_position(c.lower())
    return res[:-1]

# def alphabet_position2(text):
#     return ' '.join(str(ord(c) - 96) for c in text.lower() if c.isalpha())

print(timeit.timeit("alphabet_position('The sunset sets at twelve o clock.')", globals=globals(), number=1000))
# print(timeit.timeit("alphabet_position2('The sunset sets at twelve o clock.')", globals=globals(), number=1000))