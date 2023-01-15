# LAB_REVIEW
## Write a function that takes a string as a parameter:
#- first should seperate words using split by space (if there is any).
#- then, it should return the number of words in that string.

def splitString(sentence : str):
    words = len(sentence.split())
    return words


numberOfWords = splitString("fine, Thank you")
print("Number of words is " + str(numberOfWords))




