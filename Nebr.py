
''' Given an array. Create the array which elements are products between two neighbors '''


lst1 = [10, 2, 6, 3, 12, 5, 9, 8, 6]
sum1 = 0
for i in range(len(lst1)-1):
    sum1 = lst1[i] * lst1[i+1]
    print(sum1, ",", end="")


