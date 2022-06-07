num = int(input("Input number: "))
for i in range(2,num//2):
    if num % i == 0:
        print(f"the number {num} is NOT prime")
    else:
        print(f"the number {num} is prime")
