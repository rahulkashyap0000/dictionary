import json

dictionary = json.load(open("./data.json"))


def meaning(word):
    if word in dictionary:
        return dictionary[word]
    else:
        return "Word not found. Please check the word"


word = input("Please enter the word: ")
word = word.lower()
word = word.replace(" ", "")
print(meaning(word))
