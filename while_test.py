numbers = [1, 23, 42, 35, 68, 79, 98]
# print(len(numbers))
# # # print(numbers.pop())
# # # print(len(numbers))
# # # print(numbers.pop())
# # # print(len(numbers))
# # #
# # # numbers.append(101)
# # # print(numbers)

even = []
odd = []

# while ?

while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

print(even)
print(odd)
