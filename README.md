# streamable-archiver
Ce programme permet de télécharger toute les videos de votre [Streamable](https://streamable.com/)  
Mais aussi de les uploadé sur un canal [Telegram](https://telegram.org/)
## Comment utiliser Streamable-archiver
### Déploiement avec docker compose:
Lancée le [docker-compose.yml](https://github.com/louino2478/streamable-archiver/blob/main/docker-compose.yml) en remplacent "/path/to/config" et "path/to/download par votre répertoire précédemment créent.
### Déploiement sans docker compose:
exécuté le conteneur :
```bash
docker run -v "/path/to/config:/config" -v "/path/to/downloads:/downloads" ghcr.io/louino2478/streamable-archiver:latest
```
**Penser à remplacée "/path/to/config" et "path/to/download par votre répertoire précédemment crée.**
### Configuration
Dans le dossier "config/" il y a deux fichiers:
- config.json :  
    "username" <- Votre email Streamable.  
    "password" <- Votre mot de passe Streamable.  
    "enabletelegram" <- 'true' ou 'false' si vous voulais le reupload sur Telegram.  
    "telegramtoken" <- Le token du bot Telegram.  
    "telegramchatid" <- l'ID du groupe/channel Telegram.
- DB.txt  
    Il ne doit pas être modifié. Il permet de stocker la liste des videos déja téléchargées.
