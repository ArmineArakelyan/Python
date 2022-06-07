''' .Write a Python program to find the values of length six in a given list using Lambda. (edited)
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
result: [Monday, Friday, Sunday] '''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
weekdays1 = []

for i in weekdays:
    if len(i) == 6:
        weekdays1.append(i)

print(weekdays1)