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

class NullableInteger(fields.Integer):
    """Diese Klasse ist für die Umsetzung eines Integers mit dem Wert null zuständig"""

    __schema_type__ = ["integer", "null"]
    __schema_example__ = "nullable integer"

"""Flask wird hiermit instanziiert"""
app = Flask(__name__)

CORS(app, support_credentials=True, resources={r"/LernGruppenToolApp/*":{"origins": "*"}})

api = API(app,version = "1.0", title = "LernGruppenTool API", 
            description="Web App zur Lerngruppen Findung der Hochschule")

"""Namespaces"""
LernGruppenToolApp = api.namespace("LernGruppenToolApp", description="Funktionen der LerngruppenTool App")

"""Hier wird festgelegt, wie die BusinessObjects beim Marshelling definiert werden sollen"""
bo = api.model("BusinessObject", {
    "id": fields.Integer(attribute="_id",description="ID des Bos"),
})

nbo = api.inherit("NamedBusinessObject",bo,{
    "name": fields.String(attribute="_name", description="Name des BOs"),
})

profil = api.inherit("Profil",nbo,{
    "faecher": fields.String(attribute="_faecher", description="Faecher des Profils"),
    "alter": fields.Integer(attribute="_alter", description="Alter des Profils"),
    "studiengang": fields.String(attribute="_studiengang", description="Studiengang des Profils"),
    "wohnort": fields.String(attribute="_wohnort", description="Wohnort des Profils"),
    "semester": fields.Integer(attribute="_semester", description="Semester des Profils"),
    "vorwissen": fields.String(attribute="_vorwissen", description="Vorwissen des Profils"),
    "lernvorlieben": fields.String(attribute="_lernvorlieben", description="Lernvorlieben des Profils"),
    "about_me": fields.String(attribute="_about_me", description="AboutMe des Profils"),
    "sprachen": fields.String(attribute="_sprachen", description="Sprachen des Profils")
})

nachricht = api.inherit("Nachricht",bo,{
    "inhalt": fields.String(attribute="_inhalt", description="Inhalt der Nachricht")
})

teilnahme = api.inherit("Teilnahme",bo,{
    "teilnehmer": fields.String(attribute="_teilnehmer", description="Teilnehmer einer Teilnahme"),
    "gruppen_id": fields.Integer(attribute="_gruppen_id", description="GruppenId einer Teilnahme"),
    "konversations_id": fields.Integer(attribute="_konversations_id", description="KonversationsId der Teilnahme"),
    "nachricht_id": fields.Integer(attribute="_nachricht_id", description="NachrichtId zur Teilnahme")
})

