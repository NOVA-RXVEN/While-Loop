num = int(input("Enter a Number: "))

count = 0

while num > 0:
    count = count + 1
    num = num//10
    
print(f"There are number {count} Digits is the Number {num} !")
