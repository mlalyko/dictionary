import json
from difflib import get_close_matches

data = json.load(open('dictionary.json'))
def retrive_definition(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input('Did you mean {} instead? [yes or no] '.format(get_close_matches(word, data.keys())[0]))
        if action in ['Yes', 'y', 'yes', 'Y']:
            return data[get_close_matches(word, data.keys())[0]]
        elif action in ['No', 'n', 'no', 'N']:
            return ('The word doesn\'t exist, yet.')
        else:
            return ('We don\'t understand your entry. Apologies.')

word_user = input('Enter a word: ')
output = retrive_definition(word_user)
if type(output) == list:
    for item in output:
        print('-', item)
else:
    print('-', output)

while True:
    word_user = input('\nEnter a new word: ')
    output = retrive_definition(word_user)
    if type(output) == list:
        for item in output:
            print('-', item)
    else:
        print('-', output)
