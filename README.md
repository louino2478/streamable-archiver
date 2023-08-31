# streamable-archiver

/!\ ce programme est expérimental, il peut donc contenir des bug. /!\

Ce programme permet de télécharger toute les videos de votre [Streamable](https://streamable.com/) et puis de les uploadé sur un canal [Telegram](https://telegram.org/)

## comment utiliser streamable-archiver
### pré requis:
1. commençais par crée deux répertoires sur votre serveur, "config/" et "download/".
2. copier le "config.sample.json" dans votre dossier config/ et renommer le "config.json"
3. configuré le fichier config.json avec vos identifiant streamable, votre token telegram de votre bot et l'id du channels Telegram.
4. ajouter un fichier vide "DB.txt" dans votre dossier config/ (il servira a noté automatiquement les videos déjà téléchargé)
### avec docker compose:
5. lancée le docker-compose.yml en remplacent "/path/to/config" et "path/to/download par votre répertoire précédemment crée.
### sans docker compose:
5. exécuté le conteneur :
```bash
docker run -v "/path/to/config:/config" -v "/path/to/downloads:/downloads" ghcr.io/louino2478/streamable-archiver:latest
```
penssé a remplacée "/path/to/config" et "path/to/download par votre répertoire précédemment crée.
