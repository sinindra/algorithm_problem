N = int(input())
vote = [list(map(int, input().split())) for _ in range(N)]

count = [0] * 151
for S, E in vote:
  for i in range(S,E):
    count[i] += 1
ans = max(count)
print(ans)
