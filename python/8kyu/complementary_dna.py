# 7kyu - Complementary DNA

def DNA_strand(dna):
    result = ""
    for c in dna:
        if c == "A":
            result += "T"
        elif c == "T":
            result += "A"
        elif c == "C":
            result += "G"
        else:
            result += "C"
    return result