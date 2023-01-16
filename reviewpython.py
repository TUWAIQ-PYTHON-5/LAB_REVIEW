string1 : str ="How Are You ?"
def myFunction (string1):
    seperate= string1.rsplit(" ")
    return seperate
print (myFunction (string1))
print( len(string1.split()))