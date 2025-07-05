def caesar_cipher(generic_phrase, generic_displacement) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    encrypted_phrase = []
    for letter in generic_phrase:
        if letter.isupper():
            encrypted_phrase.append(alphabet[alphabet.index(letter.lower()) + generic_displacement].upper())
        else: 
            encrypted_phrase.append(alphabet[alphabet.index(letter) + generic_displacement])
    return "".join(encrypted_phrase)

def decrypt_caesar_cipher(generic_phrase, generic_displacement) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    decrypted_phrase = []
    for letter in generic_phrase:
        if letter.isupper():
            decrypted_phrase.append(alphabet[alphabet.index(letter.lower()) - generic_displacement].upper())
        else: 
            decrypted_phrase.append(alphabet[alphabet.index(letter) - generic_displacement])
    return "".join(decrypted_phrase)

my_phrase = list(input("Insert one phrase: ").strip())
my_displacement = int(input("Insert the displacement of caesar cipher: "))

my_encrypted_phrase = caesar_cipher(my_phrase, my_displacement)
print(my_encrypted_phrase)

my_decrypted_phrase = decrypt_caesar_cipher(my_encrypted_phrase, my_displacement)
print(my_decrypted_phrase)

# Or

def encrypt_and_decrypt_caesar_cipher(generic_phrase, generic_displacement, decrypt = False) -> str:
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    new_phrase = []
    if decrypt:
        generic_displacement *= -1
    for letter in generic_phrase:
        if letter.isupper():
            new_phrase.append(alphabet[alphabet.index(letter.lower()) + generic_displacement].upper())
        else: 
            new_phrase.append(alphabet[alphabet.index(letter) + generic_displacement])
    return "".join(new_phrase)

my_phrase02 = list(input("Insert one phrase: ").strip())
my_displacement02 = int(input("Insert the displacement of caesar cipher: "))

my_encrypted_phrase02 = encrypt_and_decrypt_caesar_cipher(my_phrase02, my_displacement02)
print(my_encrypted_phrase02)

my_decrypted_phrase02 = encrypt_and_decrypt_caesar_cipher(my_encrypted_phrase02, my_displacement02, decrypt = True)
print(my_decrypted_phrase02)