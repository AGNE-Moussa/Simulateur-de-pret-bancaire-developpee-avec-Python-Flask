# Simulateur de Prêt Bancaire

Ce projet est une application Flask qui simule les mensualités et le montant total d'un prêt bancaire basé sur les données saisies par l'utilisateur. L'application utilise un formulaire HTML pour recueillir les informations et affiche les résultats sous une forme bien stylisée.

---

## Fonctionnalités
- Saisie des paramètres du prêt :
  - **Montant du prêt (Mpret)**
  - **Taux d'intérêt annuel (Tia)**
  - **Durée du prêt (N)**
- Calcul automatique de :
  - **Mensualité (Mtmens)**
  - **Montant total global (Mglobal)**
- Interface utilisateur attrayante avec **Bootstrap**.
- Validation des données côté serveur.

---

## Technologies utilisées
- **Python** (Flask)
- **HTML5 / CSS3** avec **Bootstrap 5**
- **Jinja2** pour les templates dynamiques

---

## Installation et exécution

### Prérequis
- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/simulateur-pret-bancaire.git
   cd simulateur-pret-bancaire
Installez les dépendances :

bash
Copier le code
pip install flask
Lancez l'application :

bash
Copier le code
python app.py
Ouvrez votre navigateur et accédez à :

arduino
Copier le code
http://127.0.0.1:5000
Structure du projet
bash
Copier le code
simulateur-pret-bancaire/
├── templates/
│   ├── entree.html      # Formulaire pour saisir les données
│   ├── sortie.html      # Résultats affichés après le calcul
├── app.py               # Code principal de l'application Flask
├── README.md            # Documentation du projet