class Solution(object):
    def uniquePaths(self, M):

        MOD = 10**9 + 7
        nombre_lignes = len(M)
        nombre_colonnes = len(M[0])
        arrivee = (nombre_lignes - 1, nombre_colonnes - 1)

        nombre_chemins = [[0] * nombre_colonnes for _ in range(nombre_lignes)]

        nombre_chemins[0][0] = 1

        for ligne in range(nombre_lignes):
            for colonne in range(nombre_colonnes):
            
                chemins_ici = nombre_chemins[ligne][colonne]

                if chemins_ici == 0 or (ligne, colonne) == arrivee:
                    continue

                mouvements_possibles = [
                    (0, 1, "droite"),
                    (1, 0, "bas"),
                ]

                for decalage_ligne, decalage_colonne, direction in mouvements_possibles:
                    nouvelle_ligne = ligne + decalage_ligne
                    nouvelle_colonne = colonne + decalage_colonne

                    if not (0 <= nouvelle_ligne < nombre_lignes and 0 <= nouvelle_colonne < nombre_colonnes):
                        continue

                    while (
                        0 <= nouvelle_ligne < nombre_lignes
                        and 0 <= nouvelle_colonne < nombre_colonnes
                        and M[nouvelle_ligne][nouvelle_colonne] == 1
                    ):
                        if direction == "droite":
                            nouvelle_ligne += 1
                            direction = "bas"
                        else:
                            nouvelle_colonne += 1
                            direction = "droite"

                    if not (0 <= nouvelle_ligne < nombre_lignes and 0 <= nouvelle_colonne < nombre_colonnes):
                        continue

                    nombre_chemins[nouvelle_ligne][nouvelle_colonne] = (
                        nombre_chemins[nouvelle_ligne][nouvelle_colonne] + chemins_ici
                    ) % MOD

        return nombre_chemins[arrivee[0]][arrivee[1]]