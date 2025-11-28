# b1Python
def saluer():
    nom = input("Entrez votre nom : ")
    
    while True:
        try:
            nombre = int(input("Entrez un nombre entre 1 et 10 : "))
            if 1 <= nombre <= 10:
                print(f"Bonjour (nom), vous avez choisi le nombre (nombre).")
                break  
            else:
                print("Erreur : le nombre doit être entre 1 et 10. Veuillez réessayer.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    for i in range(nombre):
       print("repetition: Python c'est cool" ,nombre)
saluer()

