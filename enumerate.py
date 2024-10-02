#Enumerate()

# enumerate through a string with the character and index counter
for i, char in enumerate("hellooo"):
    print(i, char)
# Enumerate through a tuple with the number and index counter
for i, char in enumerate((1, 2, 3)):
    print(i, char)

for i, char in enumerate(list(range(100))):
    print(i, char)
    if char == 50:
        print(f"The character at 50 is: {i}")
