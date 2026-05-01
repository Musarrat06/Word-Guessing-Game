import random
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']


name = input("Enter your name : ")
print("Good Luck!", name)



Random_w = random.choice(words)



turns = 12

while turns > 0 :

  for word in words:
    Guess = input("Guess the word  :  ")
    for char in Random_w:
      if char in Guess:
        print(char,end=" ")
      else:
        print("__")



    if Guess != Random_w:
      print("wrong answer.")
      turns -= 1
      print("you have ",turns,"turns left")

      if turns == 0:
        print("You Lost the game.")
        print("The correct word is : ",Random_w)
        break

    else:
      print("Congracts....You win the game!")
      break

  break
