import math

qtdnotas = int(input('Digite um número: '))

nota = []
multiplicanotas = 1

for i in range(0, qtdnotas):
    	nota.append(int(input('Digite nota: ')))
    		
for x in range(0, qtdnotas):
	multiplicanotas = multiplicanotas*nota[x]


		
media = math.pow(multiplicanotas, (1/qtdnotas))
print(media)
