'''
Sadiqur. Sakib
period 8
Hangman Project
'''

print("Welcome to Hangman please enter a letter from a to z good luck")
from random import randint
#this is the list of words for the user to guess
words = ["mei","genji","hanzo","tracer","lucio","pharah","reinhardt","bastion""mcree""sombra","winston"]
answer = []


selected_word = words[randint(0,len(words)-1)]
#allows user to guess a single letter at a time
for i in range(len(selected_word)):
  answer.append(selected_word[i])
#print(answer)

#this tells the user what the theme of the game is.
print("Lets play hangman overwatch edition!")
underscores = []
for i in range(len(selected_word)):
  underscores.append("_")
#print(underscores)

while(underscores != answer):
    display = ""
    for i in underscores:
        display += i + " "
    print(display)
    # This is the code to allow the user to guess a letter
    user_input = input("Enter a letter:")
    for i in range(len(selected_word)):
        if (user_input == selected_word[i]):
            underscores[i] = user_input
#This makes the while loop end instead of repeating after player wins
if ("_" not in underscores):
   print (selected_word)
   print("YOU DID IT!!!")

