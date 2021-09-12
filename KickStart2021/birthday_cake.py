test = int(input())
for t in range(1, test+1):
    r, c, k = [int(i) for i in input().split(" ")]
    r1, c1, r2, c2 = [int(j) for j in input().split(" ")]
    if k < c1:
        temp = c1 / k
        count = temp