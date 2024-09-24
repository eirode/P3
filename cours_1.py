"""# Introduction au dictionnaires

dico = {
    "cat": "chat",
    "dog": "chien",
    "mouse": "souris"
}
# chercher un élément dans un dictionnaire
print(dico["dog"])
# ajouter un élément au dico
dico["cow"] = "vache"
# autre méthode
print(dico.get("monkey")) # pas d'erreur
# supp un élément d'un dico
del dico["cat"]
# boucle for donne les clés
for keys in dico:
    print(keys)
# donne les valeurs
for values in dico.values():
    print(values)
# items = clés + produit (tuple)
for items in dico.items():
    print(items)

dico2 = {}
# implémente le dico dans le dico2
dico2.update(dico)"""

# EXERCICES

eleves = {
    "Eline": (20, 18, 20),
    "Theo": (19, 17, 20),
    "Lucien": (19, 19, 19),
    "Pierre-Louis": (15, 12, 16),
    "Charlie": (6, 17, 12),
    "Louis": (10, 11, 6)
}


def calcul_moyenne(liste_eleve, eleve):
    notes = liste_eleve[eleve]
    tot = 0
    """for i in notes:
        tot += i""" # boucle équivalent sum()
    return sum(notes)/len(notes)


print(calcul_moyenne(eleves, "Charlie"))

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


def age_to_reste(liste_employes, age):
    for i in liste_employes.items():
        if i[1]["age"] == age:
            print(i[0])


age_to_reste(employes, 23)

perso = {
    "sante": 100,
    "force": 45,
    "dexterite": 21,
    "endurance": 87,
    "magie": 15
}


def add_perk_point(personnage):
    if personnage["sante"] < personnage["force"]/4:
        personnage["sante"] += 1
    elif personnage["dexterite"] < 22:
        personnage["dexterite"] += 1
    elif personnage["endurance"] < personnage["force"]/3:
        personnage["endurance"] += 1
    else:
        personnage["force"] += 1


print(perso)
add_perk_point(perso)
print(perso)