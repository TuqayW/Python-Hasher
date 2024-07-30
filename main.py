from alphabet import *
word=str(input("Enter word for mixing alphabet:"))
answer=creator(word.lower())
key=str(input("Alphabet mixed correctly without error, now enter key for hashing the word:"))
word=str(input("Enter your input that you want to be hashed:"))
key=fixer(key)
word=fixer(word)
hashed_word=mixer(key,word,answer)
print(f"Your word is ready its->{hashed_word}")