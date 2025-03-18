"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Karel Bláha
email: karel.blaha@gmail.com
"""

### tady bude začínat tvůj kód
import sys

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

registered_users = {
  "bob":"123",
  "ann":"pass123",
  "mike":"password123",
  "liz":"pass123"}

username = input("username:")
password = input("password:")

if password != registered_users.get(username):
  print("unregistered user, terminating the program...")
  sys.exit()

print("-"*40, "\nWelcome to the app, ", username,
      "\nWe have 3 texts to be analyzed.")
print("-"*40)
i = int(input("Enter a number btw. 1 and 3 to select: "))

if i not in range (1,3):
  print("unavailable value, terminating the program...")
  sys.exit()

print("-"*40)

words = TEXTS[i-1].split()
words_count = len(words)
words_title = 0
words_upper = 0
words_lower = 0
words_numeric = 0
words_numeric_sum = 0
words_lengths = []
word_ocurrencces = {}

for word in words:
  words_lengths.append(len(word.replace(',','').replace('.','')))
  if word.istitle():
    words_title += 1
  if word.isupper():
    words_upper += 1  
  if word.islower():
    words_lower += 1  
  if word.isnumeric():
    words_numeric += 1
    words_numeric_sum += int(word)

print("There are ", words_count, " words in the selected text.")
print("There are ", words_title, " titlecase words.")
print("There are ", words_upper, " uppercase words.")
print("There are ", words_lower, " lowercase words.")
print("There are ", words_numeric, " numeric words.")
print("The sum of all the numbers: ", words_numeric_sum)
print("-"*40)
print("LEN  |  OCCURRENCES            |  NR.")
print("-"*40)

for x in range (1, max(words_lengths)+1):
  word_ocurrencces.update({x:0})

for w in words_lengths:
  word_ocurrencces.update({w:(word_ocurrencces.get(w)+1)})

for key in word_ocurrencces.keys():
  print(" "*(2-len(str(key))), key, " | ", "*"*word_ocurrencces.get(key),
        " "*(20-word_ocurrencces.get(key)), " | ", word_ocurrencces.get(key))