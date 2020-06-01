def testPassword(password): #To define a function use the var 'def' and colons to signal an indentation on the next line
  if password == 'swordfish':
    print('Access Granted')
  else:
    print('Access Denied')


def testAgeAndName(age, name):
  print(age);
  if name == 'Alice':
    print('Hi Alice')
  elif age < 12:
    print('You are not Alice, kiddo')
  elif age > 2000:
    print('You are a liar')
  elif age > 100:
    print('Pleae give the laptop back grandad')
  elif age > 20:
    print('What is up with adulthood, right?')

password = raw_input('Please type in your password: ')
testPassword(password)

def testName(name):
  if name != '':
    print('Thanks for entering a name')
  else:
    print('You did not enter a name')

name = raw_input('Please type in your name: ')
testName(name)
age = raw_input('Please type in your age: ')
testAgeAndName(int(age), name) #pass raw input with the type it is.