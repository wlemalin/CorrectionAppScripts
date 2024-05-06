# Traducteur de Presse-papiers (système Unix ou Linux y compris macOS)

Ce projet contient un script Python qui utilise l'API de Replicate pour corriger les fautes de grammaire, d'orthographe et de syntaxe du texte actuellement copié dans le presse-papiers de l'utilisateur.

## Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Ce script a été testé avec Python 3.8 et supérieur. Vous aurez également besoin d'une clé API de Replicate, que vous pouvez obtenir en vous inscrivant sur leur [site officiel](https://replicate.com).

## Installation

Pour utiliser ce script, suivez les étapes ci-dessous :

1. **Cloner le dépôt**
   
   Ouvrez un terminal et exécutez la commande suivante :
   ```bash
   git clone https://github.com/votreusername/votrerepertoire.git
   ```
   ```bash
   cd votrerepertoire
   ```

2. **Installer les dépendances dans le dossier du projet **

   Toujours dans le terminal, exécutez la commande suivante :
   ```bash
   pip install -r requirements.txt

3. **Configurer la clé API**

   Configurez votre clé API en créant la variable d'environnement REPLICATE_API_TOKEN. Pour cela, il va falloir ajouter la ligne export REPLICATE_API_TOKEN='votre_clé_api' à un fichier .bashrc ou .zshrc. La modification est ainsi "permanente", c'est-à-dire que vous aurez toujours accès à cette variable, jusqu'à modification/suppression.

1. Ouvrir le terminal sur votre machine.
2. Éditer le fichier .bashrc qui se trouve dans votre répertoire personnel en utilisant la commande suivante dans le terminal :
   ```bash
   # Pour les utilsateurs de Bash
   nano ~/.bashrc
   ```
   ```bash
   # Pour les utilsateurs de Zsh
   nano ~/.zshrc
   ```

3. Ajouter la ligne suivante à la fin du fichier:
   ```bash
   export REPLICATE_API_TOKEN='votre_clé_api'
   # Assurez-vous de remplacer 'votre_clé_api' par votre clé API réelle.
4. Sauvegarder le fichier et quitter l'éditeur en appuyant sur Ctrl+O, puis Enter, et quitter avec Ctrl+X.
5. Appliquer les modifications en rechargeant le fichier .bashrc avec la commande:
bash
Copy code
source ~/.bashrc
Pour les utilisateurs de Zsh (.zshrc)
Ouvrir le terminal.
Éditer le fichier .zshrc de la même manière que pour .bashrc. Si vous utilisez nano, la commande sera:
bash
Copy code
nano ~/.zshrc
Ajouter la ligne suivante à la fin du fichier:
bash
Copy code
export REPLICATE_API_TOKEN='votre_clé_api'
N'oubliez pas de remplacer 'votre_clé_api' par la clé API que vous avez.
Sauvegarder et quitter. Avec nano, sauvegardez avec Ctrl+O et Enter, puis quittez avec Ctrl+X.
Recharger le fichier .zshrc pour que les modifications prennent effet immédiatement:
bash
Copy code
source ~/.zshrc
En ajoutant cette ligne à votre fichier .bashrc ou .zshrc, vous configurez votre clé API pour être automatiquement disponible dans toutes les nouvelles sessions de terminal, ce qui facilite l'utilisation de scripts et d'outils nécessitant cette clé sans avoir à la configurer à chaque fois.







## Utilisation 

