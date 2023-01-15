# LAB_REVIEW
## Write a function that takes a string as a parameter:
- first should seperate words using split by space (if there is any).
- then, it should return the number of words in that string.

Example: 'fine, Thank you' --> 3



def string_function(my_string:str )->str:
    print(string_function.split())
    splited_string = my_string.split()
    words_number = len(splited_string)
    return words_number

print(string_function("Hello world This Is Just a Test"))
