def spliting(text):
    #from line 3 to line 15 can be replaced with wordList = text.split()
    wordList=[]
    wordList2=[]
    word=""
    for letters in text:
        if letters == " ":
            wordList2.insert(1,word)
            wordList.extend(wordList2)
            wordList2=[]
            word=""
        else:
            word += letters
    wordList2.insert(1,word)
    wordList.extend(wordList2)
    numberOfWords = len(wordList)
    return numberOfWords

print(spliting("fine, Thank you"))