def distance(num1, num2, num3):

    if (abs(num1 - num2) == 1 or abs(num1 - num3) == 1):

        if (abs(num2 - num1) > 1 and abs(num2 - num3) > 1):

            return True

        elif (abs(num3 - num1) > 1 and abs(num3 - num2) > 1):

            return True
        
    return False