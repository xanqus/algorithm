N = int(input())

A = input().split()

currentLocation = [1, 1]


for i in range(len(A)):
    if A[i] == 'L':
        if currentLocation[1] != 1:
            currentLocation[1] -= 1
    elif A[i] == 'R':
        if currentLocation[1] != N:
            currentLocation[1] += 1
    elif A[i] == 'U':
        if currentLocation[0] != 1:
            currentLocation[0] -= 1
    elif A[i] == 'D':
        if currentLocation[0] != N:
            currentLocation[0] += 1

    print(currentLocation)


print(N)
print(A)
