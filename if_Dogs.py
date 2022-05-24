''' 3․ Write a Python program to calculate a dog's age in dog's years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
Expected Output:
Input a dog's age in human years: 15
The dog's age in dog's years is 73 (edited)  '''

Number = int(input("Dog's age in human years: "))

if Number <= 2:
    print ("Dog's age in dog's years:",Number * 10.5 )
elif Number > 2:
    print("Dog's age in dog's years:",(Number - 2) * 4 + 21)
else:
    print("Error")
