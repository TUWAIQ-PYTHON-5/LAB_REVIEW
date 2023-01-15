def character (count :str):
    character = count.split(" ")

    num_word = len(character)

    return character,num_word

print(character("fine Thank you"))