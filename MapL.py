'''Write a Python program to add two given lists using map and lambda (edited)
Original list:
[1, 2, 3]
[4, 5, 6]
Result: after adding two list
[5, 7, 9] (edited) '''

numbers1 = [1, 2, 3]
numbers2 = [4, 5, 6]

result = map(lambda x, y: x + y, numbers1, numbers2)
print(list(result))

