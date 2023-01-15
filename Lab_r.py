# LAB_REVIEW
## Write a function that takes a string as a parameter:

#3- first should seperate words using split by space (if there is any).
#- then, it should return the number of words in that string.

# Example: 'fine, Thank you' --> 3

def function (st : str ):   
    x = st.split()
    print(x)
    words = len(st.split())
    return words

print("Number of words:",function('fine, Thank you'))


