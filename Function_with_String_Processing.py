def getInitial_with_Options(name, force_uppercase=True):
    if force_uppercase:
        intial = name[0:1].upper()
    else:
        intial = name[0:1]
    
    return intial

def getInitial(name):
    # intial = name[0:1].upper()
    # return intial
    """
    Invoke the function with DEFAULT value defined in the function
    """
    return getInitial_with_Options(name)

first_name = input("Please Enter Your First Name:")
first_name_initial = getInitial(first_name)

last_name = input("Please Enter Your Last Name:")
last_name_initial = getInitial(last_name)


"""
2 ways to use the funtion
"""
print(f"you Initials are: {first_name_initial + last_name_initial}")
print()
print(f"you Initials are: {getInitial(first_name) + getInitial(last_name)}")
print()
print(f"you Initials are: {getInitial(first_name) + getInitial_with_Options(last_name, False)}")

"""
You can use paramater name to make the code more readable when passing bunch of parameters
once you name the paramater, the sequence of parameters is not necessary anymore
"""
last_name_initial = getInitial_with_Options(force_uppercase = True, name=last_name)
print()
print(f"you Initials are: {getInitial(first_name) + last_name_initial}")