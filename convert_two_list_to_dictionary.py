def send_to_dictionary():
    list1 = ['Naina', 'Kimi', 'Sheena']
    list2 = [1,2,3]

    result = dict(zip(list1, list2)) #method to merge two different list into one list

    print(result)


send_to_dictionary()

def dict_to_tuple():
    list = {'Naina': 1, 'Kimi': 2, 'Sheena': 3}

    for i in list.items(): #method to make them print into pairs
        print(i)


dict_to_tuple()