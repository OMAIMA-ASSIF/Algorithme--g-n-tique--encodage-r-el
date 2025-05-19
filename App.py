#Base de données
import pandas as pd
import numpy as np
df = pd.read_csv("Adv.csv")

X = df.iloc[: , [1, 2, 3]].values
print("Valeurs de X :\n", X)
n = len(X[:, 0]) # Taille de X
# Y est sales 
Y = df.iloc[: , 4].values
print("Valeurs de Y :\n", Y)

bornes = [-3, 3]
N = 30  # Taille de la population initiale
pop_w = np.random.randint(bornes[0], bornes[1] + 1, size=(N, 3)) 
print("Population initiale :\n" ,pop_w)

#calcul de produit verctoriel entre w et xi 
def wx(w , x):
    return np.dot(w, x)

#Fitness de la population w: individu de la population pop_w
def E(w):
    erreurs = np.dot(X, w) - Y
    return np.sum(erreurs) / n


#Calcul de fitness pour toute la population
def fitness(pop_w):
    return np.array([abs(E(w)) for w in pop_w])


#SELECTION
## Poids relative a chaque individu 
def Rw(i, alpha=1.2):
    return (len(pop_w)-i)**alpha

def selection(pop_w, fitness):
    # 1. Trier la population par fitness croissante (meilleur -> pire)
    indices_tries = np.argsort(fitness)
    pop_triee = pop_w[indices_tries]  # Population triée 
    # 2. Rw pour chaque individu trié
    rw = np.array([Rw(i) for i in range(N)])
    # 3. Pr(i) = Rw(i) / sum(Rw)
    proba = rw / np.sum(rw)
    # 4. Sélectionner les parents selon Pr(i)
    parents_indices = np.random.choice(N, size=N, p=proba, replace=True)
    parents = pop_triee[parents_indices]
    return parents 





#CROISEMENT 
def croisement(pop_w, pc=0.8):
    # 1. Crée une copie de la population
    nouvelle_pop = pop_w.copy()
    idx_parents = np.random.choice(len(pop_w), size=2, replace=False)
    P1, P2 = pop_w[idx_parents[0]], pop_w[idx_parents[1]]
    if np.random.rand() < pc:
        R1 = 0.5*P1 + 0.5*P2
        R2 = 1.5*P1 - 0.5*P2
        R3 = -0.5*P1 + 1.5*P2
        enfants = np.array([R1, R2, R3])
        fitness_enfants = np.array([abs(E(R)) for R in enfants])
        meilleurs_enfants = enfants[np.argsort(fitness_enfants)[:2]]
        nouvelle_pop[idx_parents[0]] = meilleurs_enfants[0]
        nouvelle_pop[idx_parents[1]] = meilleurs_enfants[1]
    
    return nouvelle_pop


#MUTATION
##Technique de Michalewicz (un seul gène modifié par individu, choisi aléatoirement)
def delta_michalewicz(y, t, T, b=3):
    r = np.random.rand()  # Nombre aléatoire entre 0 et 1
    return r * y * (1 - t/T)**b
#t : itération actuelle
#T : nombre d'itérations total
def mutation(pop_w, t, T, b=3, Pm=0.1):
    nouvelle_pop = pop_w.copy()
    for i in range(len(nouvelle_pop)):
        if np.random.rand() < Pm:
            j = np.random.randint(0, len(nouvelle_pop[i]))
            val_courante = nouvelle_pop[i][j]
            max_val = np.max(nouvelle_pop[i]) # Valeur maximale de l'individu
            y = max_val - val_courante
            delta = delta_michalewicz(y, t, T, b)
            
            # Pile ou face
            # 0 : Pile, 1 : Face
            if np.random.randint(0, 2) == 0:  # Pile
                nouvelle_pop[i][j] = nouvelle_pop[i][j] + delta
            else:  # Face
                nouvelle_pop[i][j] = nouvelle_pop[i][j] - delta
    
    return nouvelle_pop


T = 100  # Nombre total d'itérations (générations)
b = 3    # Paramètre pour la mutation de Michalewicz
Pm = 0.1 # Probabilité de mutation
Pc = 0.8 # Probabilité de croisement
alpha = 1.2 # Pour formule de Davis


historique_fitness = []

for t in range(T):
    # 1. Sélection
    pop_w = selection(pop_w, fitness(pop_w))
    
    # 2. Croisement
    pop_w = croisement(pop_w, Pc)
    
    # 3. Mutation
    pop_w = mutation(pop_w, t, T, b, Pm)
    
    # 4. Suivi des performances
    fit = np.min(fitness(pop_w))  # Meilleure fitness de la génération
    historique_fitness.append(fit)
    
    # Affichage périodique
    print(f"Generation {t}: Meilleure fitness = {fit:.4f}")

# RESULTATS FINAUX
meilleur_individu = pop_w[np.argmin(fitness(pop_w))]
print("\n=== RESULTATS FINAUX ===")
print(f"Meilleur individu trouvé : {meilleur_individu}")
print(f"Fitness correspondante : {E(meilleur_individu):.4f}")

# VISUALISATION
import matplotlib.pyplot as plt
plt.plot(historique_fitness)
plt.title("Evolution de la fitness au cours des générations")
plt.xlabel("Génération")
plt.ylabel("Fitness (erreur absolue moyenne)")
plt.grid(True)
plt.show()
