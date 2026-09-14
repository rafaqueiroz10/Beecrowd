def exibirTabela(chaves, numEnderecosBase):
    for i in range(numEnderecosBase):
        print (f"{i} ->", end=" ")

        for j in range(len(chaves)):
            if(chaves[j] % numEnderecosBase == i):
                print(f"{chaves[j]} ->", end=" ")
            
        
        print("\\")


n = int(input())

for i in range(n):
    m, c = map(int, input().split())
    chaves = list(map(int, input().split()))

    exibirTabela(chaves, m)

    if (i != n-1):
        print()