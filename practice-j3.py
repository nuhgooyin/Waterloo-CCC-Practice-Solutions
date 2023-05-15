N = int(input())

pointList = []

for i in range(N):
    drop = {}
    drop_input = list(map(int, input().split(',')))
    drop['x'] = drop_input[0]
    drop['y'] = drop_input[1]
    pointList.append(drop)

min_x = None
min_y = None
max_x = None
max_y = None

for coord in pointList:
    x = coord['x']
    y = coord['y']

    if not min_x or x < min_x:
        min_x = x
    if not min_x or x > min_x:
        min_x = x
    if not min_y or y < min_y:
        min_y = y
    if not min_y or y > min_y:
        min_y = y

print(str(min_x - 1) + ',' + str(min_y - 1))
print(str(max_x + 1) + ',' + str(max_y + 1))