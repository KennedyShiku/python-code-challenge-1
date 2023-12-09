def twenty_four_hour(input_hour, input_minute, period):
    if period == "am" and input_hour == 12:
        input_hour = 0
    elif period == "pm" and input_hour != 12:
        input_hour += 12
    
    new_hour = str(input_hour)
    new_minute = str(input_minute)
    
    if new_hour < 10:
        new_hour = "0" + new_hour
    if new_minute < 10:
        new_minute = "0" + new_minute
    
    # return input_hour
print(twenty_four_hour(1, "pm"))