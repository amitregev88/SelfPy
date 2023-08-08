num = input("Enter three digits (each digit for one pig):")

number = (int)(num)
sum = ((number//100) + ((number%100) // 10) + (number % 10))
print("",sum,"\n" ,number//3, "\n", number % 3,  "\n", number%3 == 0)
