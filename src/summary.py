"""Génération de compte rendu structuré via l'API chat completions de Groq."""

from pathlib import Path

from groq import Groq, GroqError

from src.config import GROQ_API_KEY, LLM_MODEL

CHEMIN_PROMPT_SYSTEME = Path("prompts/system.txt")

client = Groq(api_key=GROQ_API_KEY)


def charger_prompt_systeme() -> str:
    """Lit le prompt système depuis le fichier du projet."""
    if not CHEMIN_PROMPT_SYSTEME.exists():
        raise FileNotFoundError(
            f"Prompt système introuvable : {CHEMIN_PROMPT_SYSTEME}"
        )
    return CHEMIN_PROMPT_SYSTEME.read_text(encoding="utf-8")


def resumer(transcription: str) -> str:
    """Transforme une transcription brute en compte rendu structuré.

    Args:
        transcription: le texte brut issu de la transcription audio.

    Returns:
        Le compte rendu en Markdown produit par le LLM.

    Raises:
        RuntimeError: si l'appel à l'API Groq échoue.
    """
    prompt_systeme = charger_prompt_systeme()

    try:
        reponse = client.chat.completions.create(
            model=LLM_MODEL,
            temperature=0.2,
            messages=[
                {"role": "system", "content": prompt_systeme},
                {"role": "user", "content": transcription},
            ],
        )
    except GroqError as erreur:
        raise RuntimeError(
            f"Échec de la génération du compte rendu via Groq : {erreur}"
        ) from erreur

    return reponse.choices[0].message.content


if __name__ == "__main__":
    from src.transcription import transcrire

    texte = transcrire("audio/exemple.m4a")
    print(resumer(texte))