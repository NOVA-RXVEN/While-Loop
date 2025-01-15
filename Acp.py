num = int(input("Enter a Number: "))

count = 0

while num > 0:
    count = count + 1
    num = num//10
    
print(f"The number has {count} Digits!")