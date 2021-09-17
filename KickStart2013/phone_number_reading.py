dic1 = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 0: "zero"}
dic2 = {2: "double", 3: "triple", 4: "quadruple", 5: "quintuple", 6: "sextuple", 7: "septuple", 8: "octuple", 9: "nonuple", 10: "decuple"}
test = int(input())
for t in range(1, test+1):
    final = []
    inputs = list(map(str, input().split(" ")))
    number = [int(i) for i in inputs[0]]
    print(number)
    num_format = list(map(int, inputs[1].split("-")))
    print(num_format)
    m= 0
    count = 1
    words = ""
    for j in range(len(num_format)):
        final.append(number[m:num_format[j]+m])
        m += num_format[j]
    print(final)
    for k in range(0, len(final)):
        previous = final[k].pop(0)
        final[k] = final[k] + [-1]
        for l in final[k]:
            if l == previous:
                count += 1
                if count > 10:
                    temp = (dic1[l] + " ") * count
                else:
                    temp = dic2[count] + " " + dic1[l] + " "
            else:
                if count > 1:
                    words += temp
                    previous = l
                else:
                    words += dic1[previous] + " "
                    previous = l
                count = 1







    print(f"Case #{t}: {words}")


