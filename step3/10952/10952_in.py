# 10952
# A+B - 5

A = 1
B = 1
while 1:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    print(A+B)
