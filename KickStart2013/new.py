T = int(input())
for x in range(1, T + 1):
    M = int(input())
    pairs = [list(input().split()) for index in range(M)]
    print(pairs)
    y = True
    pair = pairs.pop()
    print(pair)
    print(pairs)
    members = {pair[0]: True, pair[1]: False}
    while pairs:
        previous_length = len(pairs)
        print(previous_length)
        for index, pair in reversed(list(enumerate(pairs))):
            print("pairs",list(reversed(list(enumerate(pairs)))))
            print(index)
            print(pair)
            if pair[0] in members:
                if pair[1] in members:
                    if members[pair[0]] is members[pair[1]]:
                        y = False
                        pairs.clear()
                        break
                    else:
                        pairs.pop(index)
                else:
                    members[pair[1]] = not members[pair[0]]
                    pairs.pop(index)
            elif pair[1] in members:
                members[pair[0]] = not members[pair[1]]
                pairs.pop(index)
        if len(pairs) == previous_length:
            pair = pairs.pop()
            members[pair[0]] = True
            members[pair[1]] = False
    y = "Yes" if y else "No"
    print(f"Case #{x}: {y}", flush=True)
#
# Dead_Bowie Fake_Thomas_Jefferson
# # Fake_Thomas_Jefferson Fury_Leika
# # Fury_Leika Dead_Bowie

