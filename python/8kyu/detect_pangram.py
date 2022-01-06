# 6kyu - Detect Pangram
def is_present(c, s):
    i = 0
    while i < len(s) and s[i] != c:
        i += 1
    return i < len(s)

def is_pangram(s):
    letters = ""
    for c in s:
        if c.isalpha() and not is_present(c.lower(), letters):
            letters += c.lower()
    return len(letters) == 26

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))