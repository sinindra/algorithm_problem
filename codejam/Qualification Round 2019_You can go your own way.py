T = int(input())
for case in range(1, T + 1):
    N = int(input())
    path = input()
    new_path = ''
    for p in path:
        if p == 'S':
            new_path += 'E'
        else:
            new_path += 'S'
            
    print("Case #{} {}".format(case, new_path))