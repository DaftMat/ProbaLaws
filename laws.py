import numpy as np
import numpy.random as loi
import scipy.stats as loiT
import matplotlib.pyplot as plt


# TP PROBAS et STATISTIQUES en PYTHON 2
# EXERCICE 1 : comparaison de lois uniformes : theorique & pratique
def loi_unif(nb_val, param1, param2, barres, pas):

    # Loi pratique (valeurs aleatoires)
    xp = loi.uniform(param1, param2, size=nb_val)

    # Normalisation
    mini = param1
    maxi = param2

    # Loi theorique
    vec = np.arange(mini, maxi, pas)
    xt = loiT.uniform.pdf(vec) # A COMPLETER...

    # Affichage
    plt.figure()
    plt.hist(xp, barres, density=True, label='resultat pratique')
    plt.plot(vec, xt, 'or', label='resultat theorique') # A MODIFIER dans le cas discret par 'or'
    plt.title('Loi Uniforme') # A COMPLETER...
    plt.xlabel('Intervalles')
    plt.ylabel('Probabilites')
    plt.legend()
    plt.show()


def loi_expo(nb_val, param1, barres, pas): # A COMPLETER...

    # Loi pratique (valeurs aleatoires)
    xp = loi.exponential(param1, size=nb_val) # A COMPLETER...

    # Normalisation
    mini = 0
    maxi = nb_val

    # Loi theorique
    vec = np.arange(mini, maxi, pas)
    xt = loiT.expon.pdf(vec) # A COMPLETER...

    # Affichage
    plt.figure()
    plt.hist(xp, barres, density=True, label='resultat pratique')
    plt.plot(vec, xt, 'r', label='resultat theorique') # A MODIFIER dans le cas discret par 'or'
    plt.title('Loi Exponentielle') # A COMPLETER...
    plt.xlabel('Intervalles')
    plt.ylabel('Probabilites')
    plt.legend()
    plt.show()


def loi_geom(nb_val, param1, barres, pas):

    # Loi pratique (valeurs aleatoires)
    xp = loi.geometric(param1, size=nb_val)

    # Normalisation
    mini = 0
    maxi = nb_val
    p = param1

    # Loi theorique
    vec = np.arange(mini, maxi, pas)
    xt = loiT.geom.pmf(vec, p) # A COMPLETER...

    # Affichage
    plt.figure()
    plt.hist(xp, barres, density=True, label='resultat pratique')
    plt.plot(vec, xt, 'r', label='resultat theorique') # A MODIFIER dans le cas discret par 'or'
    plt.title('Loi Geometrique') # A COMPLETER...
    plt.xlabel('Intervalles')
    plt.ylabel('Probabilites')
    plt.legend()
    plt.show()


def loi_poisson(nb_val, param1, barres, pas):

    # Loi pratique (valeurs aleatoires)
    xp = loi.poisson(param1, size=nb_val)

    # Normalisation
    mini = 0
    maxi = nb_val
    lamb = param1

    # Loi theorique
    vec = np.arange(mini, maxi, pas)
    xt = loiT.poisson.pmf(vec, lamb) # A COMPLETER...

    # Affichage
    plt.figure()
    plt.hist(xp, barres, density=True, label='resultat pratique')
    plt.plot(vec, xt, 'r', label='resultat theorique') # A MODIFIER dans le cas discret par 'or'
    plt.title('Loi Poisson') # A COMPLETER...
    plt.xlabel('Intervalles')
    plt.ylabel('Probabilites')
    plt.legend()
    plt.show()


def loi_normale(nb_val, param1, param2, barres, pas):

    # Loi pratique (valeurs aleatoires)
    xp = loi.normal(param1, param2, size=nb_val)

    # Normalisation
    mini = 0
    maxi = nb_val
    mic = param1
    mu = param2

    # Loi theorique
    vec = np.arange(mini, maxi, pas)
    xt = loiT.norm.pdf(vec, mic, mu) # A COMPLETER...

    # Affichage
    plt.figure()
    plt.hist(xp, barres, density=True, label='resultat pratique')
    plt.plot(vec, xt, 'r', label='resultat theorique') # A MODIFIER dans le cas discret par 'or'
    plt.title('Loi Normale') # A COMPLETER...
    plt.xlabel('Intervalles')
    plt.ylabel('Probabilites')
    plt.legend()
    plt.show()


# DEBUT DU PROGRAMME PRINCIPAL

# Constante
nb_barres = 20
pas_reel = 0.02
pas_discret = 1

# (a) Tests de la loi Uniforme : loi discrete ou reelle au choix...
# 50 valeurs suivant une loi uniforme (min=0 & max=20) 
loi_unif(50, 0, 20, nb_barres, pas_discret)
# 10000 valeurs suivant une loi uniforme (min=0 & max=20)
loi_unif(10000, 0, 20, nb_barres, pas_discret)
# 10000 valeurs suivant une loi uniforme (min=-5 & max=5)
loi_unif(10000, -5, 5, nb_barres, pas_discret)

# (b) Tests de la loi Exponentielle : loi reelle
# 50 valeurs suivant une loi exponentielle : λ = 0.02
loi_expo(50, 0.02, nb_barres, pas_reel)
# 10000 valeurs suivant une loi exponentielle : λ = 0.02
loi_expo(10000, 0.02, nb_barres, pas_reel)
# 10000 valeurs suivant une lui exponentielle : λ = 0.08
loi_expo(10000, 0.08, nb_barres, pas_reel)

# 50 valeurs suivant une loi geometrique : p = 0.07
loi_geom(50, 0.07, nb_barres, pas_reel)
# 10000 valeurs suivant une loi geometrique : p = 0.07
loi_geom(10000, 0.07, nb_barres, pas_reel)
# 10000 valeurs suivant une loi geometrique : p = 0.2
loi_geom(10000, 0.2, nb_barres, pas_reel)

# 50 valeurs suivant une loi de Poisson : λ = 5
loi_poisson(50, 5, nb_barres, pas_reel)
# 10000 valeurs suivant une loi de Poisson : λ = 5
loi_poisson(10000, 5, nb_barres, pas_reel)
# 10000 valeurs suivant une loi de Poisson : λ = 0.5
loi_poisson(10000, .5, nb_barres, pas_reel)
# 10000 valeurs suivant une loi de Poisson : λ = 50
loi_poisson(10000, 50, nb_barres, pas_reel)

# 50 valeurs suivant une loi Normale : μ = 0 et σ = 1
loi_normale(50, 0, 1, nb_barres, pas_reel)
# 10000 valeurs suivant une loi Normale : μ = 0 et σ = 1
loi_normale(10000, 0, 1, nb_barres, pas_reel)
# 10000 valeurs suivant une loi Normale : μ = 5 et σ = 0.5
loi_normale(10000, 5, .5, nb_barres, pas_reel)
# 10000 valeurs suivant une loi Normale : μ = 50 et σ = 500
loi_normale(10000, 50, 500, nb_barres, pas_reel)