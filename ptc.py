from itertools import product
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))
for i in product(l1, l2):
    print(tuple(i), end=' ')