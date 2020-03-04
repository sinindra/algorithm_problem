key = {"2": "abc", "3": "def", "4": "ghi",
        "5": "jkl", "6": "mno", "7": "pqrs",
        "8": "tuv", "9": "wxyz"}
T = int(input())
for test_case in range(1, T + 1):
    S, N = map(str, input().split())
    word = list(map(str, input().split()))
    W = []
    for i in range(len(S)):
        W.append(key[S[i]])
    
    ans = 0
    for i in range(int(N)):
        l = 0
        for j in range(len(word[i])):
            if word[i][j] in key[S[j]]:
                l += 1
            else:
                break
            if l == len(S):
                ans += 1

    print("#{} {}".format(test_case, ans))

