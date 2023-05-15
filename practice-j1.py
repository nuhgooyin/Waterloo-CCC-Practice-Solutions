S = int(input("Small treats:"))
M = int(input("Medium treats:"))
L = int(input("Large treats:"))

total = 1 * S + 2 * M + 3 * L

if total >= 10:
    print("happy")
else:
    print("sad")