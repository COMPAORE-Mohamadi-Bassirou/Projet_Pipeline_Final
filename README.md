# Construction d'un Pipeline ETL pour l'Analyse de l'Impact des Dépenses Publiques de Santé sur la Mortalité Infantile à l'échelle mondiale

## Description
Ce projet utilise Streamlit pour analyser l'impact des dépenses publiques de santé sur la mortalité infantile à l'échelle mondiale. Il permet de visualiser des données et d'interagir avec différentes métriques.

## Introduction
La mortalité infantile est un indicateur essentiel de la santé publique, révélant l’efficacité des systèmes de soins d’un pays. Malgré des efforts pour améliorer la survie infantile, des inégalités persistent. Cette étude vise à analyser l'impact des dépenses publiques de santé sur la mortalité infantile, couvrant la période de 2000 à 2023.

## Justification du Sujet
La mortalité infantile reste un défi majeur avec des conséquences socio-économiques. Ce rapport étudie comment les dépenses publiques de santé influencent la mortalité infantile et comment une gestion optimale de ces dépenses pourrait favoriser une société plus saine.

## Revue de la Littérature
### I. Revue Théorique
#### 1.1. Concepts de base et définitions
- **Mortalité infantile** : Nombre de décès d'enfants avant leur cinquième anniversaire.
- **Dépenses publiques de santé** : Investissements étatiques pour assurer l'accès aux soins.

### II. Revue Empirique
- **Études dans les pays en développement** : Corrélation entre l’augmentation des dépenses de santé et la baisse de la mortalité infantile.
- **Impact de la gouvernance** : La qualité de la gouvernance joue un rôle crucial pour maximiser l’efficacité des dépenses de santé.

## Problématique
Comment les dépenses publiques de santé influencent-elles la mortalité infantile dans différents pays, et quelles variables socio-économiques peuvent renforcer ou atténuer cet effet ?

## Objectifs de l’Étude
### Objectif principal
Mesurer l'impact des dépenses publiques de santé sur la mortalité infantile à l’échelle mondiale.

### Objectifs spécifiques
1. Évaluer la corrélation entre les dépenses de santé et la mortalité infantile.
2. Identifier les variables socio-économiques influençant la mortalité infantile.
3. Comparer les performances des pays.
4. Proposer des recommandations pour optimiser les dépenses publiques en santé.

## Méthodologie
### 1. Extraction
Données extraites de la Banque mondiale à l'aide d'APIs couvrant la période de 1960 à 2023.

### 2. Transformation
Filtrage, imputation et nettoyage des données.

### 3. Chargement
Chargement des données sur Amazon S3.

### 4. Analyse des Données
Analyses statistiques pour mesurer l'impact des dépenses publiques sur la mortalité infantile.

### 5. Visualisation et Reporting
Tableaux de bord dynamiques pour présenter les résultats.

## Analyses des données
### Première étape : Statistiques descriptives
Portrait d’ensemble des indicateurs clés.

### Deuxième étape : Analyses de corrélation
Analyse de la relation entre dépenses publiques et mortalité infantile.

### Interprétation de la Corrélation
Relations et implications pour les politiques de santé.

### Analyse de Régression Linéaire par Pays
Exploration des spécificités contextuelles de chaque nation.

### Analyse de Régression Linéaire Avancée
Interactions entre plusieurs variables clés.

## Résultats
Résultats des analyses présentés pour comparaison.

## Évolution de la Courbe de Tendance par Pays
Examen des tendances au fil des ans.

## Implications pour les Politiques de Santé
Recommandations basées sur les résultats.

## Conclusion et Recommandations
### Conclusion
Synthèse des résultats de l'étude.

### Recommandations
Stratégies pour maximiser l'efficacité des investissements en santé.

## Technologies Utilisées
- **Streamlit** : Framework pour créer des applications web interactives en Python.
- **Pandas** : Bibliothèque pour la manipulation et l'analyse de données.
- **Plotly** : Bibliothèque pour la création de visualisations interactives.
- **Openpyxl** : Bibliothèque pour lire et écrire des fichiers Excel.
