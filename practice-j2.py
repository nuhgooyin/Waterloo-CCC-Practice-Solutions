P = int(input("P:"))
N = int(input("N:"))
R = int(input("R:"))

total = N
add = N
dayCounter = 0

while total <= P:
    dayCounter += 1

    total += add * R

    add *= R

print(dayCounter)