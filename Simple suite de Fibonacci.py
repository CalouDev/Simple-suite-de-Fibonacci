# 1, 1, 2, 3, 5, 8, 13, 21, ...

nbr_maximum = int(input("Valeur maximum : "))

resultat, nbr, nbr2  = 0, 1, 0

while resultat < nbr_maximum:
    resultat = nbr + nbr2
    nbr = nbr2
    nbr2 = resultat
    if resultat < nbr_maximum:
        print(resultat)