def setence_reverse(sentence: str) -> str:
    sentence = sentence.split(" ")
    sentence.reverse()
    sentence = " ".join(sentence)
    return sentence

my_setence = input("Insert your sentence: ")
print(setence_reverse(my_setence))