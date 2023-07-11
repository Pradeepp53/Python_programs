a = {1, 2, 3, 4}
b = {1, 2, 3,}

sub = True
for i in b:
    if i not in a:
        sub = False
        break

# Print the result
print(sub)
