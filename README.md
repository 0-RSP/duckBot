# ![Logo du projet](/images/logo.png) duckBot
Un modèle de bot Discord introductif écrit en Python.

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Licence](https://img.shields.io/badge/licence-Apache%20License%202.0-green)
![Étoiles](https://img.shields.io/github/stars/0-RSP/duckBot?style=social)
![Forks](https://img.shields.io/github/forks/0-RSP/duckBot?style=social)

![Image de prévisualisation de duckBot](/images/console_exec_duckBot.webp)

## ✨ Fonctionnalités
`duckBot` est conçu pour être un point de départ simple et extensible pour le développement de bots Discord en Python.
* 🚀 **Architecture modulaire** : Utilise le système de `cogs` de Discord.py pour une gestion organisée, maintenable et évolutive des commandes.
* 💬 **Gestion de commandes basiques** : Fournit une base pour créer et répondre à des commandes textuelles simples.
* 🐍 **Design Pythonique** : Écrit avec un code Python propre et lisible, suivant les meilleures pratiques, ce qui le rend facile à comprendre et à modifier.
* 🛠️ **Installation facile** : Lancez votre bot rapidement avec une configuration minimale.

## ⚙️ Installation
Suivez ces étapes pour installer et exécuter `duckBot` sur votre machine locale.

### Prérequis
Assurez-vous d'avoir installé les éléments suivants :
* Python 3.8 ou supérieur
* `pip` (installateur de paquets Python)

### Étapes d'installation
1. **Cloner le dépôt :**
   ```bash
   git clone https://github.com/0-RSP/duckBot.git
   cd duckBot
   ```

2. **Créer un environnement virtuel (recommandé) :**
   ```bash
   python -m venv venv
   ```

3. **Activer l'environnement virtuel :**
   * **Sur Windows :**
     ```bash
     .\venv\Scripts\activate
     ```
   * **Sur macOS/Linux :**
     ```bash
     source venv/bin/activate
     ```

4. **Installer les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

5. **Configuration :**
   Créez un fichier `.env` dans le répertoire racine (ou utilisez des variables d'environnement) pour stocker le token de votre bot et d'autres informations sensibles.
   ```env
   # .env
   DISCORD_TOKEN = "VOTRE_TOKEN_DE_BOT_DISCORD_ICI"
   # Ajoutez ici d'autres variables de configuration
   ```
   *Remplacez `VOTRE_TOKEN_DE_BOT_DISCORD_ICI` par le token réel de votre bot Discord depuis le [Portail Développeur Discord](https://discord.com/developers/applications).*

## 🚀 Utilisation
Une fois installé et configuré, vous pouvez exécuter `duckBot` et interagir avec lui sur Discord.

### Lancer le bot
Pour démarrer le bot, exécutez simplement le fichier `main.py` :
```bash
python main.py
```
Le bot devrait maintenant être en ligne sur votre serveur Discord.

## 🗺️ Feuille de route du projet
`duckBot` est un modèle introductif, et il existe de nombreuses possibilités passionnantes pour son développement futur :
* **Version 1.1.0 - Ensemble de commandes amélioré :**
  * Ajout de commandes utilitaires supplémentaires (par exemple, `!ping`, `!info`).
  * Implémentation de commandes de modération basiques.
* **Version 1.2.0 - Stockage persistant :**
  * Intégration avec une base de données simple (par exemple, SQLite) pour stocker les données utilisateur ou les paramètres du bot.
* **Version 1.3.0 - Options de personnalisation :**
  * Permettre aux administrateurs de serveur de personnaliser les préfixes du bot ou les messages de bienvenue.
* **Améliorations futures :**
  * Meilleure gestion des erreurs et journalisation.
  * Exemples de cogs plus sophistiqués.
  * Intégration avec des API externes.

### Style de code
* Respectez le [PEP 8](https://www.python.org/dev/peps/pep-0008/) pour le style de code Python.
* Utilisez des docstrings claires et concises pour les fonctions, classes et modules.


## 📜 Licence
Ce projet est sous licence **Apache License 2.0**.
Voir le fichier `LICENSE` pour plus de détails.

```
Copyright 2023 0-RSP
Sous licence Apache License, Version 2.0 (la "Licence") ;
vous ne pouvez pas utiliser ce fichier sauf en conformité avec la Licence.
Vous pouvez obtenir une copie de la Licence à l'adresse suivante :
    http://www.apache.org/licenses/LICENSE-2.0
Sauf si requis par la loi applicable ou convenu par écrit, le logiciel
distribué sous la Licence est distribué "EN L'ÉTAT",
SANS GARANTIES OU CONDITIONS DE QUELQUE NATURE QUE CE SOIT, exprimées ou implicites.
Voir la Licence pour connaître les permissions et limitations spécifiques.
```
