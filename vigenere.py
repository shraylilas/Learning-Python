# So I was doing one of the CS50x exercises. There I found myself making a Caesar cipher in C
# I'm not the biggest cryptology nerd but I like looking at ciphers
# Naturally, let's make a Vigenere cipher in Python, as a quick exercise (Why not in C, you ask? Because the syntax is not really in my head right now)

corpus = input("Enter corpus: ")
keyword = input("Enter keyword: ")
ciphertext = ""
key_index = 0
for i in corpus:
    if i.isalpha() is True:
        key = keyword[key_index % len(keyword)]
        if i.isupper() is True:
            i = chr(((ord(i) - ord('A') + ord(key.upper()) - ord('A')) % 26) + ord('A'))
            ciphertext += i
        elif i.islower() is True:
            i = chr(((ord(i) - ord('a') + ord(key.lower()) - ord('a')) % 26) + ord('a'))
            ciphertext += i
        key_index += 1
    else:
        ciphertext += i
print(ciphertext)