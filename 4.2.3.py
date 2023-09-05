temperature_intput  = input("Insert the temperature you would like to convert:")

unit = temperature_intput[-1:-2:-1]

temperature_val = temperature_intput[:-1]

if unit == "c" or unit == "C":
    convert_temperature = ((9 * float(temperature_val) + (32 * 5))) / 5
    print(str(convert_temperature) + "F")

elif unit == "f" or unit == "F":
    convert_temperature = (5 * float(temperature_val) - 160) / 9
    print(str(convert_temperature) + "C")


else: 
    print("invalid temperature intput\n")
    

    """
    source = input("Enter the temperature you would like to convert: ")
if source[-1] == 'f' or source[-1] == 'F':
    print((float(source[:-1]) * 5 - 160) / 9)
if source[-1] == 'c' or source[-1] == 'C':
    print((float(source[:-1]) * 9 + 160) / 5)
    """

