def twenty_four_hour(input_hour, input_minute, period):
    if period == "am" and input_hour == 12:
        input_hour = 0
    elif period == "pm" and input_hour != 12:
        input_hour += 12
    
    new_hour = str(input_hour)
    new_minute = str(input_minute)
    
     
    # return input_hour
print(twenty_four_hour(1, "pm"))