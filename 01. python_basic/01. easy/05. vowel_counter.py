def vowel_counter(word: str) -> int:
    total_vowel = word.count('a') + word.count('e') + word.count('i') + word.count('o') + word.count('u')
    return total_vowel

my_word = input('Enter one word: ')
print(f"Your word has {vowel_counter(my_word)} vowel/s")