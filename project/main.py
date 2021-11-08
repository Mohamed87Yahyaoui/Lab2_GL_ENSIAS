from hashtable import *

def main():
    Tableau = hachage()

    Tableau.ajout_Elem("Ahmed", "J568452")
    Tableau.ajout_Elem("Sara", "A5642154")
    Tableau.ajout_Elem("Brahim", "D451234")

    Tableau.afficher_Elem()
    Tableau.afficher_Elem_Index(50)

    print(Tableau.chercher_elem("Ahmed")) # (Item; index; occurence)

    Tableau.supprimer_elem("Ahmed")
    print(Tableau.chercher_elem("Ahmed")) # L'item cherché est non trouve

    Tableau.nombreItems(50) # nombre d'item -1


if __name__ == "__main__":
    main()
