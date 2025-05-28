#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
from termcolor import colored

joueurSuivant = -1
score1=0
score2=0

def getCopieJeu(jeu):
    """ jeu->jeu
        Retourne une copie du jeu passe en parametre
        Quand on copie un jeu on en calcule forcement les coups valides avant
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    coups_possibles = getCoupsValides(jeu)

    return copy.deepcopy(plateau), joueur_courant, coups_possibles, coups_joues, (score1, score2)

def finJeu(jeu):
    """ jeu -> bool
        Retourne vrai si c'est la fin du jeu
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return (coups_possibles != None and len(coups_possibles) == 0)

def getCoupsValides(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups valides dans le jeu passe en parametre
        Si None, alors on met � jour la liste des coups valides
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu

    coups_valides = list()
    for i in range(8):
        for j in range(8):
            for dir_ligne in range(-1, 2):
                for dir_colonne in range(-1, 2):
                    if not (dir_ligne == 0 and dir_colonne == 0) :
                        if estValideInDirFromPos(jeu, i, j, dir_ligne, dir_colonne):
                            if (i,j) not in coups_valides:
                                coups_valides.append((i, j))
    return coups_valides


def coupValide(jeu,coup):
    """jeu*coup->bool
        Retourne vrai si le coup appartient a la liste de coups valides du jeu
   """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return coup in coups_possibles

def joueCoup(jeu,coup,sim=False):
    """jeu*coup->void
        Joue un coup a l'aide de la fonction joueCoup defini dans le module game
        Hypothese:le coup est valide
        Met tous les champs de jeu à jour (sauf coups valides qui est fixée à None)
    """
    def retournerPion(dir_ligne, dir_colonne):
        i, j = coup

        i += dir_ligne
        j += dir_colonne
        while plateau[i][j] != joueur_courant:
            plateau[i][j] = joueur_courant
            i += dir_ligne
            j += dir_colonne

    if sim :
        jeu = getCopieJeu(jeu) # plateau deep-copie

    plateau, joueur_courant, coups_possibles, coups_joues, (scr1, scr2) = jeu

    for dir_ligne in range(-1, 2):
        for dir_colonne in range(-1, 2):
            if not (dir_ligne == 0 and dir_colonne == 0):
                if estValideInDirFromPos(jeu, coup[0], coup[1], dir_ligne, dir_colonne):
                    retournerPion(dir_ligne, dir_colonne)
    plateau[coup[0]][coup[1]] = joueur_courant

    if not sim :
        global score1
        score1 = 0
        global score2
        score2 = 0
        for i in range(8):
            for j in range(8):
                if plateau[i][j] == 1:
                    score1 += 1
                elif plateau[i][j] == 2:
                    score2 += 1

    else :
        simScore1 = 0
        simScore2 = 0
        for i in range(8):
            for j in range(8):
                if plateau[i][j] == 1:
                    simScore1 += 1
                elif plateau[i][j] == 2:
                    simScore2 += 1
        return plateau, joueur_courant, list(), coups_joues + [coup], (simScore1, simScore2)

def initialiseJeu():
    """ void -> jeu
        Initialise le jeu (nouveau plateau, liste des coups joues vide, liste des coups valides None, scores a 0 et joueur = 1)
    """
    coups_joues = list()
    coups_possibles = None
    plateau = [[0]*8 for i in range(8)]
    plateau[3][3] = 1
    plateau[4][4] = 1
    plateau[3][4] = 2
    plateau[4][3] = 2

    return plateau, 1, coups_possibles, coups_joues, (0, 0)

def getGagnant(jeu):
    """jeu->nat
    Retourne le numero du joueur gagnant apres avoir finalise la partie. Retourne 0 si match nul
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    if score1 == score2: return 0
    if score1 > score2 : return 1
    return 2

def affiche(jeu):
    """ jeu->void
        Affiche l'etat du jeu de la maniere suivante :
                 Coup joue = <dernier coup>
                 Scores = <score 1>, <score 2>
                 Plateau :

                         |       0     |     1       |      2     |      ...
                    ------------------------------------------------
                      0  | <Case 0,0>  | <Case 0,1>  | <Case 0,2> |      ...
                    ------------------------------------------------
                      1  | <Case 1,0>  | <Case 1,1>  | <Case 1,2> |      ...
                    ------------------------------------------------
                    ...       ...          ...            ...
                 Joueur <joueur>, a vous de jouer

         Hypothese : le contenu de chaque case ne depasse pas 5 caracteres
    """
    def souligne():
        return "-"*49 + "\n"
    def intercale(v):
        return " {:>2} |".format(v)
    def symbole(x):
        if x == 1: return 'O'
        elif x == 2 : return 'X'
        else: return ' '

    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu

    s = "" + "*"*39 + "\n"
    if len(coups_joues) == 0:
        s += "Coup joue = .\n"
    else:
        s += "Coup joue = {}\n".format(coups_joues[-1])

    s += "Scores = {}, {}\n".format(score1, score2)
    s += "Total de coups joués : {}\n".format(len(coups_joues))
    s += "Plateau : \n"

    premiere_ligne = intercale(" ")
    for i in range(8):
        premiere_ligne += intercale(chr(ord('A') + i))
    s += premiere_ligne
    s += "\n"
    s += souligne()

    for ligne in range(8):
        s += intercale(ligne)
        for colonne in range(8):
            if (ligne, colonne) in coups_possibles :
                ind = coups_possibles.index((ligne, colonne))
                if ind < 10 :
                    s += intercale(" " + str(colored(coups_possibles.index((ligne, colonne)), "blue")))
                else :
                    s += intercale(str(colored(coups_possibles.index((ligne, colonne)), "blue")))
            else :
                s += intercale(symbole(plateau[ligne][colonne]))
        s += intercale(ligne)[:-1]
        s += "\n"
        s += souligne()
    s += premiere_ligne

    s += "\nJoueur {}, a vous de jouer\n".format(joueur_courant)
    s += "Coups possibles : "
    for cp in coups_possibles :
        s += "({}, {})".format(str(cp[0]), chr(ord('A')+cp[1])) + "  "
    print(s)
# Fonctions utiles

def getPlateau(jeu):
    """ jeu  -> plateau
        Retourne le plateau du jeu passe en parametre
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return plateau

def getCoupsJoues(jeu):
    """ jeu  -> List[coup]
        Retourne la liste des coups joues dans le jeu passe en parametre
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return coups_joues



def getScores(jeu):
    """ jeu  -> Pair[nat nat]
        Retourne les scores du jeu passe en parametre
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return (score1, score2)

def getJoueur(jeu):
    """ jeu  -> nat
        Retourne le joueur a qui c'est le tour de jouer dans le jeu passe en parametre
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return joueur_courant


def changeJoueur(jeu, sim=False):
    """ jeu  -> void
        Change le joueur a qui c'est le tour de jouer dans le jeu passe en parametre (1 ou 2)
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    global joueurSuivant

    if joueur_courant == 1:
        joueurSuivant = 2

    else:
        joueurSuivant = 1

    if sim : return joueurSuivant

def getScore(jeu,joueur):
    """ jeu*nat->int
        Retourne le score du joueur
        Hypothese: le joueur est 1 ou 2
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    if joueur == 1: return score1
    return score2

def getCaseVal(jeu, ligne, colonne):
    """ jeu*nat*nat -> nat
        Retourne le contenu de la case ligne,colonne du jeu
        Hypothese: les numeros de ligne et colonne appartiennent bien au plateau  : ligne<=getNbLignes(jeu) and colonne<=getNbColonnes(jeu)
    """

    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return plateau[ligne][colonne]

def estValideInDirFromPos(jeu, i, j, dir_ligne, dir_colonne):
            plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
            if plateau[i][j] != 0: return False
            nb_pions_adverse = 0
            i += dir_ligne
            j += dir_colonne
            while (i in range(8) and j in range(8)) \
                    and plateau[i][j] != joueur_courant\
                    and plateau[i][j] != 0 :
                nb_pions_adverse += 1
                i += dir_ligne
                j += dir_colonne
            return i in range(8) and j in range(8) and plateau[i][j] != 0 and nb_pions_adverse != 0



def evaluerCoup(jeu, coup):
    jeuApresEval = joueCoup(jeu, coup, True)
    joueur_suivant = changeJoueur(jeuApresEval, True)
    plateauE, joueur_courantE, coups_possiblesE, coups_jouesE, (score1E, score2E) = jeuApresEval
    jeuApresEval = plateauE, joueur_suivant, coups_possiblesE, coups_jouesE, (score1E, score2E)
    coups_possiblesE = getCoupsValides(jeuApresEval)
    return plateauE, joueur_suivant, coups_possiblesE, coups_jouesE, (score1E, score2E)
