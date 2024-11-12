"""x = float(input("nombre\n"))

print(-2*x**4+3*x**3+2*x**2-7*x+4)"""

time = int(input("cmb de secondes?\n"))

time %= 86400

h = time//3600
hreste = time%3600
minu = hreste//60
minureste = hreste%60
sec = minureste
print(f"il est {h}heures, {minu}minutes et {sec}secondes")

"""lst1 = [1, 2, 3, 4, 5]
lst2 = list()
lst3 = list()

for i in lst1:
    lst2.append(i**2)

for i in range(len(lst1)):
    lst3.append(lst1[i]**2)

print(lst1)
print(lst2)
print(lst3)"""

"""lst = list()
for i in range(1000, 2501):
    if (i % 7 == 0) and (i % 5 != 0):
        lst.append(i)

print(str(lst)[1: -1])"""
