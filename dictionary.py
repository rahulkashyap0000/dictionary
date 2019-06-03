import json
from difflib import get_close_matches

dictionary = json.load(open("./data.json"))


def meaning(word):
    word = word.lower()
    word = word.replace(" ", "")
    close_word = get_close_matches(word, dictionary.keys())[0]
    if word in dictionary:
        return dictionary[word]
    elif(len(close_word) > 0):
        print("No such word as "+word+"\n" +
              "Showing meaning instead of " + close_word +
              " \n")

        return dictionary[close_word]
    else:
        return "Please check the word again"


word = input("Please enter the word: ")
answer = meaning(word)
if type(answer) == list:
    i = 1
    for result in answer:
        print(str(i)+". "+result)
        i = i+1
else:
    print(result)
