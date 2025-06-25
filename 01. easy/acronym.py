def acronym(sentence: str) -> str:
    sentences = sentence.split(" ") # [Organização, das, Nações, Unidas]
    acronym = ""
    for word in sentences:
        if word[0].isupper():
            acronym += word[0]
    return acronym

my_sentence =  input("Insert one sentence to get an acronym: ") # Organização das Nações Unidas
print(acronym(my_sentence))