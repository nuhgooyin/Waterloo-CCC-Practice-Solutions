B = int(input())

P = 5 * B - 400

if P < 100:
    seaLevel = 1
elif P > 100:
    seaLevel = -1

else:
    seaLevel = 0

print(P)
print(seaLevel)