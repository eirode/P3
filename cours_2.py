import math
import pprint
"""dico = {
    "Eline": (20, 18, 20),
    "Theo": (19, 17, 20),
    "Lucien": (19, 19, 19),
    "Pierre-Louis": (15, 12, 16),
    "Charlie": (6, 17, 12),
    "Louis": (10, 11, 6)
}


for item in dico.items():
    print(item)"""

"""dico = {
    1: 25,
    2: 14,
    3: 63,
    4: 51,
    5: 73,
    6: 11
}

for key in dico.keys():
    if (key % 2) == 0:
        print(f"{key}: {dico[key]}")"""

"""dico = {}

demande = input("combien de chiffres?\n")
for i in range(1, int(demande) + 1):
    dico[i] = i**2

print(dico)"""

"""prod = 1
dico = {
    1: 25,
    2: 14,
    3: 63,
    4: 51,
    5: 73,
    6: 11
}

for value in dico.values():
    prod = prod * value

print(prod)"""

"""dico = {
    1: 25,
    2: 14,
    3: 63,
    4: 51,
    5: 73,
    6: 11
}


maxi = 1
mini = 1
for item in dico.items():
    print(item[1])
    if item[1] > dico[maxi]:
        maxi = item[0]
    if item[1] < dico[mini]:
        mini = item[0]

print(f"le plus grand nombre est {dico[maxi]} avec la clef {maxi}")
print(f"le plus petit nombre est {dico[mini]} avec la clef {mini}")"""

"""dico = {
    1: ['a', 'b', 'c', 'd'],
    2: ['e', 'f', 'g', 'h']
}

for i in dico[1]:
    for j in dico[2]:
        print(f"{i},{j}")"""

"""dico = {
    
}


def ajout_personne(dicti):
    prenom = input("quel est le prenom?\n")
    nom = input("quel est le nom?\n")
    age = input("quel est son âge?\n")
    genre = input("quel est le genre?\n")
    
    dico[prenom] = [nom, int(age), genre]
    
    
print(dico)
ajout_personne(dico)"""

"""dico = {
    "francais": 2,
    "histoire": 20,
    "math": 16
}

del dico["math"]
dico["algebre"] = 15
dico["stats"] = 18
dico["analysis"] = 5


def dico_index(dictio, index):
    lst = []
    for key in dictio.keys():
        lst.append(key)
    return lst[index]


print(dico_index(dico, 0))"""

"""dico = {
}

if len(dico) == 0:
    print("vide")
else:
    print("pas vide")"""

employes = {
    0: {
        "nom": "Tom",
        "prenom": "Mcguire",
        "age": 27
    },
    1: {
        "nom": "Tobby",
        "prenom": "Holland",
        "age": 23
    },
    2: {
        "nom": "John",
        "prenom": "Book",
        "age": 35
    },
    3: {
        "nom": "Michel",
        "prenom": "Authem",
        "age": 54
    }
}


def extract(dicti, key_value):
    for i in dicti.keys():
        for j in dicti[i].items():
            if j == key_value:
                return i


print(extract(employes, ("nom", "John")))
