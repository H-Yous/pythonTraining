def div42by(divideBy):
  try:
    return 42 / divideBy
  except  :
    print('Error: You tried to divide by zero.')

def tryAttempt1():
  print(div42by(2))
  print(div42by(10))
  print(div42by(0))
  print(div42by(1))

# tryAttempt1()

print('How many cats do you have?')
numCats = input()
try:
  if int(numCats) >= 4:
    print('That is a lot of cats')
  elif int(numCats) < 0:
    print('You can\'t have a negative amount of cats')
  else:
    print('That is not that many cats')
except ValueError:
  print('You did not enter a number.')

# Use if and else statements for something that won't break the code
# Use try and except statements for when something will break the code.