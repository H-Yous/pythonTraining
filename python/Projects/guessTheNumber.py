import random

print('Hello, what is your name?')
name = input()
ranNum = random.randint(2, 19)

print('Well, ' + name + ', I am thinking of a number between 1 and 20')

for guessesTaken in range(1, 6):
  print('Take a guess.')
  validGuess = False
  while True:
    try:
      userGuess = int(input())
      break
    except ValueError:
      print('Oops! That\'s not a number')
      guessesTaken = guessesTaken - 1
      continue
  if (userGuess >= 20 or userGuess <= 1):
    print('Your guess is outside of the range')
  elif (userGuess > ranNum):
    print('Too high!')
  elif (userGuess < ranNum):
    print('Too low')
  else:
    break
  

if (userGuess == ranNum):
    print('You got it right ' + name + ' in ' + str(guessesTaken) + ' guesses! Well done!')
else:
  print('You failed, try again next time!')

