N, K = map(int, input().split())
group = [int(input()) for _ in range(N)]
ticketBox = [0] * K

for i in range(N):
  minIdx = ticketBox.index(min(ticketBox))
  ticketBox[minIdx] += group[i]
  
print(max(ticketBox))