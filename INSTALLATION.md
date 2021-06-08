# Installationsanleitung

## Client Seite

Der Client besteht aus einem React-Frontend welches erst einmal über create-react-app gebootstrapt werden muss. Der Quellcode des Projekts liegt in "/frontend".


## Requirements

1. [Node.js](https://nodejs.org/en/)
2. Packages. Diese Können über den Paketmanager `npm install [package]` installiert werden.
	1. [React Router](https://reactrouter.com/)
	2. [Material-UI](https://material-ui.com/)
	3. [Google firebase-auth](https://firebase.google.com/docs/auth)

## Backend / Server

Der Python Server baut auf Python, Flask sowie RestX auf.

### Start des Development-Server

Der Dev-Server wird in einem Terminal mit dem Kommando `npm start` gestartet. Nach erfolgreichem Start ist die React-App unter http://localhost:3000 verfügbar.
### Deployment auf dem flask-Server

Wenn die App auf einem Hoster AWS, Google oder Azure veröffentlich/deployt werden muss ein produktionsreifer build mit `npm run build` erstellt. Der nun erstellte Build muss in den Ordner `/src/static` abgelegt werden.
### Installation
Der Python Server baut auf Python, Flask sowie RestX auf.
Installiert werden müssen folgende Packages: 
1. Aktuelle Python-Installation (siehe python.org)
2. Flask (darin enthalten sind auch *Werkzeug* und *Jinja*)
3. flask-restx
4. flask-cors 
5. google-auth
6. requests


### Backend starten

[/src] verzeichnis als Source Root wählen und in Pycharm anschließend die [main.py] starten. Erreichbar ist das backend im Debug mode anschließend über 
"""http://127.0.0.1:5000/"""