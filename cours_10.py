def how_many_of_a_word_in_file(file, word):
    f = open(file, "r")
    inside = f.read()
    f.close()
    return inside.count(word)


def how_many_words_in_file(file):
    f = open(file, "r")
    inside = f.read()
    f.close()
    return inside.count(" ") + 1

def func(file):
    return how_many_of_a_word_in_file(file, " ") + 1


def list_to_file(lst):
    f = open("list file.txt", "w")
    f.writelines(lst)
    f.close()


def patern(n):
    f = open("patern.txt", "w")
    first_half = ""
    second_half = ""
    mid = f"{n*'-'+3*' '}\n"
    for i in range(n):
        # f.write(f"{i*'-'}{3*' '}{(n-i)*'-'}\n")
        first_half += f"{i*'-'}{3*' '}{(n-i)*'-'}\n"
        second_half = f"{i*'-'}{3*' '}{(n-i)*'-'}\n" + second_half
    """for i in range(n+1):
        f.write(f"{(n-i)*'-'}{3*' '}{i*'-'}\n")"""
    f.write(first_half+mid+second_half)
    f.close()



"""print(how_many_of_a_word_in_file("text.txt", "suis"))
print(how_many_words_in_file("text.txt"))
l = ["bonjour", "hello", "hola"]
list_to_file(l)"""
patern(23)
