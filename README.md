# Scribe

**Scribe transforme un enregistrement audio en compte rendu écrit et structuré.**

À partir d'un fichier audio (réunion, cours, note vocale), Scribe enchaîne deux briques intelligentes appelées via l'API serverless de **Groq** :

1. Un modèle de reconnaissance vocale (**Speech-to-Text**) transcrit l'audio en texte brut.
2. Un LLM reformule ce texte en compte rendu propre : titre, résumé, points clés, décisions ou actions.

Le résultat s'affiche dans le terminal et est également sauvegardé dans un fichier Markdown daté.

Projet réalisé dans le cadre du **TP « Scribe »** du Master 2 MD5 — Data & IA, avec un double objectif : maîtriser le workflow Git/GitHub en équipe, et intégrer des modèles serverless dans une application classique.

---

## Structure du projet

```
scribe/
├── src/               ← code source Python
├── prompts/           ← prompts système du LLM (fichiers texte, séparés du code)
├── audio/             ← fichiers audio d'exemple
├── requirements.txt   ← dépendances Python
├── .env.example       ← variables d'environnement attendues (à copier en .env)
└── .gitignore
```

Le prompt système du LLM est délibérément stocké dans un fichier texte séparé du code, pour pouvoir l'itérer sans toucher à la logique applicative.

---

## Installation

Prérequis : **Python 3.10+** et un compte **Groq** avec une clé API (voir [console.groq.com](https://console.groq.com)).

```bash
# 1. Cloner le dépôt
git clone https://github.com/ItsKhadou/scribe.git
cd scribe

# 2. Créer et activer un environnement virtuel
python -m venv .venv
.venv\Scripts\activate         # Windows PowerShell
# source .venv/bin/activate    # macOS / Linux

# 3. Installer les dépendances
pip install -r requirements.txt

# 4. Configurer sa clé API Groq
copy .env.example .env         # Windows
# cp .env.example .env         # macOS / Linux
# puis éditer .env pour y coller sa clé
```

---

## Utilisation

*Cette section sera complétée à l'étape 5 (assemblage CLI). À ce stade du projet, Scribe est encore en construction.*

---

## Choix techniques

### Pourquoi le `.gitignore` a été mis en place avant toute logique métier (Q1)

Le `.gitignore` a été étendu dès le **premier commit fonctionnel** du projet, avant même que la moindre ligne de code manipulant un secret n'existe. C'est un ordre volontaire.

Une clé API est un mot de passe : dès qu'elle apparaît une seule fois dans un commit — même supprimée par la suite — elle vit à jamais dans l'historique Git et peut être extraite par n'importe qui ayant accès au dépôt. La réparation n'est ni simple ni fiable : il faut réécrire l'historique, invalider la clé et en régénérer une nouvelle.

Le seul remède qui fonctionne, c'est la **prévention** : configurer l'exclusion du fichier `.env` **avant** qu'un fichier `.env` puisse exister. Le `.gitignore` sert de garde-fou permanent : même si l'on tape `git add .` par mégarde, Git refuse d'ajouter les fichiers listés.

Sont ignorés dans notre `.gitignore` :

- `.env` et ses variantes (secrets)
- les fichiers audio volumineux (`*.wav`, `*.mp3`, `*.m4a`) à l'exception d'un `audio/exemple.mp3` léger destiné à la démonstration
- le dossier `outputs/` (comptes rendus générés localement pendant les tests)
- les artefacts Python usuels (environnements virtuels, caches, fichiers compilés)

### Modèles Groq utilisés (Q2)

*À compléter à l'étape 2, une fois les modèles choisis et testés.*

### Format renvoyé par l'API STT (Q3)

*À compléter à l'étape 3.*

### Choix de la température du LLM (Q4)

*À compléter à l'étape 4.*

### Prompt système et tokens en cache (Q5)

*À compléter à l'étape 4.*

---

## Suivi du développement

Le projet suit un workflow inspiré de **GitHub Flow** avec une branche d'intégration :

- `main` — version stable, taguée aux jalons de version (`v0.1.0`, `v0.2.0`...)
- `dev` — branche d'intégration où arrivent les fonctionnalités par pull request
- `feature/<nom>` — une branche par fonctionnalité, courte, mergée puis supprimée

### État des étapes

- [x] **Étape 0** — Mise en place (dépôt, branches, protection de `main`, clé API Groq)
- [x] **Étape 1** — Squelette du projet (README, arborescence, `.gitignore`, `requirements.txt`)
- [ ] Étape 2 — Configuration et chargement des secrets
- [ ] Étape 3 — Transcription (Speech-to-Text via Groq)
- [ ] Étape 4 — Compte rendu (LLM via Groq)
- [ ] Étape 5 — Assemblage en ligne de commande, jalon `v0.1.0`
- [ ] Étape 6 — Résolution d'un conflit de merge imposé
- [ ] Étape 7 (bonus) — Fonctionnalité au choix