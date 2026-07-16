
---

# Projet de recherche : Climatologie spatiale des massifs alpins à l'aide du réseau ROMMA

## Introduction

### Présentation du réseau ROMMA

Le **ROMMA** (*Réseau d'Observations Météorologiques du Massif Alpin*) est un réseau associatif d'observations météorologiques déployé à travers les Alpes françaises. Combinant les données de passionnés de météo bénévoles et d'installations professionnelles, il offre un suivi à très haute densité des facteurs environnementaux en relief complexe (couvrant des régions telles que l'Isère, la Savoie, la Haute-Savoie, les Hautes-Alpes et la Drôme).

Les rapports météorologiques institutionnels classiques s'appuient souvent sur un petit nombre de stations de référence régionales, ce qui lisse les riches variations micro-topographiques des massifs montagneux en de simples moyennes spatiales. La véritable force du réseau ROMMA réside dans sa densité : en capturant simultanément les données de dizaines de vallées, de plateaux et de sommets, il permet aux chercheurs de regarder « sous le capot » des bilans climatiques à grande échelle et d'analyser comment la géographie locale interagit avec la physique thermodynamique.

### Contexte scientifique : Le gradient thermique adiabatique

Le principe physique fondamental qui sous-tend ce projet est le **gradient thermique environnemental** — la vitesse à laquelle la température atmosphérique diminue avec l'altitude. Statistiquement, le suivi de cette relation à travers les Alpes donne un modèle de régression linéaire robuste :

Cependant, l'atmosphère est rarement uniforme. Les anomalies topographiques, telles que les massifs montagneux agissant comme des barrières physiques face aux perturbations, donnent naissance à des microclimats locaux uniques. L'un des exemples les plus célèbres au sein du réseau est la **Pelouse de Darbounouse** dans le Vercors — une dépression calcaire de haute altitude (*doline/polje*) où l'accumulation d'air froid nocturne crée d'intenses trous à froid, faisant chuter sa température bien en dessous de ce qu'un modèle de régression d'altitude classique prédit.

---

## Description des tâches

Ce projet est structuré comme un pipeline complet de science des données, allant de l'extraction web brute à la géostatistique avancée et à la modélisation physique.

### Tâche 1 : Web Scraping et expressions régulières (RegEx)

* **Objectif :** Extraire les profils de stations en temps réel et historiques de l'infrastructure web du ROMMA.
* **Méthodologie :** Écrire un script Python utilisant des expressions régulières (`re`) robustes pour analyser les structures HTML. Le scraper doit cibler les identifiants de stations, les noms, les altitudes et les coordonnées brutes.
* **Le défi :** Vous devez construire un motif regex capable de contourner proprement les caractères parasites initiaux (tels que les espaces ou les guillemets à l'intérieur des balises `<b>`) afin de commencer à capturer les noms de stations proprement à partir de la première lettre majuscule `[A-Z]`.

### Tâche 2 : Conversion algorithmique des coordonnées

* **Objectif :** Convertir les coordonnées spatiales brutes textuelles en données numériques exploitables (flottants).
* **Méthodologie :** Les coordonnées extraites directement des pages de stations sont stockées au format traditionnel DMS (**Degrés, Minutes, Seconds**), par exemple : `Longitude: 05° 50' 05" E`. Vous écrirez une fonction Python pour analyser ces chaînes et appliquer la formule de conversion :

$$\text{Degrés Décimaux (DD)} = \text{Degrés} + \frac{\text{Minutes}}{60} + \frac{\text{Secondes}}{3600}$$


* **Le défi :** Développer un script de test automatisé confirmant que les coordonnées sont fidèlement transformées en tuples de nombres décimaux `(Latitude, Longitude)` exploitables pour la cartographie.

### Tâche 3 : Pipeline géospatial et jointures spatiales « Point-in-Polygon » (PIP)

* **Objectif :** Automatiser la classification des stations météorologiques dans leurs massifs montagneux respectifs (ex. Vercors, Chartreuse, Belledonne).
* **Méthodologie :** En utilisant les bibliothèques **GeoPandas** et **Shapely**, vous ingérerez des fichiers vectoriels open-source au format GeoJSON contenant les polygones des limites des massifs alpins français (tels que les découpages officiels des massifs du modèle météorologique SAFRAN de Météo-France, disponibles sur data.gouv.fr).
* **Le défi :** Exécuter une jointure spatiale (`gpd.sjoin`) pour calculer mathématiquement dans quel polygone de massif chaque point de station se situe. Cela permet de s'affranchir d'une saisie manuelle en créant un pipeline de classification automatisé, capable également de filtrer et d'écarter automatiquement les stations hors-zone (ex. les stations situées en dehors de l'emprise géographique des Alpes).

### Tâche 4 : Analyse climatologique et modèles visuels

* **Objectif :** Analyser et comparer visuellement les gradients thermiques locaux.
* **Méthodologie :** Au lieu de traiter les Alpes comme un ensemble de données unique et uniforme, utilisez les classifications de massifs générées à la Tâche 3 pour appliquer un code couleur à vos graphiques et calculer des droites de régression *distinctes* pour chaque massif à l'aide de `scipy.stats.linregress`.

Vous pouvez vous appuyer sur le schéma conceptuel ci-dessous pour comprendre à quoi ressemble votre analyse de base initiale avant la classification par massif. Remarquez comment les anomalies globales se détachent de la tendance générale :

```
                        Analyse de base initiale
  Température (°C)
     ^
     |  . [Anomalie : ex. Station hors-Alpes]
     |     . .
     |        \ .  .
     |         \  . .
     |          \   .
     |           \    .  . [Anomalie : ex. Inversion à Darbounouse]
     |            \     .
     +----------------------------------------> Altitude (m)
               (Droite de tendance globale)

```

* **Le défi :** En comparant les différents gradients thermiques mathématiques ($\Delta^\circ\text{C} / 100\text{m}$) du Vercors, de la Chartreuse et de Belledonne, vous interpréterez physiquement leurs microclimats. Vous étudierez comment des phénomènes tels que le brassage solaire diurne, le refroidissement radiatif nocturne et les inversions thermiques en vallée font dévier des massifs spécifiques de la moyenne globale.

---

## Bibliographie et ressources du projet

Pour mener à bien ce projet, vous vous appuierez sur les documentations et dépôts de code principaux suivants :

* **Portail officiel du ROMMA :** [romma.fr](https://www.romma.fr/)
*À utiliser pour comprendre la structure du réseau, visualiser les flux de données en direct et étudier les bilans climatologiques régionaux mensuels.*
* **Dépôt de code du projet :** [github.com/macbuse/ROMMA](https://github.com/macbuse/ROMMA/)
*Accédez à ce dépôt pour examiner les scripts existants, les utilitaires d'expressions régulières et les échantillons de données compilés pour le réseau alpin.*
* **Documentation GeoPandas :** [geopandas.org](https://geopandas.org/)
*Consultez cette ressource pour obtenir des tutoriels sur la manipulation de données vectorielles géographiques, les systèmes de coordonnées de référence (CRS) et les jointures de données spatiales.*
