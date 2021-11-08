from hashtable import *

def main():
    Tableau = HashTable()

    Tableau.ajouterItem("Ahmed", "J568452")
    Tableau.ajouterItem("Sara", "A5642154")
    Tableau.ajouterItem("Brahim", "D451234")

    Tableau.afficherItem()
    Tableau.afficherItemParIndex(50)

    print(Tableau.chercherItem("Ahmed")) # (Item; index; occurence)

    Tableau.supprimer_elem("Ahmed")
    print(Tableau.chercher_elem("Ahmed")) # L'item cherché est non trouve

    Tableau.nombreItems(50) # nombre d'item -1


if __name__ == "__main__":
    main()
