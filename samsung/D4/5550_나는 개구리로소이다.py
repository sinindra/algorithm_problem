T = int(input())
for test_case in range(1, T + 1):
    sound = input()
    frog = []
    frog_max = 0
    ans = 0
    for s in sound:
        if s == 'c':
            frog.append(1)
            if len(frog) > frog_max:
                frog_max = len(frog)
        
        elif s != 'c' and len(frog) == 0:
            ans = -1
            break

        else:
            # print(frog)
            for idx in range(len(frog)):
                # print(s, frog[idx])
                if s == 'r' and frog[idx] == 1:
                    frog[idx] += 1
                    break

                elif s == 'o' and frog[idx] == 2:
                    frog[idx] += 1
                    break

                elif s == 'a' and frog[idx] == 3:
                    frog[idx] += 1
                    break

                elif s == 'k' and frog[idx] == 4:
                    frog.pop(0)
                    break

                elif idx == len(frog) - 1:
                    ans = -1
                    break
        if ans == -1:
            break
    
    if ans == -1 or len(frog) != 0:
        sol = -1
    else:
        sol = frog_max

    print("#{} {}".format(test_case, sol))