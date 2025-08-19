# Problema 2 – Căutare liniară (15p)

def cautare_liniara(lista,element):
    for i in range(len(lista)):
        if lista[i]==element:
            return i   #returneaza indexul
        else:
            return -1   #returneaza -1 daca nu a fost gasit

#Exemplu:
lista=[4,9,3,5,7,10]
pozitie_element=cautare_liniara(lista,9)
print("Pozitia elementului 9 este:",pozitie_element)
   #output: -1   (nu inteleg de ce )
