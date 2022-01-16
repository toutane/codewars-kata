def get_middle(s):
    l = len(s)
    mid = l / 2
    if l % 2 == 1:
        return s[mid]
    else:
        return s[mid - 1:mid]