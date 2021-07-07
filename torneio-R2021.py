
#grupo_1 = 5 OR 6 jogos ganhos
#grupo_2 = 3 OR 4 jogos ganhos
#grupo_3 = 1 OR 2 jogos ganhos
#Sem jogos ganhos, sem convite para treino

player = 6
match = []

for i in range(6) :
    v: str = input()
    if v == 'V':
         match.append("{}".format(v))

total = len(match)
if total == 1 or total == 2:
    print(3)
elif total == 3 or total == 4:
    print(2)
elif total == 5 or total == 6:
    print(1)
else:
    print(-1)