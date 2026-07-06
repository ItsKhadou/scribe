"""Transcription audio via l'API Speech-to-Text de Groq."""

from pathlib import Path

from groq import Groq, GroqError

from src.config import GROQ_API_KEY, STT_MODEL

client = Groq(api_key=GROQ_API_KEY)


def transcrire(chemin_audio: str) -> str:
    """Transcrit un fichier audio en texte.

    Args:
        chemin_audio: chemin vers le fichier audio à transcrire.

    Returns:
        La transcription texte de l'audio.

    Raises:
        FileNotFoundError: si le fichier n'existe pas.
        RuntimeError: si l'appel à l'API Groq échoue.
    """
    fichier = Path(chemin_audio)
    if not fichier.exists():
        raise FileNotFoundError(
            f"Fichier audio introuvable : {chemin_audio}"
        )

    try:
        with fichier.open("rb") as audio:
            reponse = client.audio.transcriptions.create(
                file=(fichier.name, audio.read()),
                model=STT_MODEL,
            )
    except GroqError as erreur:
        raise RuntimeError(
            f"Échec de la transcription via Groq : {erreur}"
        ) from erreur

    return reponse.text


if __name__ == "__main__":
    print(transcrire("audio/exemple.m4a"))