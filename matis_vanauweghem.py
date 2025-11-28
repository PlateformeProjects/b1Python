nom = input("Entrez votre nom : ")

while True:
    try:
        n = int(input("Entrez un nombre entre 1 et 10 : "))
        if 1 <= n <= 10:
            break
        else:
            print("Le nombre doit être entre 1 et 10.")
    except ValueError:
        print("Veuillez entrer un nombre entier.")

def saluer(nom):
    print(f"Bonjour {nom}!")

saluer(nom)

for i in range(1, n + 1):
    print(f"répétition {i}: Python c'est cool !")

