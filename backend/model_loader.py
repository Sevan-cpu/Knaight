# Importation des modules nécessaires pour la gestion des variables d'environnement et le chargement des modèles
import os
from transformers import AutoModelForCausalLM, AutoConfig, AutoTokenizer  # Importation des outils de Hugging Face pour les modèles de traitement du langage
from dotenv import load_dotenv  # Importation de dotenv pour charger les variables d'environnement depuis un fichier .env

load_dotenv()  # Charge les variables d'environnement du fichier .env situé dans le même répertoire ou spécifié

# Définition d'une classe pour charger les modèles de langage
class ModelLoader:
    def __init__(self, model_path: str):
        self.model_path = model_path  # Stockage du chemin d'accès au modèle
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)  # Chargement du tokenizer pour le modèle spécifié
        self.model = self._load_model()  # Chargement du modèle lui-même

    def _load_model(self):
        # Cette méthode charge un modèle de langage causal depuis le chemin spécifié
        model = AutoModelForCausalLM.from_pretrained(self.model_path, trust_remote_code=True)  # Option pour faire confiance au code distant lors du chargement
        return model  # Retourne l'instance du modèle chargé
