import pprint, random
theBoard = {'top-l': ' ', 'top-m': ' ', 'top-r': ' ', 'mid-l': ' ', 'mid-m': ' ', 'mid-r': ' ', 'low-l': ' ', 'low-m': ' ', 'low-r': ' '}
done = False
pprint.pprint(theBoard)

def createBoard():
  print(theBoard['top-l'] + ' | ' + theBoard['top-m'] + ' | ' + theBoard['top-r'])
  print('-- --- --')
  print(theBoard['mid-l'] + ' | ' + theBoard['mid-m'] + ' | ' + theBoard['mid-r'])
  print('-- --- --')
  print(theBoard['low-l'] + ' | ' + theBoard['low-m'] + ' | ' + theBoard['low-r'])

def userChoiceDefine(userChoice):
  userChoice = userChoice.lower()
  if (theBoard[userChoice]):
    theBoard[userChoice] = 'X'
    return 1
  else:
    return 0

def computerChoice():
  empty = False
  while empty == False:
    row = random.randint(1, 3)
    column = random.randint(1, 3)
    computer = ''
    if row == 1:
      computer = computer + 'top-'
    elif row == 2:
      computer = computer + 'mid-'
    elif row == 3:
      computer = computer + 'low-'
      
    if column == 1:
      computer = computer + 'l'
    if column == 2:
      computer = computer + 'm'
    if column == 3:
      computer = computer + 'r'

    if theBoard[computer] == ' ':
      theBoard[computer] = 'O'
      empty = True

def checkFinish():
  if theBoard['top-l'] == theBoard['top-m'] and theBoard['top-m'] == theBoard['top-r'] and theBoard['top-l'] != ' ':
    if theBoard['top-l'] == 'X':
      return 1
  if theBoard['mid-l'] == theBoard['mid-m'] and theBoard['mid-m'] == theBoard['mid-r']:
    return 1
  if theBoard['low-l'] == theBoard['low-m'] and theBoard['low-m'] == theBoard['low-r']:
    return 1
  if theBoard['top-l'] == theBoard['mid-l'] and theBoard['mid-l'] == theBoard['low-l']:
    print('lol')
    return 1
  if theBoard['top-m'] == theBoard['mid-m'] and theBoard['mid-m'] == theBoard['low-m']:
    return 1
  if theBoard['top-r'] == theBoard['mid-r'] and theBoard['mid-r'] == theBoard['low-r']:
    return 1

while done == False:
  createBoard()
  print('Where would you like to go? Type top/mid/low for row and L/M/R for column. e.g. Top-L')
  userChoice = input()
  while (userChoiceDefine(userChoice) == 0):
    print('I didn\'t catch that, type top/mid/low for row and l/m/r for column. e.g. Top-L')
  computerChoice()
  if checkFinish() == 1:
    break

print('lol')
