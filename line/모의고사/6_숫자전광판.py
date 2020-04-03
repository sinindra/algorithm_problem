def num(max_K, K, n, align):
  word = [["."] * K for _ in range(2*K - 1)]
  if n == 0:
    word[0], word[-1] = ["#"] * K, ["#"] * K
    for w in word[1:-1]:
      w[0], w[-1] = "#", "#"
  if n == 1:
    for w in word:
      w[-1] = "#"
  if n == 2:
    word[0], word[-1], word[K - 1] = ["#"] * K, ["#"] * K, ["#"] * K
    for w in word[1:K-1]:
      w[-1] = "#"
    for w in word[K:-1]:
      w[0] = "#"
  if n == 3:
    word[0], word[-1], word[K - 1] = ["#"] * K, ["#"] * K, ["#"] * K
    for w in word[1:K-1]:
      w[-1] = "#"
    for w in word[K:-1]:
      w[-1] = "#"
  if n == 4:
    word[K - 1] = ["#"] * K
    for w in word[:K-1]:
      w[0], w[-1] = "#", "#"
    for w in word[K:]:
      w[-1] = "#"
  if n == 5:
    word[0], word[-1], word[K - 1] = ["#"] * K, ["#"] * K, ["#"] * K
    for w in word[1:K-1]:
      w[0] = "#"
    for w in word[K:-1]:
      w[-1] = "#"
  if n == 6:
    word[-1], word[K - 1] = ["#"] * K, ["#"] * K
    for w in word[:K-1]:
      w[0] = "#"
    for w in word[K:-1]:
      w[0], w[-1] = "#", "#"     
  if n == 7:
    word[0] = ["#"] * K
    for w in word[1:]:
      w[-1] = "#"
  if n == 8:
    word[0], word[K - 1], word[-1] = ["#"] * K, ["#"] * K, ["#"] * K
    for w in word[1:K-1]:
      w[0], w[-1] = "#", "#"
    for w in word[K:-1]:
      w[0], w[-1] = "#", "#"
  if n == 9:
    word[0], word[K - 1] = ["#"] * K, ["#"] * K
    for w in word[1:K-1]:
      w[0], w[-1] = "#", "#"
    for w in word[K:]:
      w[-1] = "#"
  
  if max_K != K:
    add_num = 2 * (max_K - K)
    if align == "TOP":
      for i in range(add_num):
        word.append(["."] * K)
        
    elif align == "BOTTOM":
      tmp = [["."] * K for _ in range(add_num)]
      tmp.extend(word)
      word = tmp
    
    elif align == "MIDDLE":
      for i in range(int(add_num/2)):
        word.append(["."] * K)
      tmp = [["."] * K for _ in range(int(add_num/2))]
      tmp.extend(word)
      word = tmp
      
        
  return word


N, align = list(map(str, input().split()))
N = int(N)
K_list, num_list = [0] * N, [0] * N

for i in range(N):
  K_list[i], num_list[i] = map(str, input().split())
  K_list[i] = int(K_list[i])
max_K = max(K_list)

ans = []
for i in range(N):
  for j in str(num_list[i]):
    ans.append(num(max_K, K_list[i], int(j), align))
    
for i in range(2* max_K - 1):
  for j in ans:
    for s in j[i]:
      print(s, end="")
    print("", end=" ")
  print()