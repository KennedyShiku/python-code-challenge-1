def highest_consonant_value(input_string):
    #Tracking the current and highest values
    highest_value = 0
    current_value = 0

    # Function that calculates the value of a consonant
    def consonant_value(consonant):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        lower_case_consonant = consonant.lower()

        # Return 0 if a value is NOT a consonant
        if lower_case_consonant not in alphabet:
            return 0
        
        # Return the index of the consonant in the alphabet plus 1
        return alphabet.index(lower_case_consonant) + 1
    
    found = False
    # Loop for iterating over each letter in the inputted string
    for letter in input_string:
        # Check if the lowercase letter is a vowel
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            current_value = 0
        else:
            current_value += consonant_value(letter)
            
            # Check if the current value is greater than the highest value
            if current_value > highest_value:
                highest_value = current_value
    # Return the highest calculated value of the substring
    return highest_value
print(highest_consonant_value("kennedy"))