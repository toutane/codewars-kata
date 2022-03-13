def kebabize(string):
    res = ''
    while string[0] == '-' or not(str.isalpha(string[0])):
        if len(string) != 1:
            string = string[1:len(string)]
        else:
            return ''
    if str.isupper(string[0]):
        res = str.lower(string[0])
        string = string[1:len(string)]
    for c in string:
        if str.isupper(c):
            res += '-' + str.lower(c)
        elif str.isalpha(c) or c == '-':
            res += c
    return res
    # could be:
    # return ''.join(c if c.islower() else '-' + c.lower() for c in s if c.isalpha()).strip('-')
    # but less clever


# print(kebabize('camelsHave3Humps'))
print(kebabize('1233'))
