import string


def abbreviate(s):
    ws = []
    i, l = 0, len(s)
    while i < l:
        w = ''
        while i < l and not(s[i] in string.punctuation) and not s[i].isdigit() and s[i] != ' ':
            w += s[i]
            i += 1
        ws.append(w)
        if i < l:
            if (s[i] in string.punctuation) or s[i] == ' ' or s[i].isdigit():
                ws.append(s[i])
        i += 1
    res = ''
    print(ws)
    for w in ws:
        l2 = len(w)
        if l2 > 3:
            res += w[0] + str(l2 - 2) + w[l2 - 1]
        else:
            res += w
    return res


print(abbreviate("is. is-sat-balloon double-barreled5the5double-barreled. the: on: "))
