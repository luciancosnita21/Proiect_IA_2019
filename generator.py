
from owlready2 import *
import random
from random import shuffle

file=open("lista_intrebari.txt" ,"a")
file2=open("lista_cu_raspunsuri.txt" ,"a")

onto = get_ontology("file://C:/Users/Lucian/Desktop/USL4.owl").load()
#print(list(onto.properties()))
lista=list(onto.properties())
lista2=list(onto.classes())
aa=int(input("Numar intrebari cu variante multiple: "))
bb=int( input("Numar intrebari cu completare: "))
print(aa)
termen=random.choice(lista)

proprietati_folosite=[]

p=str(termen)
p2=p.split(".")[0]

p2=p2+"."

subiect=termen.domain[0]
obiect=termen.range[0]

#print(list(subiect.subclasses()))
file.write("Intrebari cu completare:\n")

file2.write("Intrebari cu completare:\n")
for i in range(bb):
    while termen in proprietati_folosite:
      termen = random.choice(lista)
    proprietati_folosite.append(termen)
    p3 = str(termen)
    p4 = p3.split(p2)[1]

    subiect = termen.domain[0]
    obiect = termen.range[0]
    lista_s=list(subiect.subclasses())
    lista_s.append(subiect)
    lista_o = list(obiect.subclasses())
    lista_o.append(obiect)
    print(lista_s)
    s1=random.choice(lista_s)
    o1 = random.choice(lista_o)
    s2=str(s1)
    o2=str(o1)
    s3=s2.split(p2)[1]
    o3=o2.split(p2)[1]
    file.write(s3+" "+p4+" ...\n")
    file2.write(s3 + " " + p4 +" "+ o3+"\n")

file.write("\n")
file.write("Intrebari cu variante multiple:\n")
file2.write("\n")
file2.write("Intrebari cu variante multiple:\n")

for i in range(aa):
    while termen in proprietati_folosite:
        termen = random.choice(lista)
    proprietati_folosite.append(termen)
    p3 = str(termen)
    p4 = p3.split(p2)[1]
    subiect = termen.domain[0]
    obiect = termen.range[0]
    lista_s = list(subiect.subclasses())
    lista_s.append(subiect)
    lista_o = list(obiect.subclasses())
    lista_o.append(obiect)
    print(lista_s)
    s1 = random.choice(lista_s)
    o1 = random.choice(lista_o)
    s2 = str(s1)
    o2 = str(o1)
    s3=s2.split(p2)[1]
    o3=o2.split(p2)[1]

    variante=list()
    variante.append(o3)

    asemanatoare=list()

    while len(asemanatoare)< 3:
          shuffle(lista2)
          cuvant= random.choice(lista2)
          c2 = str(cuvant)
          c3 = c2.split(p2)[1]
          if c3  not in asemanatoare and cuvant not in lista_s and cuvant not in lista_o:
             asemanatoare.append(c3)





    variante=variante+asemanatoare
    shuffle(variante)
    file.write(s3 + " " + p4 +" a."  +variante[0]+", b."  +variante[1] +", c."  +variante[2]  +", d." +variante[3] +".\n")



    file2.write(s3 + " " + p4 +" "+ o3+"\n")