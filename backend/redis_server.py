# Importation des modules nécessaires pour la gestion des processus et l'utilisation de Redis
import subprocess
import redis_server  # Import hypothétique d'un module pour la configuration du serveur Redis

# Fonction pour installer le serveur Redis à l'aide de pip
def install_redis_server(redis_version):
    try:
        # Exécute la commande pip pour installer une version spécifique du serveur Redis
        subprocess.check_call(["pip", "install", f"redis-server=={redis_version}"])
        print(f"Redis server version {redis_version} installed successfully.")  # Affiche un message en cas de succès
    except subprocess.CalledProcessError:
        # Gère les erreurs lors de l'installation et affiche un message d'erreur
        print("Failed to install Redis server.")
        exit(1)  # Quitte le programme avec un code d'erreur

# Fonction pour démarrer le serveur Redis
def start_redis_server():
    try:
        # Récupère le chemin du fichier exécutable du serveur Redis depuis le module redis_server
        redis_server_path = redis_server.REDIS_SERVER_PATH
        subprocess.Popen([redis_server_path])  # Lance le serveur Redis
        print("Redis server started successfully.")  # Affiche un message en cas de succès
    except Exception as e:
        # Gère les exceptions génériques et affiche les erreurs
        print("Failed to start Redis server:", str(e))
        exit(1)  # Quitte le programme avec un code d'erreur

# Fonction principale qui orchestre l'installation et le démarrage du serveur Redis
def main():
    redis_version = "6.0.9"  # Définit la version de Redis à installer
    install_redis_server(redis_version)  # Appelle la fonction d'installation
    start_redis_server()  # Appelle la fonction de démarrage du serveur

# Point d'entrée du script Python, vérifie si le script est exécuté directement
if __name__ == "__main__":
    main()  # Exécute la fonction main si le script est lancé directement
