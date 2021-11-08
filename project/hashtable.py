class hashTable:

    def __init__(self, taille):
        self.taille = taille
        self.hashTab = [[] for i in range(self.taille)]

    def hashage(self, key):
        return hash(key) % self.taille

    def ajouterElem(self,nom,cin):
        index=self.hachage(nom)
        self.hashTab[index].append([nom,cin])

    def afficherElem(self):
        for i in range(self.taille):
            if len(self.hashTab[i]) > 0:
                print("Index : ", i, "\n"
                      "Nom:",self.hashTab[i][0][0],"\n"
                      "CIN:", self.hashTab[i][0][1],"\n")

    def afficherElemParIndex(self, i):
        if len(self.hashTab[i]) == 1:
            print("\nIndex : ", i, "\nNom:",
                  self.hashTab[i][0][0], "\nTel:", self.hashTab[i][0][1], "\n")
        elif len(self.hashTab[i]) > 1:
            for j in range(len(self.hashTab[index])):
                print("\n Index : ", i, j, "\nNom:",
                      self.hashTab[i][j][0], "\nTel:", self.hashTab[i][j][1], "\n")
        else:
            print("no index found")

    def chercherElem(self, nom):
        index = self.HASH(nom)
        Ind = 0
        for k in range(len(self.hashTab[i])):
            if nom == self.hashTab[index][k][0]:
                return (self.hashTab[i][k], i, k)
            else:
                Ind += 1
        if Ind == len(self.hashTab[index]):
            return "L'item cherché est non trouve"
        
        
    def supprimerItem(self, nom):
        if self.chercherItem(nom) == "L'élement cherché n'est pas trouvé":
            print("Element n'est pas existant")
        else:
            i = self.chercherItem(nom)[1]
            occurance_index = self.chercherItem(nom)[2]
            item_delete = self.hashTab[i].pop(occurance_index)
            print("l'element", item_delete, "est successivement supprimé")
