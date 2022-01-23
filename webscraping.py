"""Aidan Glynn """

from bs4 import BeautifulSoup as soup
from csv import DictReader
from random import randint
from googletrans import Translator
import csv

translator = Translator()  


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a CSV into a table."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    
    # Prepare to read the data file as a csv rather than just strings
    csv_reader = DictReader(file_handle)

    # read each row of the csv line-by-line
    for row in csv_reader:
        result.append(row)

    # close file when done to free its resoruces
    file_handle.close()
    
    return result

final_list = read_csv_rows('verbs.csv')

language = str(input("What language are we learning today? "))
number_of_words = int(input("How many words would you like to study? "))

words = []

for i in range(number_of_words):
    word = input(str("What word would you like to study? "))
    words.append(word)

final_final_list = []

for l in words:
    for i in final_list:
        if (l in i.values()) and ("Indicative" in i.values()) and (("Preterite" in i.values()) or ("Present" in i.values()) or ("Future" in i.values())):
            final_final_list.append(i)

quiz_ready_vocab = []

for j in range(3*number_of_words):
    if j == 0:
        quiz_ready_vocab.append(final_final_list[j]['infinitive_english'])
    quiz_ready_vocab.append('yo')
    quiz_ready_vocab.append(final_final_list[j]['form_1s'])
    quiz_ready_vocab.append('tú')
    quiz_ready_vocab.append(final_final_list[j]['form_2s'])
    quiz_ready_vocab.append('ella')
    quiz_ready_vocab.append(final_final_list[j]['form_3s'])
    quiz_ready_vocab.append('nosotros')
    quiz_ready_vocab.append(final_final_list[j]['form_1p'])
    quiz_ready_vocab.append('vosotros')
    quiz_ready_vocab.append(final_final_list[j]['form_2p'])
    quiz_ready_vocab.append('ellos')
    quiz_ready_vocab.append(final_final_list[j]['form_3p'])

number_of_times = int(input("How many questions would you like to get? "))

counter = 0
while counter < number_of_times:
    random_int = randint(0, 24*number_of_words)
    while quiz_ready_vocab[random_int] == 'yo' or quiz_ready_vocab[random_int] == 'tú' or quiz_ready_vocab[random_int] == 'ella' or quiz_ready_vocab[random_int] == 'nosotros' or quiz_ready_vocab[random_int] == 'vosotros' or quiz_ready_vocab[random_int] == 'ellos' or random_int == 0:
        random_int = randint(0, 24)


    word = f'{quiz_ready_vocab[random_int]}'
    translate_text = translator.translate(f'{quiz_ready_vocab[random_int-1]} {quiz_ready_vocab[random_int]}',dest='en')  
    final_string = str(translate_text.text)
    final_string.lower()
    print(final_string)

    guess = str(input(f"Translate: {word}: "))
    if guess == final_string:
        print("Correct!")
    else: 
        print(f"Incorrect. The correct translation is {final_string}")
    
    counter += 1
