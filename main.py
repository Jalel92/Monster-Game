import os
from db_init import personnages, monstres
import random
from utils import *


def afficher_menu():
    #Effacer le contenu du terminal
    os.system('cls' if os.name == 'nt' else 'clear')
    #Afficher mon en-tête
    titre = "Jeu de combat"
    afficher_header(titre)
    #Afficher les choix possibles
    print("1. Démarrer une nouvelle partie")
    print("2. Afficher les 3 meilleurs scores")
    print("3. Quitter")

def nouvelle_partie() :
    #Afficher le pseudo 
    pseudo_joueur = str(input("Entrez votre pseudo : "))
    #Afficher la liste des personnages
    print("Voici la liste des personnages :")
    for i in range(len(personnages)) :
        print(f"{i}. {personnages[i]["name"]} | ❤️  ​PV : {personnages[i]["PV"]} | ⚔️  ​ATK : {personnages[i]["ATK"]} | 🛡️  ​DEF : {personnages[i]["DEF"]}") #ne pas oulblier de rajouter leurs caractéristiques
    # Récupere les personnages et vérifie les réponses
    rep1 = int(input("Entrez le numéro du premier personnage : "))
    if rep1 not in (0,1,2,3,4,5,6,7,8,9) :
        raise ValueError("Veuillez entrez un chiffre correct !")

    rep2 = int(input("Entrez le numéro du deuxième personnage : "))
    if rep2 not in (0,1,2,3,4,5,6,7,8,9) :
        raise ValueError("Veuillez entrez un chiffre correct !")
    
    rep3 = int(input("Entrez le numéro du troisième personnage : "))
    if rep3 not in (0,1,2,3,4,5,6,7,8,9) :
        raise ValueError("Veuillez entrez un chiffre correct !")
    
    team = [personnages[rep1]["name"],personnages[rep2]["name"],personnages[rep3]["name"]]
    # Sélection du nom de l'équipe
    print(f"Voici ton équipe ! : {team}")
    nom_team = str(input("Trouve lui un nom ! : "))
    # Choix aléatoire du montre
    monstre = random.choice(monstres)
    afficher_header(f"L'équipe {nom_team} affronteront le monstre {monstre['name']} (⚔️  ATK : {monstre['ATK']} | 🛡️  DEF : {monstre['DEF']} | ❤️  PV : {monstre['PV']})")


def main() :
    afficher_menu()
    choix_joueur = int(input("Entrez un choix : "))
    if choix_joueur not in (1,2,3) :
        raise ValueError("Veuillez entrez un chiffre correct !")
    #Option 1 : Démarrer une nouvelle partie
    elif choix_joueur == 1 :
        nouvelle_partie()
    #Option 2  : Affiche les 3 meilleurs scores
    elif choix_joueur == 2 :
        pass
    #Option 3 : Quitter
    else :
        print("À bientot !")
        os.system('cls' if os.name == 'nt' else 'clear')

main()
    


    