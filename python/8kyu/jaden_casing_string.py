# 7kyu - Jaden Casing Strings
def to_jaden_case(string):
    for i in range(len(string)):
        if i == 0 or string[i - 1] == " ":
            string = string[:i] + string[i].upper() + string[i + 1::]
    return string

print(to_jaden_case("How can mirrors be real if our eyes aren't real"))