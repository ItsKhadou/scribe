"""Configuration centrale de Scribe.

Charge la clé API Groq depuis le fichier .env et centralise
les identifiants des modèles utilisés dans tout le projet.
"""

import os

from dotenv import load_dotenv

# Lit le fichier .env à la racine et injecte ses variables
# dans l'environnement du processus.
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Identifiants des modèles — seul endroit du projet où ils apparaissent.
STT_MODEL = "A_REMPLIR"
LLM_MODEL = "A_REMPLIR"

# Échec immédiat et lisible si la clé manque, plutôt qu'une
# erreur 401 cryptique au moment de l'appel API.
if not GROQ_API_KEY:
    raise SystemExit(
        "Erreur : GROQ_API_KEY est absente.\n"
        "Créez un fichier .env à la racine du projet (modèle : .env.example)."
    )