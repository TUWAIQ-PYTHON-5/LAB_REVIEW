def word_count(phrase:str)->int:
    words = phrase.split(" ")
    total_words=len(words)
    return total_words


print(word_count("fine, thank you"))