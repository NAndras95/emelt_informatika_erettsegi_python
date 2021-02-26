#!/usr/bin/python

print("1. feladat")
adatok = []
file=open("tavirathu13.txt")
adatok=[line.rstrip('\n') for line in file]

#print(adatok)
print("2. feladat")
print("adjon meg egy varos kodot:")
kod=input()
#print("megadott kod: "+str(kod))

utolso = 0

for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')
    if(sordb[0] == kod):
        utolso=sordb[1]

print("utolso adat idopont: "+str(utolso))

print("3. feladat")
mini = 0
maxi = 100
for i in range(0, len(adatok)):
    sordb=adatok[i].split(' ')

    print(sordb[3]) #tesztelés

    if(int(sordb[3]) < int(mini)):
        mini=int(sordb[3])

    if(int(sordb[3]) > int(maxi)):
        maxi=int(sordb[3])

print("minimum: "+str(mini)+"\nmaximum: "+str(maxi))