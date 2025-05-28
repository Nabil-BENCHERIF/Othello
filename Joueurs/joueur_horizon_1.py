#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

sys.path.append("../..")
import copy
from othello import evaluerCoup

def evaluer_coup(jeu, coup):
    """ jeu * coup -> int
        retourne la différence de points obtenus en jouant le coup
        coup à partir de la configuration de jeu jeu """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    jeuEval = evaluerCoup(jeu, coup)
    plateau, joueur_courantEval, coups_possibles, coups_joues, (score1, score2) = jeuEval
    if joueur_courant == 1 :
        return score1 - score2
    elif joueur_courant == 2:
        return score2 - score1
    # print("============= {}".format(coup))

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    meilleur_coup = coups_possibles[0]
    meilleur_gain = evaluer_coup(jeu, coups_possibles[0])
    for autre_coup in coups_possibles[1:]:
        gain_autre_coup = evaluer_coup(jeu, autre_coup)
        if gain_autre_coup > meilleur_gain:
            meilleur_gain = gain_autre_coup
            meilleur_coup = autre_coup

    return meilleur_coup
