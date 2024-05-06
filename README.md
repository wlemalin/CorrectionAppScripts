# Traducteur de Presse-papiers (système Unix ou Linux y compris macOS)

Ce projet contient un script Python qui utilise l'API de Replicate pour corriger les fautes de grammaire, d'orthographe et de syntaxe du texte actuellement copié dans le presse-papiers de l'utilisateur.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Ce script a été testé avec Python 3.8 et supérieur. Vous aurez également besoin d'une clé API de Replicate, que vous pouvez obtenir en vous inscrivant sur leur [site officiel](https://replicate.com).

## Installation

Pour utiliser ce script, suivez les étapes ci-dessous :

1. **Cloner le dépôt**
   
   Ouvrez un terminal et exécutez la commande suivante :
   ```bash
   git clone https://github.com/MateoDib/CorrectionAppScripts.git
   ```
   ```bash
   cd votrerepertoire
   ```

2. **Installer les dépendances dans le dossier du projet **

   Toujours dans le terminal, exécutez la commande suivante :
   ```bash
   pip install -r requirements.txt
   ```
Vous avez dorénavant téléchargé tout ce qu'il fallait. Vous pouvez continuer la configuration.

## Configurer la clé API

   Configurez votre clé API en créant la variable d'environnement REPLICATE_API_TOKEN. Pour cela, il va falloir modifier votre fichier .bashrc ou .zshrc. La modification est ainsi "permanente", c'est-à-dire que vous aurez toujours accès à cette variable, jusqu'à modification/suppression.

1. Ouvrir le terminal sur votre machine (Command + Espace, écrivez "Terminal" dans la barre de recherche, puis taper sur Entrer).

2. Éditer le fichier .bashrc pour les utilisateurs de Bash ou .zshrc pour les utilisateurs de Zsh qui se trouve dans votre répertoire personnel en utilisant la commande suivante dans le terminal :

   Pour savoir si vous êtes en Bash ou Zsh :
    ```bash
   echo $SHELL
   ```
    Puis en fonction de la sortie :
   ```bash
   # Pour les utilsateurs de Bash (.bashrc)
   nano ~/.bashrc
   ```
   ```bash
    # Pour les utilisateurs de Zsh (.zshrc)
   nano ~/.zshrc
   ```

3. Ajouter la ligne suivante à la fin du fichier (la configuration est étonante mais faites-vous confiance, la fin du fichier c'est juste en bas, vous avez simplement à copier la liegne suivante):
   ```bash
   export REPLICATE_API_TOKEN='votre_clé_api'
   # Assurez-vous de remplacer 'votre_clé_api' par votre clé API réelle.
   ```
5. Sauvegarder le fichier et quitter l'éditeur en appuyant sur Ctrl+O, puis Enter, et quitter avec Ctrl+X.

6. Appliquer les modifications en rechargeant le fichier .bashrc avec la commande:
   ```bash
   source ~/.bashrc
    # Pour les utilisateurs de Bash (.bashrc)
   ```
   
   ```bash
   source ~/.zshrc
   # Pour les utilisateurs de Zsh (.zshrc)
   ```

En ajoutant cette ligne à votre fichier .bashrc ou .zshrc, vous configurez votre clé API pour être automatiquement disponible dans toutes les nouvelles sessions de terminal, ce qui facilite l'utilisation de scripts et d'outils nécessitant cette clé sans avoir à la configurer à chaque fois.



## Utilisation 

