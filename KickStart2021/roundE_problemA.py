t = int(input())

for m in range(t):
    s = list(input())
    other = s[:]
    chars = [(s.count(i), i) for i in set(s)]
    chars.sort(reverse=True)
    if chars[0][0] > len(s)/2:
        ans = 'IMPOSSIBLE'
    else:
        indices = []
        for char in chars[1:]:
            for i in range(len(s)):
                if (s[i] == char[1]):
                    indices.append(i)

        for i in range(len(s)):
            if (s[i] == chars[0][1]):
                indices.append(i)

        j = 0
        for element in chars:
            char = element[1]
            for i in range(len(s)):
                if (s[i] == char):
                    other[i] = s[indices[j]]
                    j+=1

        ans = ''.join(other)


    print(f'Case #{m+1}: {ans}')

