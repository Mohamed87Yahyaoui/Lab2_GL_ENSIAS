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
        for index in range(self.taille):
            if len(self.hashTable[index]) > 0:
                print("--------------\nIndex : ", index, "\nNom:",
                      self.hashTable[index][0][0], "\nTel:", self.hashTable[index][0][1], "\n--------------")

    def afficherItemParIndex(self, i):
        if len(self.hashTable[i]) == 1:
            print("--------------\nIndex : ", i, "\nNom:",
                  self.hashTable[i][0][0], "\nTel:", self.hashTable[i][0][1], "\n--------------")
        elif len(self.hashTable[i]) > 1:
            for j in range(len(self.hashTable[index])):
                print("--------------\n Index : ", i, j, "\nNom:",
                      self.hashTable[i][j][0], "\nTel:", self.hashTable[i][j][1], "\n--------------")
        else:
            print("no index found")

