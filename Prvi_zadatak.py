#UNOS
d = open('datoteka', 'w')
d.write(input("Unesi zeljene radnje s robotom: "))

d=open('datoteka')
line = d.readline()
lista = line.split(' ')

#NAREDBE OD PRVOG PLACE
j=0
for i in range(len(lista)):
    if (lista[i] == 'PLACE'):
        j = i
        break

#IZVRSAVANJE SVIH UVJETA
for j in range(len(lista)):
    if (lista[j] == 'PLACE'):
        sporedna = lista[j+1]
        sporedna = sporedna.split(',')
        x = int(sporedna[0])
        y = int(sporedna[1])
        f = sporedna[2]
        pomocna = f
    elif (lista[j] == 'MOVE'):
        if (pomocna == 'NORTH') and (y < 5): y = y + 1
        elif (pomocna == 'SOUTH') and (y > 0): y = y - 1
        elif (pomocna == 'EAST') and (x < 5): x = x + 1
        elif (pomocna == 'WEST') and (x > 0): x = x - 1
    elif (lista[j] == 'LEFT'):
        if (f == 'NORTH'): pomocna = 'WEST'
        if (f == 'WEST'): pomocna = 'SOUTH'
        if (f == 'SOUTH'): pomocna = 'EAST'
        if (f == 'EAST'): pomocna = 'NORTH'
    elif (lista[j] == 'RIGHT'):
        if (f == 'NORTH'): pomocna = 'EAST'
        if (f == 'WEST'): pomocna = 'NORTH'
        if (f == 'SOUTH'): pomocna = 'WEST'
        if (f == 'EAST'): pomocna = 'SOUTH'


#ISPIS
d = open('datoteka', 'w')
d.write("PLACE ")
d.write(str(x))
d.write(",")
d.write(str(y))
d.write(",")
d.write(pomocna)
d=open('datoteka')
print(d.readline())


