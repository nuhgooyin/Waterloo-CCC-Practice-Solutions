N = int(input())

nameBidsList = []
valueBidsList = []

for i in range(N):
    name = input()
    value = int(input())
    nameBidsList.append(name)
    valueBidsList.append(value)

highestBidValue = max(valueBidsList)

index = valueBidsList.index(highestBidValue)

print(nameBidsList[index])
