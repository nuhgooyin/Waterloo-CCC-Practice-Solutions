stepsDirectionList = []
listOfDirectionNumber = []
directionWayList = []

positionInList = 0
counter = 0
secondCounter = 0
thirdCounter = 0

done = 0
while done == 0:
    number = input()

    if int(number) == 99999:
        done = 1

    if int(number) != 99999:
        directionNumber = number[0:2]
        stepsDirection = number[2:5]
        listOfDirectionNumber.append(directionNumber)
        stepsDirectionList.append(stepsDirection)      

if done == 1:
    for i in listOfDirectionNumber:
        firstNumber = listOfDirectionNumber[positionInList]
        
        digitOne = firstNumber[0:1]
        digitTwo = firstNumber[1:2]
        totalSum = int(digitOne) + int(digitTwo)
        check = int(totalSum)/2
        check = check - int(check) == 0

        if int(totalSum) > 0 and check == True:
            directionWay = "right"
            directionWayList.append(directionWay)

        if check == False:
            directionWay = "left"
            directionWayList.append(directionWay)

        if int(totalSum) == 0:
            previousDirectionWay = directionWayList[counter-1]
            directionWayList.append(previousDirectionWay)
        
        positionInList += 1
        counter += 1

    for i in directionWayList:
        print(directionWayList[thirdCounter], stepsDirectionList[secondCounter])
        secondCounter += 1
        thirdCounter += 1