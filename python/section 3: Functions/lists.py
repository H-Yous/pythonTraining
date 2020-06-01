spam = ['cat', 'bat']
print(spam[0])

spam2 = [['cat', 'bat', 'elephant', 'lion'], [10, 20, 30, 40, 50]]
print(spam2[0][1])
print(spam2[1][3])

spam3 = ['cat', 'bat', 'elephant', 'lion']
print(spam3[1:3])

spam4 = ['cat', 'bat', 'elephant', 'lion']
spam4[1:3] = ['CAT', 'BAT', 'ELEPHANT']
print(spam4)

del spam4[2]
print(spam4)

spam5 = list('hello')
print(spam5)

spam6 = ['cat', 'bat', 'elephant', 'lion']
print('lion' in spam6)
print('lion' not in spam6)

cat=['fat', 'orange', 'loud']
size, color, disposition = cat
print(size)
print(color)
print(disposition)

spam7 = ['lion', 'elephant', 'bat', 'cat']
print(spam7.index('bat'))

spam7.append('moose')
print(spam7);
spam7.remove('bat')
print(spam7)

spam7.sort(reverse=True)
print(spam7)

spam8 = ['A', 'z' , 'Z','a']
spam8.sort(key=str.lower)
print(spam8)