def stringName(name :str) -> int:
    new_list = name.split(" ")
    print(new_list)
     
    numberOfWord : int = len(new_list)

    return numberOfWord    


print(stringName("fine, Thank you"))