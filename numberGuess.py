#Number guessing game

from random import randint

random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
  guess = int(raw_input("What is your guess?: ")
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "Your lose."
