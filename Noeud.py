# game.game=awele

class Noeud():

    def __init__(self, typeJeu=None, jeu=None, Max=True):
        """Noeud * TYPE_JEU * jeu * bool - > void
            instancie un noeud du jeu TYPE_JEU (awele, othello) avec la configuration de jeu
            jeu. Si Max = True alors il s'agit d'un Noeud Max sinon il s'agit d'un noeud Min"""
        self.typeJeu = typeJeu                             # Awele ou Othello
        self.jeu = typeJeu.getCopieJeu(jeu)                # Copie du jeu avec recalcule des coups possibles
        self.typeNoeud_est_Max = Max
        # fils : dict[coup, Noeud]
        self.fils = dict()
        # initialisation de l'evaluation du noeud (+ infini pour les noeuds de type max; - infini pour les noeuds min)
        if self.typeNoeud_est_Max :
            self.v = - float("inf")
        else:
            self.v = float("inf")

    def developper(self, profondeur, fonctionEvaluation, elagage=False, alpha=-float("inf"), beta=float("inf")):
        """Noeud * int * int * bool * int * int -> void
            developpe le noeud courant en un arbre de profondeur profondeur avec comme valeur d evaluation
            de la sequence de jeu courante egale a cumul. Cette construction d'arbre minimax utilise l elagage
            ssi elagage == True."""

        if profondeur > 0 and not self.typeJeu.finJeu(self.jeu):
            plateau, joueur_courant, coups_possibles, coups_joues, (score1, score2) = self.jeu
            for coup in coups_possibles:
                jeuEval = self.typeJeu.evaluerCoup(self.jeu, coup)
                plateauE, joueur_suivant, coups_possiblesE, coups_jouesE, (score1E, score2E) = jeuEval
                if len(coups_possiblesE) == 0: # joueur_suivant bloque
                    # print("================== BLOCKED")
                    jeuEvalMod = plateauE, joueur_courant, coups_possiblesE, coups_jouesE, (score1E, score2E)
                    noeud_coup = Noeud(typeJeu=self.typeJeu, jeu=jeuEvalMod, Max=self.typeNoeud_est_Max)
                    noeud_coup.developper(profondeur - 1, fonctionEvaluation, elagage, alpha, beta)
                else :
                    noeud_coup = Noeud(typeJeu=self.typeJeu, jeu=jeuEval, Max=not(self.typeNoeud_est_Max))
                    noeud_coup.developper(profondeur - 1, fonctionEvaluation, elagage, alpha, beta)

                if self.typeNoeud_est_Max:
                    self.v = max(self.v, noeud_coup.v)
                    if elagage :
                        if self.v >= beta: return
                        alpha = max(alpha, self.v)
                else:
                    self.v = min(self.v, noeud_coup.v)
                    if elagage :
                        if self.v <= alpha: return
                        beta = min(beta, self.v)

                self.fils[coup] = noeud_coup

        else:
            self.v = fonctionEvaluation(self.jeu)

    def decision(self):
        """Noeud -> Coup
        retourne le meilleur coup depuis le Noeud appelant."""
        for coup, node_fils in self.fils.items():
            if self.v == node_fils.v: return coup

    def __len__(self):
        taille = 1
        for noeud_fils in self.fils.values():
            taille += len(noeud_fils)
        return taille
