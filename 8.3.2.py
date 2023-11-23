person = {"first_name" : "Mariah", "last_name": "Carey", "birth_date" : "27.03.1970", "hobbies" : ["Sing", "Compose", "Act"]}

num = input("insert a number between 1-7\n")

if int(num) == 1:
    print(person["last_name"])

elif int(num) == 2:
    print(person["birth_date"][4])

elif int(num) == 3:
    print(len(person["hobbies"]))

elif int(num) == 4:

    print(person["hobbies"][2])

elif int(num) == 5:
    person["hobbies"] += "Cooking"

elif int(num) == 6:
    person["birth_date"] = tuple(map(int,'27.03.1970'.split('.')))
    print(person["birth_date"])

elif int(num) == 7:
    person["age"] = 52
    print(person["age"])



#     mariah = {
#     "first_name": "Mariah",
#     "last_name": "Carey",
#     "birth_date": "27.03.1970",
#     "hobbies": ["Sing", "Compose", "Act"]
# }
# command = int(input("Enter a command: "))
# if command == 1:
#     print(mariah["last_name"])
# if command == 2:
#     print(mariah["birth_date"][3:5])
# if command == 3:
#     print(len(mariah["hobbies"]))
# if command == 4:
#     print(mariah["hobbies"][-1])
# if command == 5:
#     mariah["hobbies"].append("Cooking")
# if command == 6:
#     mariah["birth_date"] = (int(mariah["birth_date"][:2]), int(mariah["birth_date"][3:5]), int(mariah["birth_date"][-4:]))
#     print(mariah["birth_date"])
# if command == 7:
#     mariah['age'] = 2021 - int(mariah["birth_date"][6:])
#     print(mariah["age"])