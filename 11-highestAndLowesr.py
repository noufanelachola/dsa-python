def high_and_low(numbers):
    
    number_str = numbers.split()
    number_int = list(map(int,number_str))
    high = max(number_int)
    low = min(number_int)
    return f"{high} {low}"

print(high_and_low("1 2 -3 4 5"))