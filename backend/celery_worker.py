# Importation des bibliothèques nécessaires pour la mise en place de tâches asynchrones avec Celery
from celery import Celery, signals
from utils import generate_output  # Importation d'une fonction utilitaire pour générer une sortie
from langchain_community.llms import LlamaCpp  # Importation du modèle LlamaCpp pour le traitement du langage naturel

# from handlers import MyCustomHandler  # Importation commentée d'un gestionnaire personnalisé

# Fonction pour créer une instance de Celery configurée
def make_celery(app_name=__name__):
    backend = broker = 'redis://redis:6379/0'  # Définition des paramètres du backend et du broker Redis
    return Celery(app_name, backend=backend, broker=broker, broker_connection_retry_on_startup=True)

celery = make_celery()  # Création de l'instance Celery

llm = None  # Initialisation de la variable `llm` pour stocker l'instance du modèle
model_path = "model/phi-2.Q4_K_M.gguf"  # Chemin d'accès au modèle pré-entraîné

# Définition d'un gestionnaire qui s'exécute lors de l'initialisation du processus de travail
@signals.worker_process_init.connect
def setup_model(signal, sender, **kwargs):
    global llm  # Utilisation de la variable globale `llm`
    llm_cpp = LlamaCpp(
        model_path=model_path,  # Chemin du modèle
        temperature=0,  # Température pour la génération de texte
        max_tokens=500,  # Nombre maximal de jetons
        top_p=1,  # Paramètre top_p pour le contrôle de la diversité
        # callbacks=callbacks,  # Paramètre commenté pour des rappels
        verbose=True  # Activation du mode verbeux
    )
    llm = llm_cpp  # Stockage de l'instance du modèle dans `llm`

# Définition d'une tâche Celery pour générer du texte à partir d'un prompt
@celery.task
def generate_text_task(prompt):
    memory, time, outputs = generate_output(  # Génération de la sortie avec utilisation mémoire et temps de traitement
        prompt, llm
    )
    return outputs, time, memory  # Retour des résultats, du temps et de la mémoire utilisée
