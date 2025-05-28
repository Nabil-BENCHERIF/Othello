#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")


def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    case = float("inf")
    while case >= len(coups_possibles) or case < 0:
        case = int(input("Saisissez le numéro de la case à jouer!\n"))
    return coups_possibles[case]
