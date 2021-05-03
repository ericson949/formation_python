import os
import random
import time
from math import ceil as ceil


def couleur(case:int) -> str:
    return ('noire','rouge')[case%2==0]

def lancer_bille() -> int:
    return random.randint(0,50)
    
def verifier(case, bille) -> int:
    if case == bille :
        print("!!! Bravo vous avez trouvé la bonne Case !!!")
        return 3
    elif couleur(case) == couleur(bille):
        print("!! Bravo vous avez obtenu la meme couleur que la case !!")
        return 2
    print("§§§§ Desolé mais vous avez perdu §§§§")
    return 0
def entrer_mise(credit) ->int:
    mise = 0
    while mise not in range(1, credit+1) :
        mise = int(input("entrer la valeur de votre paris : "))
        if (mise < credit):
            return mise
        print(f'votre mise: {mise} est superieur a votre credit: {credit}')
        

def jouer(credit:int) -> None:
    while credit in range(1,100000) : 
        try :
            case = int(input("choissisez une mise entre 0-49 : "))
            if case not in range(0,50):
                print("casse non valide")
                continue
            print(f'Vous avez choisit la case: {case} de couleur:  {couleur(case)}')
            mise = entrer_mise(credit)
            credit -= mise
            print(f'Votre Paris :\n\tcase: {case} ; couleur : {couleur(case)}\n\tmise: {mise}\nNouveau solde: {credit}')
            print("###### le croupier va lancer la bille ######")
            time.sleep(5)
            bille = lancer_bille()
            veri = verifier(case, bille)
            print(f"#### la bille c'est arreté sur la case: {bille} ; de couleur: {couleur(bille)} #####")
            if veri == 3:
                msg = f'vous avez gagné : {veri*mise} Points'
                credit += veri*mise
            elif veri == 2:
                msg = f'vous avez gagné : {ceil(mise/veri)} points'
                credit += ceil(mise/veri)
            else:
                msg = f'Vous avez Perdu : {mise} points'
            print(msg)
            print(f'Votre nouveau solde est : {credit} points')
        except ValueError:
            print("impossible de convertir le nombre")
    if (credit < 1) :
        print("Votre credit est epuisé")
    else :
        print("Bravo vous avez Depouillé le casino.")
    print("#### Game Over ####")

if __name__ == "__main__":
    print('#### Bienvenu sur le mini-casino by ericson949 ####')
    print('\tVous partez avec 100 points à la base')
    print('\tVotre objectif est de battre le casino')
    print('\t\tPour cela vous devez atteindre 100000 points')
    print('\t\tvous perdez si votre solde descend à 0')
    print('#############################################')
    jouer(100)