# CSA (CentraleSupélec Autocensure)


# Sommaire
- [Description](#description)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Contributeurs](#contributeurs)

# Description
[Haut](#sommaire)

Détection d'insultes dans un tweet (MVP).

Evaluation du degré de grossièreté d'un tweet :
* Rapport du nombre de mots insultants sur le nombre de mots du tweet. On attribuera à chaque mot insultant un coefficient de 1 à 5 évaluant la méchanceté de l'insulte que l'on prendra en compte dans cette évaluation.

Censure : 
* Censure des insultes dans les tweets.

Analyse d'un thème
* Graphique et diagramme des insultes et de leurs catégories sur un thème donné. 

Evaluation de la vague de haine engendrée : 
* En fonction de la grossièreté d'un tweet, on cherche à mesurer la façon dont les RTs et commentaires sont impactés

# Installation
[Haut](#sommaire)

Cloner le dépot (commande bash `git clone https://gitlab-ovh-02.cloud.centralesupelec.fr/paul.salquebre/csa.git`)

Installer les modules nécessaires : 
+ numpy
+ seaborn
+ matplotlib
+ pandas
+ TextBlob
+ Json
+ Tweepy

# Utilisation
[Haut](#sommaire)

Exécuter MVP.py avec la commande bash `python MVP.py`

Répondre aux instructions affichées :
* thème
* nombre de tweets traités
* format souhaité du résultat

# Contributeurs
[Haut](#sommaire)

* Marius Nahon
* Paul Salquebre
* Hugo Hakem
* Mark Piquant
* Noé Prat

