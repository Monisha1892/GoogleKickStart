from math import log

t = int(input())
score = [0, 1.0]
temp = score[1]

for i in range(2, 1000005):
    summ = 1 + temp / i
    score.append(summ)
    temp += summ

for i in range(1, t+1):
    n = int(input())
    if n > 1000000:
        ans = score[1000000] + log(n + 1) - log(1000001)
    else:
        ans = score[n]
    print(f'Case #{i}: {ans}')