
class Noeud:

    def __init__(self, donnee, noeud_gauche=None, noeud_droit=None):
        self.donnee = donnee
        self.noeud_gauche = noeud_gauche
        self.noeud_droit = noeud_droit

    def est_feuille(self):
        return self.noeud_gauche is None and self.noeud_droit is None


def liste_noeuds(occurrences: dict) -> list:
    liste = [Noeud((char, freq)) for char, freq in occurrences.items()]
    return liste


def construire_arbre(occurrences: dict) -> Noeud:
    liste_noeuds = liste_noeuds(occurrences)
    # tri en fonction de la fréquence
    liste_noeuds.sort(key=lambda n: n.donnee[1])
    # tant que liste noeud a plus de 1 element :
    while len(liste_noeuds) > 1:
        n1 = liste_noeuds.pop(0)  # retourne le premier elt et le supprime de la liste
        n2 = liste_noeuds.pop(0)

        somme_occurrence = (None, n1.donnee[1] + n2.donnee[1])
        n = Noeud(somme_occurrence, n1, n2)
        # ajout du nouveau noeud a la liste
        liste_noeuds.append(n)
        # tri de la liste
        liste_noeuds.sort(key=lambda n: n.donnee[1])
    return liste_noeuds[0]


# tester la fonction  construire_arbre sur “si ton tonton tond mon tonton"
texte = "si ton tonton tond mon tonton"
occurrences = {}
for char in texte:
    if char in occurrences:
        occurrences[char] += 1
    else:
        occurrences[char] = 1

arbre = construire_arbre(occurrences)
print(arbre.donnee[0])
print(arbre.donnee[1])
print(arbre.noeud_gauche.donnee[0])
print(arbre.noeud_gauche.donnee[1])
print(arbre.noeud_droit.donnee[0])
print(arbre.noeud_droit.donnee[1])
print(arbre.noeud_gauche.noeud_gauche.donnee[0])  # affiche le premier caractere du texte