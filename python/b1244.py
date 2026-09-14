n = int(input())

for _ in range(n):
    s = str(input())

    strings = s.split(' ')

    dic = []

    for string in strings:
        dic.append({"palavra": string, "tam": len(string)})

    dic.sort(key=lambda item:item["tam"], reverse=True)

    contImp = 0

    for item in dic:
        contImp += 1

        if contImp == len(strings):
            print(item["palavra"])
        else:
            print(item["palavra"], end=" ")