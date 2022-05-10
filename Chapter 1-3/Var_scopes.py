

calculation_to_units = 24
name_of_unit = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units}  {name_of_unit}")
    print(custom_message)


def scope_check(num_of_days):
    my_var = "my variable inside a function"
    print(name_of_unit) #pulling a global variable into a local function
    print(num_of_days)
    print(my_var)

scope_check(20)




