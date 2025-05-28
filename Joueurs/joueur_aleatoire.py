#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.path.append("../..")

import random

def saisieCoup(jeu):
    """ jeu -> coup
        Retourne un coup a jouer
    """
    plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = jeu
    print(coups_possibles)
    return coups_possibles[random.randrange(len(coups_possibles))]

