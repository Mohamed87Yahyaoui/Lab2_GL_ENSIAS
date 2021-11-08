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
        if len(self.hashTable[i]) == 1:
            print("Index : ", i, "\n"
                  "Nom:",self.hashTable[i][0][0], "\n"
                  "CIN:", self.hashTable[i][0][1], "\n")
        elif len(self.hashTable[i]) > 1:
            for j in range(len(self.hashTable[i])):
                print("Index : ", i, j, "\n"
                      "Nom:",self.hashTable[i][j][0], "\n"
                      "Tel:", self.hashTable[i][j][1], "\n")
        else:
            print("no index found")

