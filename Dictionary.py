import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("Did you mean %s instead ? " %get_close_matches(word, data.keys())[0])
        decide = input("press y or n \n")
        decided = decide.lower()
        if decided == "y":
            return data[get_close_matches(word , data.keys())[0]]

    return "Word Not Found! "

word = input("Enter the word you want to search : \n")
output = translate(word)
count=1
if type(output) == list:
    for item in output:
        print(f"Number {count} Meaning :\n")
        print(item)
        count=count+1
        
else:
    print(output)
