"""This is a python code which takes on a number of different tasks from the user

and queries an API to provide the required respons
"""

import requests
url = 'https://api.datamuse.com/words'


def query_user():
    print("Welcome to the Words Task.\nThis service uses DataMuse API for performing the tasks. \n")
    print("What service do you want? 1. Words Rhyme \t 2. Similar Words  \n 3. Similar Sounds \n")
    user_input = int(input("> "))

    return user_input


def words_rhyme(word):
    """This function returns 5 words that rhymes with the given word"""

    params = {"rel_rhy": word}
    print(f"Here are 5 words which rhyme with {word}")
    req = requests.get(url, params=params).json()

    for entry in req[:5]:
        print(entry['word'])

def similar_words(word):
    """This function returns 5 words similar to the provided word"""

    params = {"ml": word}
    print("Here are 5 similar words")

    req = requests.get(url, params=params).json()

    for entry in req[:5]:
        print(entry['word'])

def similar_sounds(word):
    """This function returns words that sound alike to the provided word"""
    params = {"sl": word}
    print("Here are similar sounding words")

    req = requests.get(url, params=params).json()
    for entry in req[:5]:
        print(entry['word'])


if __name__ == '__main__':
    user_input = query_user()

    if user_input == 1:
        print("You have selected the service - Rhyming words. \nPlease enter a word: \n")
        word = input("> ")
        words_rhyme(word)

    if user_input == 2:
        print("You have selected the service - Similar Words.\nPlease enter a word: \n")
        word = input("> ")
        similar_words(word)

    if user_input == 3:
        print("You have selected the service - Similar Sounds. \nPlease enter a word:\n")
        word = input("> ")
        similar_sounds(word)

