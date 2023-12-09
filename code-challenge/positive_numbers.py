def two_positive_numbers(a,b,c): # Takes in three numbers
    # A counter for the positive numbers which will keep track of our numbers and return positive if is equal to two
    positive_numbers = 0

    #Checking all three numbers to find out if they are positive or negative
    if a > 0:
        positive_numbers += 1
    if b > 0:
        positive_numbers += 1
    if c > 0:
        positive_numbers += 1
    
    #If the positive numbers are 2 then we return true
    return positive_numbers == 2
print(two_positive_numbers(1, 2, -3))   