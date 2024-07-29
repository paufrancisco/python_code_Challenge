def common_letters(): #function to know the similar letters between two words
    str1 = input("Enter first word: ")
    str2 = input("Enter second word: ")

    #convert them into sets first
    s1 = set(str1)
    s2 = set(str2)

    lst = s1 & s2 #compare the two sets buy using & operator to find the common literals between the two sets


    print(lst)


common_letters() #calling the function