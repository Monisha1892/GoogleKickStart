def forgone(x,y):
    x1 = x
    y1 = y
    lst1 = str(x1)
    lst2 = str(y1)
    if '4' in lst1:
        for i in range(0, len(lst1)):
            if lst1[i] == '4':
                n = len(lst1) - 1 - i
                temp = 4 * (10 ** n)
                y1 = y1 + temp
                x1 = x1 - temp
            else:
                pass
    elif '4' in lst2:
        for i in range(0, len(lst2)):
            if lst2[i] == '4':
                n = len(lst2) - 1 - i
                temp = 4 * (10 ** n)
                x1 = x1 + temp
                y1 = y1 - temp
            else:
                pass
    else:
        return x1,y1

    if '4' not in str(x1) and '4' not in str(y1):
        return x1, y1
    else:
        forgone(x1,y1)




test = int(input())
for t in range(1, test+1):
    n = int(input())
    temp = int(n / 2)
    if temp+temp != n:
        temp1 = temp + 1
        print(temp)
        print(temp1)
        print(temp + temp1 == n)
    else:
        temp1 = temp
    a, b = forgone(temp, temp1)
    print(a + b == n)
    print(f'Case #{t}: {a} {b}')
