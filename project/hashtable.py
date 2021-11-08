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

