def print_list(shopping_list_str):
    print(shopping_list_str)

def print_nums_of_items(shopping_list_str):
    print (shopping_list_str.count(",") + 1)

def is_in_the_list(shopping_list_str):
    product_checked = input("enter a product name:\n")

    if product_checked in shopping_list_str:
        print(True) 
    
    else:
        print(False)

def count_how_much_product_in_the_list(shopping_list_str):

    product_checked = input("enter a product name:\n")

    print(shopping_list_str.count(product_checked))

def remove_product_from_the_list(shopping_list_str):

    to_remove = input("Which product to remove?\n")

    output_str = shopping_list_str.replace(to_remove, "",1)

    # incase the element to remove is first in the list
    if output_str[0] == ',':
        output_str =  output_str[1::]

    # incase the element to remove is last in the list
    elif output_str[-1] == ',':
        output_str =  output_str[0:-1:]

    # incase the element to remove is middle in the list
    else:
        output_str =  output_str.replace(",,",",")


    return output_str


def add_product_to_the_list(shopping_list_str):

    to_add = input("Which product to add?\n")

    return shopping_list_str + to_add

# def print_invalid_product(shopping_list_str):


# def Removing_duplicates_in_list(shopping_list_str)
    



def menu():

    shopping_list_str = input("what to buy?\n")
    
    while (True):

        print("""\n\n\n
            1. Printing the list of products
            2. Printing the number of products in the list
            3. Is the product on the list? (enter a product name)
            4. How many times does a certain product appear? (enter a product name)
            5. remove a product from the list (enter a product name to remove)
            6. Adding a product to the list (enter a product name to add)
            7. Printing all invalid products (a product is invalid if its length is less than 3 or it contains characters other than letters)
            8. Removing all existing duplicates in the list
            9. Exit
            """)


        selection_num = input("please enter a number\n")

        selection_num = int(selection_num) 
        
        if selection_num == 1:
            print_list(shopping_list_str)

        elif selection_num == 2:
            print_nums_of_items(shopping_list_str)

        elif selection_num == 3:
            is_in_the_list(shopping_list_str)

        elif selection_num == 4:
            count_how_much_product_in_the_list(shopping_list_str)

        elif selection_num == 5:

            shopping_list_str = remove_product_from_the_list(shopping_list_str)

        elif selection_num == 6:
            shopping_list_str = add_product_to_the_list(shopping_list_str)

        elif selection_num == 7:

            print("TODO")

        elif selection_num == 8:

            print("TODO")


        elif selection_num == 9:

            return None

        else:

            print("Invalid selection\n")


def main():

    menu()


if __name__ == "__main__":
    main()