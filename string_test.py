s = 'Hello, World!'

print(s[0])

print(s[len(s) - 1])

print(s[-1])

s1 = 'Hello, '
s2 = 'World!'

print(s1 + s2)

print(s1, s2)

print(s * 2)

print(s[0:-1])

print(s[0:5:3])  # <c:foreach  step="1"> 步长

print('Hello' in s)

print(True)

print(False)

s = 'hello, World!'

print(s.capitalize())

print(s.center(19))

print(s.zfill(20))  # z = zero

print(s.count('l', 0, 4))

print(s.endswith('o', 0, 5))

print(s.startswith('e', 1, 5))

print(s.find(','))

print(s.isalnum())  # al=alpha num=number

print(s.isalpha())

print(s.isdigit())

s = "A一二三"
print(s.islower())
print(s.isupper())

s = "123a"

print(s.isnumeric())

s = '    '
print(s.isspace())

s = 'Hello, World!'
print(s.lower())
print(s.upper())
print(s.swapcase())

s = '       Hello, World!      '
print(s.lstrip())
print(s.rstrip())
print(s.strip())  # trim()


s = "HelloWorld一"

print(min(s))
print(max(s))

s = 'Hello, World!'
print(s.replace('l', 'L', 2))

print(type(123))
print(type(str(123)))

s = '123'

print(s.isdigit())
print(s.isnumeric())
print(s.isdecimal())

