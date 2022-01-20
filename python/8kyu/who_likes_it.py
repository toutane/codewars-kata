# 6kyu - Who likes it ?

def likes(names):
    l = len(names)
    start = ""
    if l == 0:
        start = "no one likes"
    elif l == 1:
        start = str(names[0]) + " likes"
    elif l == 2:
        start = str(names[0]) + ' and ' + str(names[1]) + ' like'
    elif l == 3:
        start = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(names[2]) + ' like'
    else:
        start = str(names[0]) + ', ' + str(names[1]) + ' and ' + str(l - 2) + ' others' + ' like'
    return start + " this"

print(likes(["Alex", "Jacob", "Mark", "Max"]))