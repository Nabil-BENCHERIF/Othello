from Noeud import *

import othello
import time
horizon = 4

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """


    debut = time.time()
    arbre_minimax = instancier_arbre_minimax(jeu, difference_score, horizon, True)
    fin = time.time()
    print("=================== horizon : {}; temps : {} s; len(arbre) : {} noeuds".format(horizon, fin-debut, len(arbre_minimax)))
    coup = arbre_minimax.decision()
    return coup

def instancier_arbre_minimax(jeu, fonction_evaluation=None, profondeur=float("inf"), elagage=False):
    arbre_minimax = Noeud(typeJeu=othello, jeu=jeu)
    arbre_minimax.developper(profondeur, fonction_evaluation, elagage)
    return arbre_minimax

def difference_score(jeu):
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    if joueur_courant == 1:
        return score1 - score2
    elif joueur_courant == 2:
        return score2 - score1

def mobilite(jeu):
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    return len(coups_possibles)
