# Importation des bibliothèques nécessaires pour la manipulation du temps, des tensors et des utilitaires de fonctions
import time
import torch
import functools
import psutil  # Bibliothèque utilisée pour accéder aux informations sur l'utilisation du système

# Décorateur pour mesurer le temps d'exécution d'une fonction
def time_decorator(func):
    @functools.wraps(func)  # Utilise wraps pour préserver les métadonnées de la fonction originale
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Capture le temps au début de l'exécution
        result = func(*args, **kwargs)  # Exécute la fonction décorée
        end_time = time.time()  # Capture le temps à la fin de l'exécution
        exec_time = end_time - start_time  # Calcule le temps d'exécution
        return (result, exec_time)  # Retourne le résultat de la fonction et le temps d'exécution
    return wrapper

# Décorateur pour mesurer la consommation de mémoire pendant l'exécution d'une fonction
def memory_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        ram_info = psutil.virtual_memory()  # Obtient des informations sur la mémoire virtuelle du système
        peak_mem_consumption = ram_info.used / 1024 / 1024 / 1024  # Calcule la consommation de mémoire en Go
        result, exec_time = func(*args, **kwargs)  # Exécute la fonction décorée
        return round(peak_mem_consumption,2), round(exec_time,2), result  # Retourne la consommation mémoire, le temps d'exécution arrondis, et le résultat
    return wrapper

# Utilisation des décorateurs pour enrichir la fonction `generate_output`
@memory_decorator  # Premier décorateur appliqué pour mesurer la mémoire
@time_decorator  # Second décorateur appliqué pour mesurer le temps
def generate_output(prompt, llm):
    outputs = llm(prompt)  # Exécute une fonction de modèle de langage avec le prompt donné
    return outputs  # Retourne les sorties du modèle

# Le décorateur de temps est exécuté en premier suivi par le décorateur de mémoire lors de l'exécution de `generate_output`
