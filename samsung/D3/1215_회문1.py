import copy

def test(arr, len_str):
    sol = 0
    for i in range(8):
        for j in range(8 - len_str + 1):
            if arr[i][j:j+len_str] == arr[i][j:j+len_str][::-1]:
                sol += 1
    return sol
    
#T = int(input())
#for test_case in range(1, T+1):
for test_case in range(1, 11):
    len_str = int(input())
    arr = []
    for i in range(8):
        arr.append(list(input()))
    
    arr_tr = copy.deepcopy(arr)
    for i in range(8):
        for j in range(8):
            arr_tr[i][j] = arr[j][i]
    
    sol1 = test(arr, len_str)
    sol2 = test(arr_tr, len_str)
    ans = sol1 + sol2

    print("#{} {}".format(test_case, ans))
