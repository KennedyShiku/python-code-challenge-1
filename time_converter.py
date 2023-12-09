def twenty_four_hour(input_hour, input_minute, period):
    if period == "am" and input_hour == 12:
        input_hour = 0
    elif period == "pm" and input_hour != 12:
        input_hour += 12
    
    new_hour = str(input_hour)
    new_minute = str(input_minute)
    
    if input_hour < 10:
        new_hour = "0" + new_hour
    if input_minute < 10:
        new_minute = "0" + new_minute
    
    return new_hour + new_minute
print(twenty_four_hour(1, 12, "am"))