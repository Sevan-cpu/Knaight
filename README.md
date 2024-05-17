# Projet de Démonstration IAG avec LLM

## Introduction

Ce projet est une plateforme de démonstration conçue pour explorer les capacités des modèles de langage de grande taille (LLM) dans un contexte de production. Il vise à évaluer les performances de streaming et de parallélisation des requêtes sur des modèles open-source comme ceux de HuggingFace, LlamaCpp, et CustomLLM. Le projet utilise Docker pour faciliter le déploiement et assurer la compatibilité sur différentes architectures, rendant ainsi la solution adaptable et facile à déployer pour des tests ou des démonstrations.

## Structure du Projet

### Backend

Le backend sert de fondation au traitement des requêtes et à l'exécution des modèles LLM. Voici une description détaillée des composants clés :

- **`app.py`** : Implémente l'application FastAPI qui expose des endpoints API pour interagir avec le frontend. Ce fichier configure les routes pour recevoir les données de l'utilisateur et envoyer des tâches de génération de texte à des travailleurs en arrière-plan.
- **`celery_worker.py`** : Définit les tâches Celery qui gèrent l'exécution asynchrone des requêtes. Ce module est crucial pour la parallélisation des opérations et permet d'assurer une haute disponibilité et une réponse rapide des services.
- **`model_loader.py`** : Charge et configure les modèles LLM à partir de chemins spécifiés. Ce script est essentiel pour s'assurer que les bons modèles sont prêts à être utilisés dès que l'API reçoit une demande.
- **`redis_server.py`** : Configure et gère les interactions avec le serveur Redis, qui est utilisé pour la mise en cache et la gestion de l'état des requêtes en cours. Cela permet une récupération rapide des résultats et une gestion efficace des sessions utilisateur.
- **`utils.py`** : Fournit des fonctions auxiliaires qui aident avec le formatage des réponses, la gestion des erreurs, et d'autres tâches communes à travers l'application.

### Frontend

Le frontend offre une interface conviviale pour interagir avec le backend via une interface de chat, ce qui rend les tests et démonstrations plus accessibles :

- **`modeling.py`** : Utilise Streamlit pour créer une interface graphique où les utilisateurs peuvent soumettre des prompts et recevoir des réponses des modèles. Cette interface visualise les interactions en temps réel et permet une évaluation directe des performances du modèle.

## Mise en Place

### Prérequis

Avant de démarrer, assurez-vous que Docker et Docker Compose sont installés sur votre machine. Ces outils sont essentiels pour construire et exécuter les conteneurs nécessaires au projet.

### Installation

Pour installer et démarrer le projet, suivez ces étapes :

1. **Clonage du dépôt** :

git clone https://votre-repertoire/projet.git

2. **Navigation dans le répertoire du projet** :

cd chemin_vers_le_projet

3. **Construction des images Docker** :

docker-compose up --build


### Utilisation

Après le démarrage du projet, l'interface utilisateur de Streamlit sera accessible via : http://localhost:8501


Vous pouvez interagir avec le système en entrant des prompts dans le chat. Le système enverra ces prompts au backend qui, à son tour, retournera les réponses générées par les modèles LLM. Les interactions sont visualisées dans une fenêtre de chat, permettant une évaluation visuelle et technique des capacités du modèle.

## Conclusion

Ce projet offre une plateforme robuste pour tester et démontrer les capacités des technologies LLM open-sources dans un environnement contrôlé. Il permet aux développeurs et chercheurs d'évaluer les performances des modèles dans des conditions réelles et d'ajuster les paramètres pour des déploiements optimisés.


## Lien des sites utilisés

### Streaming :

https://github.com/jaswanth04/llm_response_streaming/blob/main/src/handlers.py

https://medium.com/@shrinath.suresh/implementing-streaming-chatbot-with-langchain-callbacks-a-step-by-step-guide-a527a7d65b8b

https://dev.to/suzuki0430/implementing-real-time-responses-with-langchain-and-llm-537h



### Custom LLM:

https://linuxhint.com/create-custom-llm-wrapper-langchain/

https://medium.com/@shrinath.suresh/building-an-interactive-streaming-chatbot-with-langchain-transformers-and-gradio-93b97378353e



### Parallel Request:

https://blog.stackademic.com/fastapi-parallel-processing-1eaa67981ab9

https://fastapi.tiangolo.com/async/

https://freedium.cfd/https://towardsdatascience.com/leveraging-llama-2-features-in-real-world-applications-building-scalable-chatbots-with-fastapi-406f1cbeb935

### Deployment (Docker) and process:

https://fastapi.tiangolo.com/deployment/concepts/

https://fastapi.tiangolo.com/deployment/docker/#multiple-containers

https://rihab-feki.medium.com/deploying-machine-learning-models-with-streamlit-fastapi-and-docker-bb16bbf8eb91

https://github.com/george-mountain/LLM-Local-Streaming/tree/main

https://www.nicelydev.com/docker/reseau-docker-compose



### Celery/Redis:

https://testdriven.io/courses/fastapi-celery/getting-started/

https://github.com/luisroque/large_laguage_models/tree/main

https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db