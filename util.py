def printable_percent(num):
    return "{:.2%}".format(num)

def v_in(var):
    if var == "":
        return False
    elif var.isnumeric() == True:
        return True
    else:
        return False