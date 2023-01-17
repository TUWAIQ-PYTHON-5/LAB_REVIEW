def string_function(my_string:str )->str:
    splited_string = my_string.split()
    print(splited_string)
    words_number = len(splited_string)
    return words_number
print(string_function("Hello world This Is Just a Test."))

