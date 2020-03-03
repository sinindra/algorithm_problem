import re
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = input()
    S = re.split('[.?!]', S)
    S_list = []
    ans_list = [0] * N
    for i in range(N):
        S_list.append(S[i].split())
    
    for i in range(N):
        for s in S_list[i]:
            if bool(re.match('^[A-Z][a-z]*',s)) and not bool(re.match('.*[0-9]+',s)) and not bool(re.match('^[A-Z].*[A-Z]+',s)):
                ans_list[i] += 1
    print("#{}".format(test_case), end="")
    for i in range(N):
        print("", ans_list[i], end="")
    print()
