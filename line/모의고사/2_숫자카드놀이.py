from itertools import permutations

card = list(map(int, input().split()))
K = int(input())
card.sort()
perm = list(permutations(card, 3))

print("{} {} {}".format(perm[K-1][0], perm[K-1][1], perm[K-1][2]))