spam = 0
while spam < 5:
  spam += 1
  if spam == 3:
    continue #Continue stops this execution of the cycle and jumps back to the beginning
  print('spam is: ' + str(spam))
  
#Input validation is when you await a specifc value before moving on.
name = ''
while name != 'Humza':
  name = raw_input('Please type your name: ')
  if name == 'your name':
    break;
print('Thank you');
  
