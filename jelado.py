class Jel:
    def __init__(self,ora,perc,masodperc,x,y):
        self.ora=ora
        self.perc=perc
        self.masodperc=masodperc
        self.x=x
        self.y=y
    def mp(self):
        return int((self.ora*3600)+(self.perc*60)+self.masodperc)

def eltelt(ido1,ido2):
    return int(ido2-ido1)

def mpora(mp):
    return [int(mp/3600),int((mp%3600)/60),(mp%3600)%60]

f = open("jel.txt", "rt")

adatok = []

for sor in f:
    sor = sor.strip().split(" ")
    for i in range(len(sor)):
        sor[i] = int(sor[i])
    adatok.append(Jel(sor[0],sor[1],sor[2],sor[3],sor[4],))

sorszam = int(input("Adja meg a jel sorszámát: "))
if sorszam != 0:
    sorszam -= 1

print(f"x={adatok[sorszam].x} y={adatok[sorszam].y}")

teljes = mpora(eltelt(adatok[0].mp(),adatok[len(adatok)-1].mp()))


print("4. feladat")

print(f"Időtartam: {teljes[0]}:{teljes[1]}:{teljes[2]}")


print("5. feladat")

ballent = [adatok[0].x,adatok[0].y]
jobbfent = [adatok[0].x,adatok[0].y]


for jel in adatok:
    if jel.x < ballent[0]:
        ballent[0]=jel.x
    elif jel.x > jobbfent[0]:
        jobbfent[0]=jel.x
    if jel.y < ballent[1]:
        ballent[1]=jel.y
    elif jel.y > jobbfent[1]:
        jobbfent[1]=jel.y
    
print(f"Bal alsó: {ballent[0]} {ballent[1]}, jobb felső: {jobbfent[0]} {jobbfent[1]}")