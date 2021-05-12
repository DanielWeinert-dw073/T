# Das Lerngruppen-Tool basiert auf Flask

from flask import Flask

# Die Flask Erweiterung Flask CORS ist für das Ressource Sharing verantwortlich

from flask_cors import CORS

# Zudem wird das auf Flask aufbauende Flask-RestX verwendet

from flask_restx import API, Resource, fields
from flask import request
import json 

#Zugriff auf die Applikationslogik inkl. BusinessObject-Klassen 
from server.LerngruppenAdministration import LerngruppenAdministration
from server.bo.Teilnahme import Teilnahme
from server.bo.Gruppe import Gruppe
from server.bo.Konversation import Konversation
from server.bo.Profil import Profil
from server.bo.Student import Student
from server.bo.Gruppenempfehlung import Gruppenempfehlung 


# SercurityDecorator
from SecurityDecorator import secured