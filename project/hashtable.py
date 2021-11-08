class hashTable:

    def __init__(self, taille):
        self.taille = taille
        self.hashTab = [[] for i in range(self.taille)]

    def hachage(self, key):
        return hash(key) % self.taille

    def ajout_Elem(self,nom,cin):
        index=self.hachage(nom)
        self.hashTab[index].append([nom,cin])

    def afficher_Elem(self):
        for i in range(self.taille):
            if len(self.hashTab[i]) > 0:
                print("Index : ", i, "\n"
                      "Nom:",self.hashTab[i][0][0],"\n"
                      "CIN:", self.hashTab[i][0][1],"\n")

    def afficher_Elem_Index(self, i):
        if len(self.hashTab[i]) == 1:
            print("Index : ", i, "\n"
                  "Nom:",self.hashTab[i][0][0], "\n"
                  "CIN:", self.hashTab[i][0][1], "\n")
        elif len(self.hashTab[i]) > 1:
            for j in range(len(self.hashTab[i])):
                print("Index : ", i, j, "\n"
                      "Nom:",self.hashTab[i][j][0], "\n"
                      "Tel:", self.hashTab[i][j][1], "\n")
        else:
            print("Aucun index trouvé")

    def chercher_elem(self, nom):
        index = self.HASH(nom)
        Ind = 0
        for k in range(len(self.hashTab[i])):
            if nom == self.hashTab[index][k][0]:
                return (self.hashTab[i][k], i, k)
            else:
                Ind += 1
        if Ind == len(self.hashTab[index]):
            return "Element introuvable"


    def supprimerItem(self, nom):
        if self.chercherItem(nom) == "L'élement cherché n'est pas trouvé":
            print("Element n'est pas existant")
        else:
            i = self.chercherItem(nom)[1]
            occurance_index = self.chercherItem(nom)[2]
            item_delete = self.hashTab[i].pop(occurance_index)
            print("l'element", item_delete, "est successivement supprimé")
