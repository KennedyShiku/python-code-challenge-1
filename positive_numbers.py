def two_positive_numbers(a,b,c):
    positive_numbers = 0

    if a > 0:
        positive_numbers += 1
    if b > 0:
        positive_numbers += 1
    if c > 0:
        positive_numbers += 1
    
    return positive_numbers == 2

print(two_positive_numbers(1, 2, -3))