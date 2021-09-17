test = int(input())
for t in range(1, test+1):
    n = int(input())
    order = list(map(int, input().split(" ")))
    even = [i for i in order if i % 2 == 0]
    even.sort(reverse=True)
    odd = [i for i in order if i % 2 != 0]
    odd.sort()
    e = 0
    o = 0
    for j in range(0, len(order)):
        if order[j] % 2 == 0:
            order[j] = even[e]
            e += 1
        else:
            order[j] = odd[o]
            o += 1
    print(f'Case #{t}: ',end="")
    for i in order:
        print(i, end=" ")
    print()

