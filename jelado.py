class Jel:
    def __init__(self,ora,perc,masodperc,x,y):
        self.ora=ora
        self.perc=perc
        self.masodperc=masodperc
        self.x=x
        self.y=y

f = open("jel.txt", "rt")

adatok = []

for sor in f:
    sor = sor.strip().split(" ")
    adatok.append(Jel(sor[0],sor[1],sor[2],sor[3],sor[4],))