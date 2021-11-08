class hashTable:

    def __init__(self, taille):
        self.taille = taille
        self.hashTab = [[] for i in range(self.taille)]

    def hashage(self, key):
        return hash(key) % self.taille

    def ajouterItem(self,nom,cin):
        index=self.hachage(nom)
        self.hashTab[index].append([nom,cin])

    def afficherItem(self):
        for i in range(self.taille):
            if len(self.hashTab[i]) > 0:
                print("Index : ", i, "\n"
                      "Nom:",self.hashTab[i][0][0],"\n "
                      "CIN:", self.hashTab[i][0][1],"\n")

    def afficherItemParIndex(self, i):
        if len(self.hashTab[i]) == 1:
            print("\nIndex : ", i, "\nNom:",
                  self.hashTab[i][0][0], "\nTel:", self.hashTab[i][0][1], "\n")
        elif len(self.hashTab[i]) > 1:
            for j in range(len(self.hashTab[index])):
                print("\n Index : ", i, j, "\nNom:",
                      self.hashTab[i][j][0], "\nTel:", self.hashTab[i][j][1], "\n")
        else:
            print("no index found")

