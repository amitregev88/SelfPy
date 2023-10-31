def sort_prices(list_of_tuples):
    ''' Sort tuples of ('item', price) from from higher to lower price
        :param arg1: list of tuple items (;item name', item_price)
        :rtype arg1:  list of tuples (str, float)
    '''
    return sorted(list_of_tuples, reverse = True, key=get_item_price)


def get_item_price(item):
    return item[1]


def main():

    products = [('milk', '5.5'), ('candy', '2.5'), ('bread', '9.0')]
    l = sort_prices(products)
    print(l)
    

if __name__ == "__main__":
    main()


    # def sort_prices(list_of_tuples):
    # """Sorts items according to their price, from higher to lower.
    # :param: list_of_tuples: the input list, each tuple contains an item and its
    # price
    # :param: list of tuples. price is double
    # :return: sorted list
    # :rtype: list of tuples.
    # """

    # list_of_tuples.sort(key=lambda x: x[1])
    # list_of_tuples.reverse()
    # return list_of_tuples
