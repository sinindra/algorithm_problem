T = int(input())
for test_case in range(1, T + 1):
    S = list(input())
    bar = 0
    ans = 0
    for i in range(len(S)):
        if S[i] == '(' and S[i+1] == ')':
            ans += bar
        elif S[i] == '(':
            bar += 1
        elif S[i] == ')' and S[i-1] != '(':
            ans += 1
            bar -= 1
    print("#{} {}".format(test_case, ans))
    
