# Commandes
## Construire l'image à partir d'un Dockerfile
docker build -t [nom:tag] [Fichier dans lequel est présent le Dockerfile]
## Lancer et arreter un conteneur
### Créer un container à partir d'une image
docker run --name [nom] [image]
### Stopper un conteneur
docker stop [nom]
### Relancer un container aretté 
docker start [nom]
## Voir les container et images
### Voir les containers en activité
docker ps
### Voir tout les container
docker ps -a
### Voir les images
docker ps
