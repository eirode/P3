"""n = int(input("nbr?\n"))

while n != 1:
    if n % 3 == 0:
        n //= 3
    else:
        n += 1
"""

"""l = [9, 7, 4, 0, 23]
a = 0

while a < len(l):
    print(l[a])
    a += 1"""

"""for i in range(20):
    if i % 3 == 0:
        continue
    print(i)"""

"""n = True
while n:
    n += 1
    print(n)
    if n == 100:
        break

else:
    print("else")"""

"""nbr = int(input("nbr?\n"))
tampon = 0

while nbr >= 1:
    tampon *= 10
    tampon += nbr % 10
    nbr //= 10

print(int(tampon))"""


"""def reverse_nbr(nbr):
    nbr = str(nbr)
    nbr = nbr[::-1]
    return int(nbr)


reverse_nbr(12345)"""


def generator(n=1, m=1):
    result = []
    for i in range(n):
        tmp = []
        for j in range(m):
            tmp.append(0)
        result.append(tmp)
    return result


def generator_but_better(n, m):
    return [[0 for i in range(m)] for j in range(n)]


print(generator_but_better(5, 5))
