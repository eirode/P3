import os
# v = input("nbr ")

"""while not v.isdecimal():
    print("beteee")
    v = input("nbr ")
v = int(v)
print(f"moitié : {v/2}")"""
"""var = True
while var:
    try:
        v = int(input("nbr "))
        print(f"moitié : {v / 2}")
        var = False
    
    except:
        print("beteee")"""

"""try:
    v = int(input("nbr "))
    print(f"moitié : {5/v}")

except Exception as err:
    print(f"erreur : {err}")
"""
"""except ZeroDivisionError:
    print("division par 0 imp")
except ValueError:
    print("pas un chiffre")

open("txt", "a")"""

while True:
    try:
        v = int(input("entre un nombre :\n"))
    except ValueError:
        print(f"la valeur donnée n'est pas un nombre")
    else:
        if v > 0:
            print(f"le nombre {v} est positif")
        elif v < 0:
            print(f"le nombre {v} est négatif")
        else:
            print(f"le nombre {v} est nul")
        break




"""def divide(a=None, b=None):
    try:
        return int(a)/int(b)
    except ZeroDivisionError:
        return "division par zero"
    except ValueError:
        return "au moins une des deux valeurs n'est pas un nbr entier"
        

c = input("nbr 1 ")
d = input("nbr 2")
print(divide(c, d))"""
