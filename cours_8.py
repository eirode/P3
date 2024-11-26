lst = ["chien", "chat", "oiseau", "zebre"]
dico = {}

for i in range(len(lst)):
    dico[lst[i]] = len(lst[i])

print(dico)


def search_longest_word(dictionnaire):
    return max(dictionnaire, key=len)


def search_longest_word_no_max(dictionnaire):
    longest = ""
    for keys in dictionnaire.keys():
        if len(keys) > len(longest):
            longest = keys
    return longest


print(search_longest_word(dico))
print(search_longest_word_no_max(dico))

matrix = [[3, 7, 0], [0, 1, 5], [0, 9, 5, 9, 2, 3]]


def clean_the_matrix(matrice):
    longest = len(max(matrice, key=len))
    for i in matrice:
        long = len(i)
        for j in range(longest-long):
            i.append(0)
    for i in matrice:
        print(i)
    return matrice


print(clean_the_matrix(matrix))

