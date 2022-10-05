from hangman_art import logo, stages
from hangman_words import word_list
import random

lives = 6

print(logo)
print(stages[lives])

current_word = []
alread_used_words = []

secret_word = random.choice(word_list)
for x in secret_word:
  current_word.append("*")

def create_new_word(word):
  new_word = ""
  for x in word:
    new_word +=x
  return new_word


print("Word Status")
print(create_new_word(current_word))
  
while True:
  if "*" not in current_word:
    print("You're WIN!!!")

    new_game = input("Do you wanna play again? 'y' or 'n'? ")
    if new_game == "y":
      current_word = []
      alread_used_words = []
      lives = 6
      print(logo)
      print(stages[lives])
      secret_word = random.choice(word_list)
      for x in secret_word:
        current_word.append("*")
      print("Word Status")
      print(create_new_word(current_word))
    else:
      print("Buy!")
      break
    
  if lives <=0:
    print("You lose!")
    print(stages[lives])
    break
  else:
    choose = input("Write letter: ").lower()
    if choose in alread_used_words:
      print("This letter already used.")
    elif choose in secret_word:
      alread_used_words.append(choose)

      for num in range(len(secret_word)):
        if secret_word[num] == choose:
          current_word[num] = choose
          
      print(stages[lives])
      print("Excellent. Word Status.")
      print(create_new_word(current_word))
    else:
      lives-=1
      print(stages[lives])
      print("Oh no. You are mistaken :(")