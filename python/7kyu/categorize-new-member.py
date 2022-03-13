def open_or_senior(data):
    l = []
    for c in data:
        if c[0] >= 55 and c[1] > 7:
            l.append('Senior')
        else:
            l.append('Open')
    return l
