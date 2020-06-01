import random,sys, pyperclip
number = random.randint(1, 10)
print(number)

pyperclip.copy("hello world")
print(pyperclip.paste())

sys.exit()
print('Goodbye');

# Using pip you can install third party modules to do different things
# Use this by using pip install <module>