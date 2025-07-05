word = input("Insert one word: ").lower()

# If the word has accents or other symbols, this might not work, but I'm disregarding that for now.
if word == word[::-1]:
    print(f"The word {word} is a palindrome")
else:
    print(f"The word {word} isn't a palindrome")