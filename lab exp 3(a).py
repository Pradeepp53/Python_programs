
numbers = [2, 6, 7, 12, 17, 7, 8, 2, 6, 20, 3, 5]
element = int(input("Enter the element to be found: "))

positive_indices = []
negative_indices = []



for i in range(len(numbers)):
    if numbers[i] == element:
        positive_indices.append(i + 1)
        negative_indices.append(-(len(numbers) - i))

print("Positive Index:", positive_indices)

print("Negative Index:", negative_indices)