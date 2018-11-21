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

d.update({'new key':'new value'})

print(d)

d.update(test='test value')

print(d)

del d['test']
del d['new key']

d.pop('key')

print(d)

# del d
#
# print(d)
