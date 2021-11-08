class hashTable:

    def __init__(self, taille):
        self.taille = taille
        self.hashTab = [[] for i in range(self.taille)]

    def hashage(self, key):
        return hash(key) % self.taille

    def ajouterItem(self,nom,tel)
        index=self.hachage(nom)
        self.hashTable[index].append([nom,tel])



