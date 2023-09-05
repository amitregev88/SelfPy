def chocolate_maker(small, big, x):

    num_of_big = x // 5 
    if num_of_big > big:
        num_of_big = big
    
    rest = x - num_of_big * 5

    if rest <= small:
        return True
    else:
        return False
    
"""
def chocolate_maker(small, big, x):
    if small + (5 * big) < x:
        return False
    if x % 5 > small:
        return False
    return True
"""
