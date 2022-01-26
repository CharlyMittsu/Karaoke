#__Initialisation
import cProfile
from pickle import TRUE
import random
album = 5 #nombre de chanson

#__Classes
class Joueur :
    def __init__(self,pseudo):
        self.__pseudo= pseudo
        #self.__score[0]=0
        #self.__score[1]=0
        #self.__score[2]=0
        #self.__score[3]=0
        #self.__score[4]=0
        for i in range (album):
            self.score[i]=0

    def getPseudo(self):
        return self.__pseudo
    def score(self,entier,chanson):
        if self.score[chanson] < entier :
            self.score[chanson] = entier
        return self.score[chanson]
    def getMoyenne(self):
        moyenne = 0
        compte = 0
        for i in range (album):
            if self.score[i] !=0:
                moyenne+=self.score[i]
                compte+= 1
        moyenne=moyenne/compte
        return moyenne
    def getBest(self):
        memoire = 0
        for i in range (album):
            if self.score[i] >memoire:
                memoire = self.score[i]
        return memoire
    def getWorst(self):
        memoire = self.getBest()
        for i in range (album):
            if self.score[i] <memoire and self.score[i] !=0 :
                memoire = self.score[i]
        return memoire

#__Jeu
#____initialisation
choix = 0
party = []
game = True
while game == True:
    while choix<1 or choix>3:
        print ("Veuillez choisir entre ")
        print ("(1):Créer un nouveau joueur ")
        print ("(2):Enlever un joueur de la partie ")
        print ("(3):Lancer une musique ")
        choix = int(input())
        if not(party):
            if choix == 2 or choix == 3:
                print("Il n'y a aucun joueur enregistrée pour le moment.")
                choix = 0
    #____Création de perso
    while choix == 1:
        cPerso = 0
        while cPerso <1 or cPerso >2:
            cPerso = int(input("(1): créer un nouveau joueur (2): revenir au menu principal"))
        if cPerso==1:
            party.append (Joueur(input("Choisissez votre pseudo")))
            print("Bienvenue ",party[-1].getPseudo())
        if cPerso == 2:
            choix = 0
    #____Annihilation sans scrupule de perso
    while choix == 2:
        cPerso = 0
        while cPerso <1 or cPerso >2:
            if not (party):
                "Il n'y a plus de joueur à supprimer, vous revenez au menu principal."
                cPerso = 2
            else:
                cPerso = int(input("(1): pour supprimer un joueur (2): revenir au menu principal"))
                if cPerso==1:
                    for i in range (len(party)):
                        print ("(",i,")",party[i].getPseudo())
                    suppr=int(input("Entrez le numéro du joueur que vous voulez retirer."))
                    if suppr not in range(len(party)):
                        print("choix invalide, retour au menu principal.")
                        cPerso =2
                    else :
                        print(party[suppr].getPseudo()," a été enlevé de la partie.")
                        del party[suppr]

            
        if cPerso == 2:
            choix = 0
    #____Jeu
    while choix == 1:
        cPerso = 0
        while cPerso <1 or cPerso >2:
            cPerso = int(input("(1): Lancer une chanson (2): revenir au menu principal (3): tableau des scores"))
        if cPerso==1:
            cMusique = -1
            while cMusique not in range (album):
                cMusique=int(input("choisissez une musique"))
            for i in range (party):
                score = int(input("entrez le score de ",party[i].getPseudo()))
                party[i].score(score,cMusique)
        if cPerso == 2:
            choix = 0
        if cPerso == 3:
            for i in range (party):
                print (party[i].getPseudo())
                print('meilleur score : ',party[i].getBest())
                print('pire score : ',party[i].getworst())
                print('moyenne score : ',party[i].getMoyenne())
                print("__________")