import json
import difflib
from difflib import get_close_matches
data = json.load(open("data.json",'r'))

def translate(Word):
    Word=Word.lower()
    Word1=Word.capitalize()
    Word2=Word.upper()
    if Word in data:
        return data[Word]
    elif Word1 in data:
        return data[Word1]
    elif Word2 in data:
        return data[Word2]
    elif len(get_close_matches(Word,data.keys()))>0:
        YN = input('Did you mean %s? Enter Y if yes, or N if no: '%get_close_matches(Word,data.keys())[0])
        if YN == 'Y' or YN == 'y':
            return data[get_close_matches(Word,data.keys())[0]]
        elif YN == 'N' or YN == 'n':
            return 'Not such word found in the dictionary.'
        else:
            return 'We were unable to understand your entry.'
    else:
        return 'Word not found.'


Word=input("Enter the word: ")
#Word=get_close_matches(Word,data.keys(),n=1)[0]
#Word=str(Word)
Ans = translate(Word)
if type(Ans) == list:
    for item in Ans:
        print(item)
else:
    print(Ans)