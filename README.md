# Algorithme--genetique--encodage-reel
Un algorithme génétique est une méthode d'optimisation inspirée de la sélection naturelle et de la génétique. Il simule le processus évolutif pour résoudre des problèmes complexes en explorant efficacement un large espace de solutions.


Voici une description détaillée de votre algorithme génétique à encodage réel, structurée pour être incluse dans un fichier `README.md` sur GitHub :

---

# Algorithme Génétique à Encodage Réel pour la Régression Linéaire

## 📌 Description
Cet algorithme génétique utilise un **encodage réel** pour optimiser les poids d'un modèle de régression linéaire, minimisant l'erreur absolue moyenne entre les prédictions (`X·w`) et les valeurs réelles (`Y`). Il suit les étapes classiques d'un AG (sélection, croisement, mutation) avec des opérateurs adaptés aux valeurs continues.

## 🧠 Fonctionnalités Clés
- **Encodage réel** : Les individus sont des vecteurs de poids `w = [w1, w2, w3]` dans un espace continu.
- **Fitness** : Erreur absolue moyenne entre `X·w` et `Y`.
- **Sélection** : Roulette biaisée (Davis) avec pondération exponentielle (`α=1.2`).
- **Croisement** : Opérateur arithmétique générant 3 enfants et conservant les 2 meilleurs.
- **Mutation** : Technique de Michalewicz modifiant un gène aléatoire avec décroissance temporelle.
- **Visualisation** : Suivi de la fitness sur 100 générations via matplotlib.

## ⚙️ Opérateurs Spécifiques

### 1. Sélection (`selection`)
- **Mécanisme** : 
  - Trie la population par fitness croissante.
  - Attribue un poids `Rw(i) = (N - i)^α` à chaque individu (meilleurs = poids élevés).
  - Sélectionne les parents via un tirage aléatoire pondéré par `Rw`.

### 2. Croisement (`croisement`)
- **Probabilité `Pc=0.8`** : 
  - Génère 3 enfants par combinaisons linéaires de 2 parents :
    - `R1 = 0.5*P1 + 0.5*P2`
    - `R2 = 1.5*P1 - 0.5*P2`
    - `R3 = -0.5*P1 + 1.5*P2`
  - Garde les 2 enfants avec la meilleure fitness.

### 3. Mutation (`mutation`)
- **Probabilité `Pm=0.1`** : 
  - Modifie un gène aléatoire via `delta_michalewicz` :
    - `delta = r * y * (1 - t/T)^b` (où `y = max_val - val_courante`).
    - Ajoute/soustrait `delta` aléatoirement (pile/face).
  - Décroissance exponentielle avec `b=3` pour réduire l'impact des mutations au fil des générations.

## 📊 Résultats
- **Sortie** : Meilleur individu `w` et son erreur moyenne.
- **Visualisation** : Graphique montrant la convergence de la fitness (erreur minimale par génération).

## 🛠️ Compatibilité avec Votre Code
- **Entrée** : Fichier CSV `Adv.csv` avec colonnes 1-3 pour `X` et colonne 4 pour `Y`.
- **Paramètres ajustables** :
  ```python
  T = 100      # Nombre de générations
  N = 30       # Taille de la population
  bornes = [-3, 3]  # Bornes des poids initiaux
  alpha = 1.2  # Exposant de sélection
  ```

## 📈 Exemple de Sortie
```python
Generation 99: Meilleure fitness = 1.2456
=== RESULTATS FINAUX ===
Meilleur individu trouvé : [0.045 2.123 -1.876]
Fitness correspondante : 1.2456
```



