import math
def squares(a,b):
    start = math.ceil(math.sqrt(a))
    end = math.floor(math.sqrt(b))
    count = 0
    for i in range(start,end+1):
        count += 1

    return count

print(squares(17,24))
