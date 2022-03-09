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
        if fac == k:
            res.append(n)
    return res


def consec_kprimes(k, arr):
    res = 0
    for i in range(0, len(arr) - 1):
        c, n = arr[i], arr[i + 1]
        if count_Kprimes(k, c, c) != [] and count_Kprimes(k, n, n) != []:
            res += 1
    return res


# print(consec_kprimes(4, [10005, 10030, 10026, 10008, 10016, 10028, 10004]))
