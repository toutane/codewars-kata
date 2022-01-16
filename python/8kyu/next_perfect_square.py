import math

def find_next_square(sq):
    sqrt = math.sqrt(sq)
    if sqrt == 0 or sqrt == (sq // sqrt) :
        return (sqrt + 1) * (sqrt + 1)
    else:
        return -1

print(find_next_square(121));
print(find_next_square(114)); 