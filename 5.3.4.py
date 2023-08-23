
def last_early(my_str):
    lowcase_str = my_str.lower()
    last_character = lowcase_str[-1:-2:-1]
    if lowcase_str.find(last_character,0,-1) == -1:
        return False
    else:
        return True
    

    """
    def last_early(my_str):
    x = my_str.upper()
    return x[-1] in x[:-1]
    """