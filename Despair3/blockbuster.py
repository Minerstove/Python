n = int(input())
setlist = list(map(int, input().split()))

cur_max = cur_min = 0
best_max = -10**18
best_min = 10**18

for x in setlist:
    cur_max = max(x, cur_max + x)
    best_max = max(best_max, cur_max)

    cur_min = min(x, cur_min + x)
    best_min = min(best_min, cur_min)

answer = max(abs(best_max), abs(best_min))
print(answer)