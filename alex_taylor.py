#3 création de la fonction
def saluer(nom):
    print("Bonjour ",nom)

#1&2 
nomUtilisateur=input("Rentrer un nom:")


continueBoucle=True

while continueBoucle==True:

    #Gestion de l'erreur si l'utilisateur ne rentre pas un nombre mais une chaine de caractère
    try:
        nbreUtilisateur=int(input("Rentrer un nombre entre 1 et 10:"))
        if nbreUtilisateur<1 or nbreUtilisateur>10:
            print("Veuillez rentrer un nom valide.")
        else:
            continueBoucle=False
    except ValueError:
        print("Désolé, la valeur saisie n'est pas un nombre.")
        pass

  

#4 appel de lafonction
nomExemple="Bernard"
saluer(nomExemple)

#5 boucle for

for i in range(nbreUtilisateur):
    print("Répétition",nbreUtilisateur,": Python c'est cool!")

