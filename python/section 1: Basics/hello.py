print("hello world")

# print('what is your name?')  #ask for their name


myName = raw_input("Enter your name: ")  #Raw input allows for input to be taken from the user 
print(myName)
print('The length of your name is: ' + str(len(myName))) #str() will allow you to print integar's as string

myAge = raw_input('What is your age? ') #Ask for their age
print(myAge)
print('You will be ' + str(int(myAge) + 1)) #Age + 1