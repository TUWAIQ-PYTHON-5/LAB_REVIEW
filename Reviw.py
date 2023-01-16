def add_word(info:str):
    j=3
    for i in range(len(info)):
     if(info[i])==j:
        j+=1
    print(j)
    return info
print(add_word("sultan mohammad alshahrani".split()))



