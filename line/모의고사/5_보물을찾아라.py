import math

N, M = map(int, input().split())
goal = list(map(int, input().split()))

if goal[0] > N - 1 or goal[1] > M - 1:
  print("fail")
elif goal == [0, 0]:
  print("fail")
else:
  time = sum(goal)
  path = math.factorial(time) / math.factorial(goal[0]) / math.factorial(goal[1])
  print(time)
  print(int(path))
  