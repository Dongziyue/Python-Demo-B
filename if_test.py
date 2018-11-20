"""
C
if ()
{
    // ...
}

Java
if () {
    // ...
}

Python
if ():
    // ...

"""

score = 55

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 60:
    print('C')
else:
    print('D')

if score >= 60: print('passed...')

# (condition)?value1:value2 三目运算符

# value1 if condition else value2 Python

print('A' if score >= 90 else ('B' if score >= 60 else 'C'))


