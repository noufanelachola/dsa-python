def solve(n, m):
    num = 0
    power = 1
    
    for i in range(n):
        num = (num + power) % m
        power = (power * 10) % m

    return num

solve(3,3)