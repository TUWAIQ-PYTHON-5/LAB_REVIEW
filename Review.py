# LAB_REVIEW
## Write a function that takes a string as a parameter:
#- first should seperate words using split by space (if there is any).
#- then, it should return the number of words in that string.

#Example: 'fine, Thank you' --> 3
'''
def wordCount(phrase : str) ->int:
    words = phrase.split(" ")
    totalWords = len(words)
    return totalWords
















'''
def splitFunction (txtToSeprate : str) -> str:
    cleanText:str=""
    counter1:int=0
    counter2:int=0
    arrow:str=" --> "
    for char in txtToSeprate: # (counter2,txtToSeprate,1):
        if  (char != " "):
            cleanText += char
            counter1 + 1
            #print(char)
            
        else:
            cleanText += ' '
            counter2 +=1
                #rerun : str = (' '+char.lower())
                #return rerun
                #if (islower(rewright)
        #Testprint(cleanText)
    
    outPut : str = cleanText + arrow 
    outPut : str = cleanText + arrow + str(counter2)
    return outPut
    #return counter2

usrTxt:str=input("Enter Your Text:\n") #\n for the newline
print(splitFunction(usrTxt))














'''

txt = "welcome to the jungle"

x = txt.split()

print(x)


def splitFunction (txtToSeprate : str) -> str:
    for word in txtToSeprate:
        if (word == True):
            rerun: str = (char + '')
        return rerun
                #print("Test")
    else:

        rerun : str = (' '+char.lower())
        return rerun
            #if (islower(rewright)'''