class hashTable:

    def __init__(self, taille):
        self.taille = taille
        self.hashTab = [[] for i in range(self.taille)]

    def hashage(self, key):
        return hash(key) % self.taille





