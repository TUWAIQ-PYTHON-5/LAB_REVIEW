def spliting(text):
    wordList=[]
    for letters in text:
        word =""
        counter = 0
        if letters == " ":
            wordList.insert(counter,word)
            counter += 1
        else:
            word += letters
    counter += 1
    wordList.insert(counter,word)
    numberOfWords = len(wordList)
    return numberOfWords


x = input()
print(spliting(x))
