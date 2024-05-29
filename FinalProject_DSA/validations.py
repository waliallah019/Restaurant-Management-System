
def name_validation(name):
    if not name or name.isspace():
        return False

    for c in name:
        if not c.isalpha() and not c.isspace():
            return False

    return True
def name_validation2(name):
    if not name or name.isspace():
        return False

    for c in name:
        if not c.isalpha() and not c.isspace() and c not in (',', '(', ')','-'):
            return False

    return True



def int_validation(value):
    try:
        int_value = int(value)
        return True
    except ValueError:
        return False

        
def price_validation(price):
    for c in price:
        if not c.isdigit():
            return False
    return True


def int_validation_with_limits(value, lower_limit, upper_limit):
    try:
        int_value = int(value)
        return lower_limit <= int_value <= upper_limit
    except ValueError:
        return False


def double_validation(value):
    try:
        double_value = float(value)
        return True
    except ValueError:
        return False


def double_validation_with_limits(value, lower_limit, upper_limit):
    try:
        double_value = float(value)
        return lower_limit <= double_value <= upper_limit
    except ValueError:
        return False

