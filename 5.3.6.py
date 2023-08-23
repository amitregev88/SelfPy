def fix_age(age):

    if (age >= 13 and age <= 19) and (age != 15 and age != 16):
        return 0

    else:
        return age


def filter_teens(a = 13, b = 13, c = 13):
    return  fix_age(a) + fix_age(b) + fix_age (c)


    """
    def filter_teens(a=13, b=13, c=13):
    return fix_teen(a) + fix_teen(b) + fix_teen(c)


def fix_teen(n):
    if n in (13, 14, 17, 18, 19):
        return 0
    return n
    """
    