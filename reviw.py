#Write a function that takes a string as a parameter:

   # first should seperate words using split by space (if there is any).
   #then, it should return the number of words in that string.
#
#Example: 'fine, Thank you' --> 3

'''
def wordCount(word):

    count=1
    for i in word:
        if i == " ":
            count=count+1
    return count
print(wordCount("fine, Thank you"))
'''

def wordCount(word):
    
    res = ""
    List = []
    word = word + " "
    for i in word:
        if i != " ":
            res += i
        else:   
            List.append(res)
            res = ""
    result = len(List)
    return result
     
word = "fine, Thank you"
print(wordCount(word))