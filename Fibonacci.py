max_nbr = int(input("Maximum value : ")) # max_nbr = Valeur maximale
print("FIBONACCI WITH MAXIMUM VALUE = {} \n".format(max_nbr))

def fibonacci(totale, result, nbr, nbr2):
  while totale <= result: # Utilise max_nbr pour définir la valeur maximale
    totale = nbr + nbr2 # Le nombre finale par boucle
    nbr = nbr2
    nbr2 = totale
    if totale == result:
      print(totale, end='')
    elif totale <= result: # Parceque la boucle ce répète une fois après que la valeur maximale soit atteinte (totale <= result)
      print(totale, end=', ') # Affiche la valeur

fibonacci(0, max_nbr, 1, 0)
