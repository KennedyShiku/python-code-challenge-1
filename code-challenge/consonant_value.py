def highest_consonant_value(input_string):
    highest_value = 0
    current_value = 0

    def consonant_value(consonant):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        lower_case_consonant = consonant.lower()

        if lower_case_consonant not in alphabet:
            return 0
        
        return alphabet.index(lower_case_consonant) + 1
    
    found = False
    for letter in input_string:
        if letter.lower() == 'a' or letter.lower() == 'e' or letter.lower() == 'i' or letter.lower() == 'o' or letter.lower() == 'u':
            current_value = 0
        else:
            current_value += consonant_value(letter)
            if current_value > highest_value:
                highest_value = current_value
    return highest_value
print(highest_consonant_value("kennedy"))