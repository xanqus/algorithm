N, M = map(int, input().split())

my_list = [list(map(int, input().split())) for _ in range(N)]

answer_list = list()
for i in range (N):

    answer_list.append(min(my_list[i]))

print(max(answer_list))





