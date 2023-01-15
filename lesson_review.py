# LAB_REVIEW
## Write a function that takes a string as a parameter:
#- first should seperate words using split by space (if there is any).
#- then, it should return the number of words in that string.

#Example: 'fine, Thank you' --> 3


def seperate (list_s : str) :
    sp = list_s.split()
    print(sp)
    word = len(list_s.split())
    return word  






print("the number of word is :", seperate("hello my name is nada"))