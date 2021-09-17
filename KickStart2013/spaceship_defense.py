# def locating(color, turbo_dic, source, destination, final, temp, delay):
#     for i in turbo_dic.keys():
#         if source == i[0]:
#             if color[i[1]] == color[destination]:
#                 delay += turbo_dic[i]
#                 temp.append(delay)
#             elif:
#                 if i[1] in [i[0] for i in turbo_dic.keys()]:
#                     for j in turbo_dic.keys():
#                         if i[1] == j[0]:
#                             if color[j[1]] == color[destination] or j[1] == destination:
#                                 delay += 0



test = int(input())
for t in range(1, test+1):
    final = []
    rooms = int(input())
    color = [str(input()) for i in range(rooms)]
    m = int(input())
    turbo = [list(map(int,input().split(" "))) for i in range(m)]
    turbo_dic = {(i[0], i[1]): i[2] for i in turbo}
    bots = int(input())
    loc = [list(map(int, input().split(" "))) for i in range(bots)]
    for i in range(bots):
        temp = []
        delay = 0
        source, destination = loc[i]
        print("s, d", source, destination)
        if color[source-1] == color[destination-1]:
            final.append(0)
        elif (source, destination) in turbo_dic:
            print(turbo_dic[(source, destination)])
            final.append(turbo_dic[(source, destination)])
        elif source in [m[0] for m in turbo_dic.keys()]:
            for j in turbo_dic.keys():
                if j[0] == source:
                    print("j", j)
                    delay = 0
                    if color[j[1] -1] == color[destination-1]:
                        delay += turbo_dic[j]
                        temp.append(delay)
                        print(temp)
                    else:
                        for l in turbo_dic.keys():
                            if l[0] == j[1]:
                                delay += turbo_dic[j]
                                prev = j[1]
                                for k in turbo_dic.keys():
                                    if prev == k[0]:
                                        print("k", k)
                                        print("prev",prev)
                                        if k[1] == destination:
                                            delay += turbo_dic[k]
                                            print("delay", delay)
                                            temp.append(delay)
                                            print("temp", temp)
                                            break
                                        elif color[k[1]-1] == color[destination-1]:
                                            delay += turbo_dic[k]
                                            print("delay", delay)
                                            temp.append(delay)
                                            print("temp", temp)
                                            break
                                        elif k[1] in [b[0] for b in turbo_dic.keys()]:
                                            delay += turbo_dic[k]
                                            print("delay", delay)
                                            prev = k[1]
                                            print("last prev", prev)
                                        else:
                                            temp.append(-1)
            if len(temp) == 1 and temp == [-1]:
                print(temp)
                final.append(-1)
            else:
                min_pos = [i for i in temp if i != -1]
                print(temp)
                print(min_pos)
                final.append(min(min_pos))

        else:
            final.append(-1)

    print(f'Case #{t}:')
    for i in final:
        print(i)




