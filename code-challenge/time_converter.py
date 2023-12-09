def twenty_four_hour(input_hour, input_minute, period): # Takes the inputted hour, minute and period
    if period == "am" and input_hour == 12:
        input_hour = 0 #If the period is "am" and the hour is 12 then the input hour should be reassigned the value 0
    elif period == "pm" and input_hour != 12:
        input_hour += 12 #If the period is "pm" and the hour is NOT 12 then we should add 12 to the hour and reassign the value to input_hour
    
    #Have the new hours and minutes be strings because of concatenation
    new_hour = str(input_hour)
    new_minute = str(input_minute)
    
    if input_hour < 10:
        new_hour = "0" + new_hour
    # Prepending a 0 to the new hour string to ever hour below 10
    if input_minute < 10:
        new_minute = "0" + new_minute
    # Prepending a 0 to the new minute string to ever minute below 10
    return new_hour + new_minute
print(twenty_four_hour(1, 12, "am"))