#!/usr/bin/python3

class DictionnaireOrdonne:

    def __init__(self, base={}, **donne):
        self.cles = []
        self.valeur = []
        if type(base) not in (dict, DictionnaireOrdonne):
            raise TypeError("le type attendu est un dictionnaire (usuel ou ordonne)")
        for cle in base:
            self.cles.append(cle)
            self.valeur.append(base[cle])
        for cle in donne:
            self.cles.append(cle)
            self.valeur.append(donne[cle])

    def __str__(self):
        string = "{"
        i = 0
        while (i < len(self.cles)):
            if (i != 0):
                string += ", "
            string += str(self.cles[i]) + ": " + str(self.valeur[i])
            i += 1
        string += "}"
        return string
    
    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.cles)

    def __contains__(self, cle):
        return cle in self.cles
    
    def __getitem__(self, cle):
        if (cle in self.cles):
            i = self.cles.index(cle)
            return self.valeur[i]

    def __setitem__(self, cle, valeur):
        if (cle in self.cles):
            i = self.cles.index(cle)
            self.valeur[i] = valeur
        else:
            self.cles.append(cle)
            self.valeur.append(valeur)

    def __delitem__(self, cle):
        if (cle in self.cles):
            i = self.cles.index(cle)
            del self.cles[i]
            del self.valeur[i]

    def sort(self):
        cle_trier = sorted(self.cles)
        valeur = []
        for cle in cle_trier:
            i = self.cles.index(cle)
            valeur.append(self.valeur[i])
        self.cles = cle_trier
        self.valeur = valeur

    def __add__(self, other):
        if type(other) not in (dict, DictionnaireOrdonne):
            raise TypeError("le type attendu est un dictionnaire (usuel ou ordonne)")
        for cle in other:
            self.cles.append(cle)
            self.valeur.append(other[cle])
    
    def __iter__(self):
        return iter(self.cles)

    def reverse(self):
        self.cles.reverse()
        self.valeur.reverse()

    def keys(self):
        return list(self.cles)
    
    def values(self):
        return list(self.valeur)

    def items(self):
        for i, cle in enumerate(self.cles):
            valeur = self.valeur[i]
            yield (cle, valeur)


