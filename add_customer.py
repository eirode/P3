import shelve


def add_a_customer():
    customers = shelve.open("customers")
    nbr = len(customers)+1
    customers[str(nbr)] = {
        "last_name": input("le nom du client").upper(),
        "first_name": input("le prénom du client").upper(),
        "postal_code": input("le code postal du client").upper(),
        "age": input("âge du client (facultatif)").upper()
    }
    print(f"le numéro client est {nbr}")
    customers.close()


def find_customers():
    customers = shelve.open("customers")
    nom = input("quel est le nom du client?\n").upper()
    prenom = input("quel est le prénom du client?\n").upper()
    for item in customers.items():
        if (item[1]["first_name"] == prenom) and (item[1]["last_name"] == nom):
            customers.close()
            return item[0]


def change_customers_info():
    customers = shelve.open("customers", writeback=True)
    num = input("quel est le numéro client? (find si inconnu)\n").upper()
    if num == "find":
        num = find_customers()
        print(f"numéro client trouvé! : {num}")
    info_a_changer = input("quelle est l'info a changer?\n"
                           "-last name\n"
                           "-first name\n"
                           "-postal code\n"
                           "-age\n").upper()
    print(f"la valeur actuelle pour : {info_a_changer} est : {customers[num][info_a_changer]}")
    nouvelle = input("par quoi faut-il modifier cette info?\n").upper()
    # customers[num].pop(info_a_changer)
    customers[num][info_a_changer] = nouvelle
    print(customers[num])
    print(f"la nouvelle valeur pour : {info_a_changer} est : {customers[num][info_a_changer]}")
    customers.close()


def find_customer_info():
    customers = shelve.open("customers")
    num = find_customers()
    print(f"les infos du client sont :\n{customers[num]}")


action = input("que voulez-vous faire?\n"
               "ajouter\n"
               "chercher_numero\n"
               "modifier\n"
               "chercher_info\n")

if action == "ajouter":
    add_a_customer()
elif action == "chercher_numero":
    print(f"Le numéro client recherché est : {find_customers()}")
elif action == "modifier":
    change_customers_info()
elif action == "chercher_info":
    find_customer_info()
else:
    print("pas bon mon frerz")
