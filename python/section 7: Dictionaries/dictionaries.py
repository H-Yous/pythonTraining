eggs = {'type': 'large', 'color': 'white', 'amount': 12}

for k, v in eggs.items():
  print(k, v)

if 'type' in eggs:
  print(eggs['type'])

print(eggs.get('age', 0))

if 'age' not in eggs:
  eggs['age'] = '2 weeks'
  print(eggs['age'])

eggs.setdefault('color', 'black')
print(eggs['color'])