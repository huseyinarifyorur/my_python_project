Number1 = int(input("Enter The First Number:"))
Number2 = int(input("Enter The Second Number:"))

total=0

for number in range(Number1,Number2):
    total=(total + number)
    number += 1
    print(total)