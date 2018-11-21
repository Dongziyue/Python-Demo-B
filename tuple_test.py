names = ('Tom', 'Jerry')

print(names)

numbers = (1,)

print(numbers)

print(len(numbers))

print(names[0])

week_day = ('Mon', 'Thu')
# week_day = ['Mon', 'Thu']

students = ['Tom', 'Jerry']
# students = ('Tom', 'Jerry')

print('Tom' in names)

names = tuple(('Tom', 'Jerry', 'Spike'))

print(names)

print(names.count('Tom'))

print(names.index('Tom'))

superstars = ['Tom', 'Jerry']

names = (superstars, 'Spike')

# print(superstars)
print(names)

# names[1] = 'Tyke'

names[0].append('Tyke')

print(names)

for name in names:
    print(name)


