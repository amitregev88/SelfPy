def mult_tuple(tuple1, tuple2):
    
    list_of_pairs = []

    for i in tuple1:
            
        for j in tuple2:
            list_of_pairs.append((i,j))
            list_of_pairs.append((j,i))

    return tuple(list_of_pairs)

    


def main():

    print(mult_tuple((1, 2),(3, 4)))



if __name__ == "__main__":
    
    main()




def mult_tuple(tuple1, tuple2):
    """Builds all possible couples of the given 2 tuples
    :params: tuple1, tuple2: input touples
    :return: tuple contains all the couples. Order not mandatory
    :rtype: tuple
    """
    calc = tuple([(t1, t2) for t1 in tuple1 for t2 in tuple2])
    return calc + tuple([p[::-1] for p in calc])


