# 8kyu - Reversed Strings
def solution(string):
    rev = ""
    for c in string:
        rev = c + rev
    return rev

print(solution('world'))