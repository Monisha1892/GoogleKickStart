test = int(input())
for t in range(1, test+1):
    final = [(1,1)]
    arr = list(map(int, input().split()))
    id = arr.pop(0)
    if id == 1:
        n = arr.pop(0)
        k = 0
        while k >= 0:
            p,q = final[k]
            temp1, temp2 = (p, p+q), (p+q, q)
            final.append(temp1)
            final.append(temp2)
            if len(final) > n:
                break
            else:
                k += 1
        print(final)
        print(f"Case #{t}: {final[n-1][0]} {final[n-1][1]}")
    else:
        x = (arr[0], arr[1])
        k = 0
        while k >= 0:
            p,q = final[k]
            temp1, temp2 = (p, p+q), (p+q, q)
            final.append(temp1)
            final.append(temp2)
            if x in final:
                break
            else:
                k += 1
        print(f"Case #{t}: {final.index(x)+1}")

