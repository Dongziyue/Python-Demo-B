names = {'Tom', 'Jerry', 123, True, 123}

print(names)

names.add('test')

print(names)

names.remove('test')

print(names)

# names.clear()

print(names)  # {}

names.pop()  # random remove

print(names)


# java.util.Set

names1 = {'Tom', 'Jerry', 'Spike'}
names2 = {'Tom', 'Jerry'}

names3 = names1.difference(names2)

print(names3)
print(names1)

# names1.difference_update(names2)

print(names1)

names4 = names1.intersection(names2)

print(names4)

names1.intersection_update(names2)

print(names1)

names1 = {'Tom'}

print(names1.isdisjoint(names2))

print(names1.issubset(names2))

print(names2.issuperset(names1))

names1 = {'Tom', 'Tyke'}

print(names1)

names5= names1.symmetric_difference(names2)

print(names5)

names1.symmetric_difference_update(names2)

print(names1)

names6 = names1.union(names2)

print(names6)

names1.update(names2)  # union_update

print(names1)

print(names1 & names2)

print(names1 | names2)

for name in names:
    print(name)
