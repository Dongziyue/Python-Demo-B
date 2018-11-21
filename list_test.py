names = ['Tom', 'Jerry']

names.append('Spike')

names.insert(2, 'Tyke')

name = names.pop()

names[0] = 'tom'

# names.clear()

# print(names[-1])

print(len(names))

print(name)

print(names)

new_names = names.copy()

print(new_names)

print(names == new_names)

names.append('Jerry')

print(names.count('Jerry'))

names.extend(new_names)

print(names)

print(names.index('Jerry'))

names.remove('Jerry')

print(names)

names.reverse()

print(names)

names.sort()

print(names)

names.sort(reverse=True)

print(names)

names[0] = 'tommmmy'


def f(s):
    return len(s)


names.sort(reverse=True, key=f)

print(names)

for name in names:
    print(name)

superstars = ['Tom', 'Jerry']
names = [superstars, 'Spike']

print(names)

print(names[0][1])
