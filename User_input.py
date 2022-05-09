
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units}  {name_of_unit}")


user_input = input("Hey user, enter a number of days and I will convert it to hours\n") #ask user to enter data--input function
print(user_input)