def func(num1, num2):
    '''
    this function calculates the multiplication of 2 numbers.
    :parm num1: The first number of the multiplication operation.
    :type num1 float
    :parm num2: The second number of the multiplication operation.
    :type num2 float
    :return The result of multiplication operation between two numbers.
    rtype: flaot 
    '''
    return num1 * num2

def main():
    # Call the function func
    res = func(1.5, 1.5)

    #print(func.__doc__)           
    #help(func)

    print(res)
if __name__ == "__main__":
    main()



