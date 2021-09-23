location = input()
row = int(location[1])
column = int(ord(location[0]) - ord('a') + 1)

steps = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if 0 < next_row < 9 and 0 < next_column < 9:
        result = result + 1

print(result)