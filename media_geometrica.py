import math


nota = []
multiplicanotas = 1
entrada = 0
while entrada != '!':
    	entrada  = input('Digite nota: ')
    	if entrada != '!':
    		nota.append(int(entrada))
    	
    		
for x in range(0, len(nota)):
	multiplicanotas = multiplicanotas*nota[x]

		
media = math.pow(multiplicanotas, (1/len(nota)))
print(media)
