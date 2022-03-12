def count_Kprimes(k, start, end):
    res = []
    if start == 0:
        start += 1
    for n in range(start, end + 1):
        fac = 0
        t = n
        while t % 2 == 0:
            t = t // 2
            fac += 1
        i = 3
        while (i * i) <= n:
            while t % i == 0:
                t = t // i
                fac += 1
            i += 2
        if n % t == 0 and t != 1:
            fac += 1
        # print(n, ':', t, fac, sep=' ')
        if fac == k:
            res.append(n)
    return res


# print(count_Kprimes(5, 500, 600))
# print(count_Kprimes(2, 0, 100))


def puzzle(s):
    res = 0
    oneP = count_Kprimes(1, 2, s)
    treeP = count_Kprimes(3, 8, s)
    sevenP = count_Kprimes(7, 128, s)
    l3 = len(sevenP)
    for i in oneP:
        for j in treeP:
            k = 0
            while k < l3 and i + j + sevenP[k] <= s:
                if i + j + sevenP[k] == s:
                    res += 1
                k += 1
    return res

# print(puzzle(143))
