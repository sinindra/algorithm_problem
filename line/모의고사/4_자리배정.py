N = int(input())
student = list(map(int, input().split()))

full = [i for i, s in enumerate(student) if s == 1]
if len(full) == 1:
  ans = max(full[0], N - 1 - full[0])
  print(ans)

else:
  dist = [full[i+1] - full[i] for i in range(len(full) - 1)]
  
  ans = int(max(dist) // 2 )
  
  print(ans)