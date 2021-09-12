# def tester(lst, dic):
#     for x in lst:
#         if x in dic:
#             if dic[x] in lst:
#                 return False
#             else:
#                 pass
#         else:
#             pass
#     else:
#         return True
#
# test = int(input())
# for t in range(1, test+1):
#     dic = {}
#     group1 = []
#     group2 = []
#     m = int(input())
#     for i in range(0, m):
#         a, b = list(map(str, input().split(" ")))
#         dic[a] = b
#         group1.append(a)
#         group2.append(b)
#     print(group1)
#     print(group2)
#     print(dic)
#     ans = tester(group1, dic)
#     print(ans)
#     if ans:
#         if tester(group2, dic):
#             print(f'Case #{t}: Yes')
#         else:
#             print(f'Case #{t}: No')
#     else:
#         print(f'Case #{t}: No')
#     group2.clear()
#     group1.clear()

test = int(input())
for t in range(1, test+1):
    dic = {}
    group1 = []
    group2 = []
    count = []
    m = int(input())
    pairs = [list(map(str, input().split(" "))) for i in range(0,m)]
    dic[pairs[0][0]] = [pairs[0][1]]
    group1.append(pairs[0][0])
    dic[pairs[0][1]] = [pairs[0][0]]
    group2.append(pairs[0][1])
    for u in range(0, len(pairs)):
        for v in range(0, len(pairs[u])):
            if pairs[u][v] not in count:
                count.append(pairs[u][v])
    siz = len(count)
    for i in range(1, len(pairs)):
        for j in range(0, len(pairs[i])):
            if pairs[i][j] not in dic:
                dic[pairs[i][j]] = []
                if j == 1:
                    dic[pairs[i][j]].append(pairs[i][0])
                else:
                    dic[pairs[i][j]].append(pairs[i][1])
            else:
                if j == 1:
                    dic[pairs[i][j]].append(pairs[i][0])
                else:
                    dic[pairs[i][j]].append(pairs[i][1])
    print(dic)
    for x in range(1, len(pairs)):
        for y in range(0, len(pairs[x])):
            temp = pairs[x][y]
            flag = 0
            print(temp)
            if temp in group1 or temp in group2:
                print("yes")
                continue
            else:
                if len(group1) <= len(group2):
                    for g in dic[temp]:
                        if g in group1:
                            flag = 1
                            break
                    else:
                        group1.append(temp)
                    if flag:
                        for h in dic[temp]:
                            if h in group2:
                                break
                        else:
                            group2.append(temp)
                elif len(group2) <= len(group1):
                    for g in dic[temp]:
                        if g in group2:
                            flag = 1
                            break
                    else:
                        group2.append(temp)
                    if flag:
                        for h in dic[temp]:
                            if h in group1:
                                break
                        else:
                            group1.append(temp)
    print(group1)
    print(group2)
    if (len(group1) + len(group2)) == siz:
        print(f"Case #{t}: Yes")
    else:
        print(f"Case #{t}: No")
    dic.clear()
    count.clear()
    group1.clear()
    group2.clear()


















    #     dic[a] = b
    #     group1.append(a)
    #     group2.append(b)
    # print(group1)
    # print(group2)
    # print(dic)
    # ans = tester(group1, dic)
    # print(ans)
    # if ans:
    #     if tester(group2, dic):
    #         print(f'Case #{t}: Yes')
    #     else:
    #         print(f'Case #{t}: No')
    # else:
    #     print(f'Case #{t}: No')
    # group2.clear()
    # group1.clear()
    #

