#Problema:De uma cadeia de inteiros, retorne a soma de todos eles.
#   Quando houver um zero na cadeia, 'ignore' o último número corrente

#Entrada: Primeiro um inteiro N = quantidade de números Xi a serem inseridos
#Saída: Uma linha contendo a soma dos números, onde 0 significa erro

#Restrições:
#   1 <= N <= 100.000
#   0 <= Xi <= 100, para(1<=i<=N)
#   0 <= resultado <= 1.000.000

N = int(input())
chain = []
for i in range(N):
    Xi = int(input())
    if Xi == 0:
        chain.pop()
    else:
        chain.append(Xi)

print(sum(chain))