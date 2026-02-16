# Deep Learning Project

Application Flask simple avec API REST.

## Installation

1. Installer les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

Lancer l'application :
```bash
python run.py
```

L'application sera accessible sur `http://localhost:5000`

## Structure du projet

- `app/` - Application Flask principale
  - `routes/` - Blueprints pour les routes
    - `main.py` - Routes de rendu
    - `api.py` - Routes API
  - `templates/` - Templates HTML
- `data/` - Dataset
    - `dataset.csv` (<a target="_blank" href="https://www.kaggle.com/datasets/sharmajicoder/gaming-and-mental-health">téléchargeable ici</a>)
- `config.py` - Configuration de l'application
- `run.py` - Point d'entrée de l'application

## Routes

- `/` - Page d'accueil
- `/api/` - API REST (GET/POST)