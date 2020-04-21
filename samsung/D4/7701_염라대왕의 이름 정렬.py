T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    nameList = {input(): 1 for _ in range(N)}
    sortedName = sorted(nameList.keys(), key = lambda x : (len(x), x))

    print("#{}".format(test_case))
    for name in sortedName:
        print(name)