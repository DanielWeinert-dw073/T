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
from server.bo.Suggestion_Algorithmus import Suggestion_Algorithmus
from server.bo.Nachricht import Nachricht
from server.bo.Lernvorlieben import Lernvorlieben
from server.bo.Lerntyp import Lerntyp



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

student = api.inherit("Student",nbo,{
    "email": fields.String(attribute="_email", description="Email eines Studenten"),
    "google_user_id": fields.String(attribute="_google_user_id", description="GoogleUserId eines Studenten")
})

empfehlung = api.inherit("Empfehlung",bo,{
    "empfehlung": fields.String(attribute="_empfehlung", description="Empfehlung"),
    "empfehlungsListe": fields.String(attribute="_empfehlungsListe", description="Empfehlungsliste"),
    "empfehlungGruppe":fields.String(attribute="_empfehlungGruppe", description="Empfehlunggruppe"),
    "empfehlungProfil": fields.String(attribute="_empfehlungProfil", description="EmpfehlungProfil")
})

lerntyp = api.inherit("Lerntyp",bo,{
    "lerntyp": fields.String(attribute="_lerntyp", description="Lerntypbezeichnung")
})

lernvorlieben = api.inherit("Lernvorlieben",bo,{
    "frequenz": fields.String(attribute="_frequenz", description="Frequenz des Lernens"),
    "internet_verbindung": fields.String(attribute="_internet_verbindung", description="InternetVerbindung online/offline"),
    "pole_der_persönlichkeit": fields.String(attribute="pole_der_persönlichkeit", description="Introvertier/Extrovertiert")
})

konversation = api.inherit("Konversation",bo,{
    "nachricht_id": fields.Integer(attribute="_nachricht_id", description="NachrichtId in einer Konversation"),
    "teilnehmer": fields.String(attribute="_teilnehmer", description="Teilnehmer an einer Konversation"),
    "herkunfts_id": fields.Integer(attribute="_herkunfts_id", description="Herkunfts Id einer Nachricht in einer Konversation"),
    "ziel_id": fields.Integer(attribute="_ziel_id", description="Ziel einer Nachricht in Konversation"),
    "inhalt": fields.String(attribute="_inhalt", description="Inhalt in einer Konversation")
})

suggestion_algorithmus = api.inherit("SuggestionAlgorithmus",bo,{
    "lerntyp_Id" :fields.Integer(attribute="_lerntyp_Id", description="LerntypId"),
    "lernvorlieben_Id" : fields.Integer(attribute="_lernvorlieben_Id", description="Lernvorlieben_Id"),
    "profil_Id" : fields.Integer(attribute="_profil_Id", description= "Profil_Id"),
    "gruppen_id": fields.Integer(attribute="gruppen_id", description="Gruppen Id ")
})




