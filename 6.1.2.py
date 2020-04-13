def shift_left(my_list):
    """Take every word to the left"""
    x=my_list[0]
    y=my_list[1:]
    y.append(x)
    return y

print(shift_left([4,6,"izik"]))















