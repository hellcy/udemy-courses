# None

print(type(None))  # NoneType


def searchstring(search):
    # when you can't find anything
    return None


# return None if input parameter is not float or int
def square(number):
    if isinstance(number, float) == False and isinstance(number, int) == False:
        return None
    else:
        return number ** 2
