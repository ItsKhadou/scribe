"""Point d'entrée en ligne de commande de Scribe.

Usage :
    python -m src.cli chemin/vers/audio.m4a
"""

import sys
from datetime import datetime
from pathlib import Path

from src.summary import resumer
from src.transcription import transcrire

DOSSIER_SORTIES = Path("outputs")


def main() -> None:
    # 1. Lecture de l'argument (le chemin du fichier audio)
    if len(sys.argv) != 2:
        raise SystemExit(
            "Usage : python -m src.cli <chemin_du_fichier_audio>"
        )
    chemin_audio = sys.argv[1]

    # 2. Transcription
    print("[1/3] Transcription en cours...")
    transcription = transcrire(chemin_audio)

    # 3. Compte rendu
    print("[2/3] Rédaction du compte rendu en cours...")
    compte_rendu = resumer(transcription)

    # 4. Sauvegarde dans un fichier Markdown daté
    print("[3/3] Sauvegarde...")
    DOSSIER_SORTIES.mkdir(exist_ok=True)
    horodatage = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    fichier_sortie = DOSSIER_SORTIES / f"{horodatage}.md"
    fichier_sortie.write_text(compte_rendu, encoding="utf-8")

    # 5. Affichage
    print()
    print(compte_rendu)
    print()
    print(f"Compte rendu sauvegardé dans : {fichier_sortie}")


if __name__ == "__main__":
    main()
    