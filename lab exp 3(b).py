n = int(input("Enter number of elements in list: "))
numbers = []
for i in range(n):
    number = int(input(f"Enter the value : "))
    numbers.append(number)
    
ascending = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i+1]:
        ascending = False
        break
        
print("Original list:", numbers)

if ascending:
    print("Yes, the list is in ascending order.")
else:
    print("No, the list is not in ascending order.")
