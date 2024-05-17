# Importation des bibliothèques nécessaires
from fastapi import FastAPI
from pydantic import BaseModel
from celery.result import AsyncResult
from typing import Any
from celery_worker import generate_text_task

# Création de l'instance de l'application FastAPI
app = FastAPI()

# Définition d'une classe de modèle pour les données entrantes, utilisant Pydantic
class Item(BaseModel):
    prompt: str  # Une propriété `prompt` de type chaîne de caractères est requise

# Définition d'un endpoint POST pour générer du texte à partir d'un prompt
@app.post("/generate/")
async def generate_text(item: Item) -> Any:
    # Soumission du prompt à la tâche Celery et récupération de l'identifiant de la tâche
    task = generate_text_task.delay(item.prompt)
    return {"task_id": task.id}  # Retour de l'identifiant de la tâche au client

# Définition d'un endpoint GET pour récupérer le résultat d'une tâche spécifique
@app.get("/task/{task_id}")
async def get_task(task_id: str) -> Any:
    # Récupération du résultat de la tâche par son ID
    result = AsyncResult(task_id)
    # Vérification si le résultat de la tâche est prêt
    if result.ready():
        res = result.get()  # Obtention du résultat de la tâche
        return {"result": res[0],  # Renvoi du résultat
                "time": res[1],    # Renvoi du temps de traitement
                "memory": res[2]}  # Renvoi de l'utilisation mémoire
    else:
        return {"status": "Task not completed yet"}  # Si la tâche n'est pas encore complétée
