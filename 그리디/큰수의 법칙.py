A = input()
B = input()
data = list(map(int, B.split()))
data.sort()
N = int(A.split()[0])
M = int(A.split()[1])
K = int(A.split()[2])


B_N1 = data[N-1]
B_N2 = data[N-2]

answer = (M-(M//K))*B_N1 + M//K * B_N2

print(answer)