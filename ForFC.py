''' 2․ Write a Python program to convert temperatures to and from celsius, fahrenheit.
[ Formula : c/5 = f-32/9 [ where c = temperature in celsius and f = temperature in fahrenheit ]
Expected Output :
60°C is 140 in Fahrenheit
45°F is 7 in Celsius
Sample Output:
Input the temperature you like to convert? (e.g., 45F, 102C etc.) : 104f
The temperature in Celsius is 40 degrees (edited) '''


temp = input("Input the temperature:(25C or 77F) - ")
degree = int(temp[:-1])
CorF = temp[-1]

if CorF == "C":
  print ("Result - ",degree * 1.8 + 32)
elif CorF == "F":
  print ("Result - ",(degree -32) / 1.8)
else:
  print("input correct value")
