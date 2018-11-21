d = {'name': 'Tom', 'age': 18, 'married': False}

print(d)

print(d['name'])

# Java java.util.Map

# print(d[0])

d = {}

d = dict()

print(d)

d = dict(key='value')

print(d)

d = {}.fromkeys(['k1', 'k2', 'k3'])

d = {}.fromkeys(['k1', 'k2', 'k3'], 'value')

d = {'name': 'Tom', 'age': 18, 'married': False}

print(d)

# print(d['age1'])

print(d.get('age', 'new value'))

d['name'] = 'Jerry'

print(d)

d['key'] = 'value'

print(d)

d.update({'new key': 'new value'})

print(d)

d.update(test='test value')

print(d)

del d['test']
del d['new key']

d.pop('key')

print(d)

# d.popitem()
# d.popitem()
# d.popitem()

# d.clear()

print(len(d))

print(d.keys())

for key in d:
    print(key, ':', d[key])

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

# del d
#
# print(d)

if 'name' in d:
    print(d['name'])

print(d.get('name1'))

key = []

d = {'key': 'value', 123: '123', (1,): 'tuple'}

print(d)
