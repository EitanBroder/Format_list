def format_list(my_list):
    """The function accepts a string of double-length strings.
     The function returns a string containing the list organs in the spousal positions,
      separated by commas and spaces, as well as the last limb with the caption "and" before it."""
    two=(my_list[::2])
    x=", ".join(two)
    last=(my_list[-1::])
    y='and'.join(last)


    print (x+' and '+y)

format_list(["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium"])

