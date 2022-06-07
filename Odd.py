'''
Transpose of a Matrix using List Comprehension
example [[1, 2], [3,4], [5,6], [7,8]] => [[1, 3, 5, 7], [2, 4, 6, 8]] '''

lis1 = []
lis2 = []
list1 = [[1, 2], [3,4], [5,6], [7,8]]
for i in list1:
    for s in i:
        if s % 2 == 0:
            lis1.append(s)
        else:
            lis2.append(s)
print(lis1)
print(lis2)

