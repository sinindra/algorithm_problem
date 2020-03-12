def pal(s):
    ans = 0
    for i in range(len(s)):
        for j in range(1, len(s) - i + 1):
            word = s[i:i + j]
            if word == word[::-1]:
                ans += 1
    return ans

T = int(input())
for test_case in range(1, T + 1):
    s = list(input())
    s_sort = sorted(s)
    word = ''
    for w in s_sort:
        word = word + w
    ans = pal(word)

    print("#{} {}".format(test_case, ans))