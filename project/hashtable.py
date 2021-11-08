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

    def chercherElem(self, nom):
        index = self.HASH(nom)
        Ind = 0
        for i in range(len(self.hashTable[index])):
            if nom == self.hashTable[index][i][0]:
                return (self.hashTable[index][i], index, i)
            else:
                Ind += 1
        if Ind == len(self.hashTable[index]):
            return "element introuvable"
