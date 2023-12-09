def twenty_four_hour(input_hour, period):
    if period == "am" and input_hour == 12:
        input_hour = 0
    elif period == "pm" and input_hour != 12:
        input_hour += 12
    return input_hour
print(twenty_four_hour(1, "pm"))