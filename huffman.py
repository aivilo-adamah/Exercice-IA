import math
from collections import Counter


# 1 : Entropie d'un texte 


def compter_occurrences(texte: str) -> dict:
    
    # initialisation d'un dictionnaire vide pour stocker les occurrences
    occurrences = {}
    
    # Parcoure chaque caractère du texte
    for caractere in texte:
        # Si le caractère est déjà dans le dictionnaire, on incrémente son compteur
        if caractere in occurrences:
            occurrences[caractere] += 1
        else:
            # Sinon, on l'ajoute au dictionnaire avec une occurrence initiale de 1
            occurrences[caractere] = 1
    
    return occurrences





def compter_occurrences_count(texte: str) -> dict:
    return {caractere: texte.count(caractere) for caractere in set(texte)}





# Exemple 
texte = "hello world"

# Appel de la fonction

# resultat = compter_occurrences(texte)
resultat =compter_occurrences_count(texte)

# Affichage du résultat
print("Occurrences de chaque caractère :")
for caractere, occurrence in resultat.items():
    print(f"'{caractere}': {occurrence}")



# m´ethode calculant l’entropie d’un texte (pass´e en param`etre). 
    

    def entropie(texte: str) -> float:
        # Compte les occurrences de chaque caractère
        occurrences = compter_occurrences_count(texte)
        probabilites = [occurrences[x]/len (texte) for x in occurrences]
        # Calcul de l'entropie
        entropie = -sum([p * math.log2(p) for p in probabilites])
        return entropie

 





"""
def entropie(texte):
    # Compte les occurrences de chaque caractère
    compteur = Counter(texte)
    
    # Calcule la probabilité d'apparition de chaque caractère
    probabilites = [compteur[x] / len(texte) for x in compteur]
    
    # Calcule l'entropie

    entropie = - sum([p * math.log2(p) for p in probabilites])
    
    return entropie

    
"""
# Exemple d'utilisation
texte = "si ton tonton tond mon tonton"
entropie_texte = entropie(texte)
print("Entropie du texte :", entropie_texte)

resultat = compter_occurrences_count(texte)
print(resultat)



# 2 : Codage de huffman




