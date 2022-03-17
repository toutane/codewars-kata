def revrot(string, sz):
    l = len(string)
    if sz <= 0 or l == 0 or sz > l:
        return ''
    chunks = []
    i = 0
    while i < l:
        j = 0
        c = ''
        while i < l and j < sz:
            c += string[i]
            i += 1
            j += 1
        if j == sz:
            chunks.append(c)
    res = ''
    for c in chunks:
        sum3 = 0
        for d in c:
            sum3 += pow(int(d), 3)
        if sum3 % 2 == 0:
            for k in range(sz - 1, -1, -1):
                res += c[k]
        else:
            for k in range(1, sz):
                res += c[k]
            res += c[0]
    return res


print(revrot('66443875', 4))
