lst = [1, 7, 3, 6, 7, 9, 2, 3]


def del_second_smallest_value(liste):
    liste2 = sorted(liste)
    liste.remove(liste2[1])


def del_odd_numbs(liste):
    index = 0
    stop = len(liste)
    while stop > index:
        if liste[index] % 2 == 1:
            liste.pop(index)
            stop -= 1
        else:
            index += 1


def count_to_x(x):
    for i in range(x):
        print(i, end=", ")
    print(x)


print(lst)
del_odd_numbs(lst)
print(lst)

count_to_x(6)


matrix = [
    [1, 2, 3, 4],
    [2, 3, 6, 8],
    [1, 0, 2, 5]
]


def take_values_from_matrix(mat):
    somme = 0
    for i in mat:
        for j in i:
            somme += j
    return somme


def take_values_from_matrix_but_better(mat):
    result = 0
    for i in mat:
        if type(i) == list:
            result += take_values_from_matrix_but_better(i)
        else:
            result += i
    return result


print(take_values_from_matrix_but_better(matrix))


def merge_sort(liste):
    if len(liste) == 1:
        return liste
    elif len(liste) == 2:
        return merge([liste[0]], [liste[1]])
    mid = len(liste) // 2 + 1
    left = liste[:mid]
    right = liste[mid:]

    merge_sort(left)
    merge_sort(right)

    return merge(left, right)


def merge(l1, l2):
    result = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
    result.extend(l1[i:])   
    result.extend(l2[j:])
    return result
