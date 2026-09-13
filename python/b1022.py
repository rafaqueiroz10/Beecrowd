n = int(input())

for _ in range(n):
    s = str(input())

    contBarras = 0

    opDiferenteBarra = False

    # só quebrar por espaços
    partes = s.split(' ')

    # erros ao longo da solução (lógica mais complexa que não funciona)
    #for c in s:
     #   if c == '+' or c == '-' or c == '*':
      #      partes = s.split(c)
       #     opDiferenteBarra = True

        #if c == '/' and not opDiferenteBarra:
         #   contBarras += 1
          #  if(contBarras == 2):
           #     partes = s.split(c)


    #f1 = partes[0].split(' / ')
    #f2 = partes[1].split(' / ')

    #n1 = int(f1[0])
    #d1 = int(f1[1])

    #n2 = int(f2[0])
    #d2 = int(f2[1])

    n1 = int(partes[0])
    d1 = int(partes[2])

    op = partes[3]

    n2 = int(partes[4])
    d2 = int(partes[6])

    if op == '+':
        resultadoNumerador = (n1 * d2 + n2 * d1)
        resultadoDenominador = (d1 * d2)

    elif op == '-':
        resultadoNumerador = (n1 * d2 - n2 * d1)
        resultadoDenominador = d1 * d2

    elif op == '*':
        resultadoNumerador = n1 * n2
        resultadoDenominador = d1 * d2

    elif op == '/':
        resultadoNumerador = n1 * d2
        resultadoDenominador = n2 * d1

    resultadoNumerador = str(resultadoNumerador)
    resultadoDenominador = str(resultadoDenominador)

    print(resultadoNumerador + "/" + resultadoDenominador + " =", end=" ")

    resultadoNumerador = int(resultadoNumerador)
    resultadoDenominador = int(resultadoDenominador)

    if resultadoDenominador < resultadoNumerador:
        if resultadoDenominador > -1:
            for i in range(resultadoDenominador, 0, -1):
                if resultadoDenominador % i == 0 and resultadoNumerador % i == 0:
                    resultadoNumerador /= i
                    resultadoDenominador /= i
                    i = -1
        
        else:
            for i in range(resultadoNumerador, 0, -1):
                if resultadoDenominador % i == 0 and resultadoNumerador % i == 0:
                    resultadoNumerador /= i
                    resultadoDenominador /= i
                    i = -1
                
    else:
        if resultadoNumerador > -1:
            for i in range (resultadoNumerador, 0, -1):
                if resultadoDenominador % i == 0 and resultadoNumerador % i == 0:
                    resultadoNumerador /= i
                    resultadoDenominador /= i
                    i = -1
            
        else:
            for i in range(resultadoDenominador, 0, -1):
                if resultadoDenominador % i == 0 and resultadoNumerador % i == 0:
                    resultadoNumerador /= i
                    resultadoDenominador /= i
                    i = -1

    resultadoNumerador = str(int(resultadoNumerador))
    resultadoDenominador = str(int(resultadoDenominador))

    print(resultadoNumerador + "/" + resultadoDenominador)