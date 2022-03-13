def thirt(n):
    res = n
    seq = [1, 10, 9, 12, 3, 4, 1]
    i = 0
    changed = True
    while res > 0 and changed:
        lRes = res
        nRes = 0
        i = 0
        while res > 0:
            nRes += seq[i % 6] * (res % 10)
            res = res // 10
            i += 1
        changed = lRes != nRes
        res = nRes
        print(res)
    return res


print(thirt(85299258))
