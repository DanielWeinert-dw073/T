# Das Lerngruppen-Tool basiert auf Flask

from flask import Flask

# Die Flask Erweiterung Flask CORS ist für das Ressource Sharing verantwortlich

from flask_cors import CORS

# Zudem wird das auf Flask aufbauende Flask-RestX verwendet

from flask_restx import Api, Resource, fields
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
"""from SecurityDecorator import secured"""


"""Flask wird hiermit instanziiert"""
app = Flask(__name__)

CORS(app, support_credentials=True, resources=r"/LernGruppenToolApp/*")

api = Api(app, version="1.0", title="LernGruppenTool ", description="Web App zur Lerngruppen Findung der Hochschule")

"""Namespaces"""
LernGruppenToolApp = api.namespace("LernGruppenToolApp", description="Funktionen der LerngruppenTool App")

"""Hier wird festgelegt, wie die BusinessObjects beim Marshelling definiert werden sollen"""
bo = api.model("BusinessObject", {
    "id": fields.Integer(attribute="_id", description="ID des BOs"),
    "erstellungszeitpunkt": fields.DateTime(attribute="_erstellungszeitpunk", description="Erstellungszeitpunkt des BOs"),
})

nbo = api.model("NamedBusinessObject", {
    "name": fields.String(attribute="_name", description="Name des BOs"),
})

profil = api.inherit("Profil", nbo, {
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

nachricht = api.inherit("Nachricht", bo, nbo, {
    "inhalt": fields.String(attribute="_inhalt", description="Inhalt der Nachricht")
})

teilnahme = api.inherit("Teilnahme", bo, {
    "teilnehmer": fields.String(attribute="_teilnehmer", description="Teilnehmer einer Teilnahme"),
    "gruppen_id": fields.Integer(attribute="_gruppen_id", description="GruppenId einer Teilnahme"),
    "konversations_id": fields.Integer(attribute="_konversations_id", description="KonversationsId der Teilnahme"),
    "nachricht_id": fields.Integer(attribute="_nachricht_id", description="NachrichtId zur Teilnahme")
})

student = api.inherit("Student", nbo, {
    "email": fields.String(attribute="_email", description="Email eines Studenten"),
    "google_user_id": fields.String(attribute="_google_user_id", description="GoogleUserId eines Studenten")
})

empfehlung = api.inherit("Empfehlung", bo, {
    "empfehlung": fields.String(attribute="_empfehlung", description="Empfehlung"),
    "empfehlungsListe": fields.String(attribute="_empfehlungsListe", description="Empfehlungsliste"),
    "empfehlungGruppe":fields.String(attribute="_empfehlungGruppe", description="Empfehlunggruppe"),
    "empfehlungProfil": fields.String(attribute="_empfehlungProfil", description="EmpfehlungProfil")
})

lerntyp = api.inherit("Lerntyp", bo, {
    "lerntyp": fields.String(attribute="_lerntyp", description="Lerntypbezeichnung")
})

lernvorlieben = api.inherit("Lernvorlieben", bo, {
    "frequenz": fields.String(attribute="_frequenz", description="Frequenz des Lernens"),
    "internet_verbindung": fields.String(attribute="_internet_verbindung", description="InternetVerbindung online/offline"),
    "pole_der_persönlichkeit": fields.String(attribute="pole_der_persönlichkeit", description="Introvertier/Extrovertiert")
})

konversation = api.inherit("Konversation", bo, {
    "nachricht_id": fields.Integer(attribute="_nachricht_id", description="NachrichtId in einer Konversation"),
    "teilnehmer": fields.String(attribute="_teilnehmer", description="Teilnehmer an einer Konversation"),
    "herkunfts_id": fields.Integer(attribute="_herkunfts_id", description="Herkunfts Id einer Nachricht in einer Konversation"),
    "ziel_id": fields.Integer(attribute="_ziel_id", description="Ziel einer Nachricht in Konversation"),
    "inhalt": fields.String(attribute="_inhalt", description="Inhalt in einer Konversation")
})

suggestion_algorithmus = api.inherit("SuggestionAlgorithmus", bo, {
    "lerntyp_Id" :fields.Integer(attribute="_lerntyp_Id", description="LerntypId"),
    "lernvorlieben_Id" : fields.Integer(attribute="_lernvorlieben_Id", description="Lernvorlieben_Id"),
    "profil_Id" : fields.Integer(attribute="_profil_Id", description= "Profil_Id"),
    "gruppen_id": fields.Integer(attribute="_gruppen_id", description="Gruppen Id ")
})

#Student Methoden

@LernGruppenToolApp.route("/studenten")
@LernGruppenToolApp.response(500, 'Falls es zu einem Serverseitigen Fehler kommt.')
@LernGruppenToolApp.param("name", 'Dies ist der name des Studenten')
class StudentListOperations(Resource):
    @LernGruppenToolApp.marshal_with(student)

    #@secured
    def get (self):
        """Auslesen aller Studenten"""

        adm = LerngruppenAdministration()
        studenten = adm.get_alle_studenten()
        return studenten

    #@secured
    def delete (self):
        """Löschen eines Studenten"""



@LernGruppenToolApp.route("/studenten-by-name/<string:name>")
@LernGruppenToolApp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@LernGruppenToolApp.param("name", "Der Name des Studenten")
class StudentByNameOperations(Resource):
    @LernGruppenToolApp.marshal_list_with(student)

    #@secured
    def get (self, name):
        """Auslesen eines bestimmten Studenten Objekt. Nachrichten

        Das auszulesene Objekt wird über den Namen bestimmt."""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_name(name)
        return stud

@LernGruppenToolApp.route("/studenten-by-google-user-id/<string:google_user_id>")
@LernGruppenToolApp.response(500, "Falls es zu einen serverseitigen Fehler kommt")
@LernGruppenToolApp.param("google_user_id", "GoogleUserId des Studenten")
class StudentByGoogle_User_Id(Resource):
    @LernGruppenToolApp.marshal_list_with(student)

    #@secured
    def get (self, google_user_id):
        """Auslesen eines bestimmten Studenten Objekts.

        Das auszulesene Objekt wird über die GoogleUserId bestimmt."""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_google_user_id(google_user_id)
        return stud

@LernGruppenToolApp.route("/studenten-by-id/<int:id>")
@LernGruppenToolApp.response(500, "Falls es zu einen serverseitigen Fehler kommt.")
@LernGruppenToolApp.param("id", "Id eines Studenten")
class StudentById(Resource):
    @LernGruppenToolApp.marshal_list_with(student)

    #@secured
    def get (self, id):
        """Auslesen eines bestimmten Studenten Objekts.

        Das auszulesene Objekt wird über die Id bestimmt"""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_id(id)
        return stud


# Nachrichten Methoden
@LernGruppenToolApp.route("/nachrichten")
@LernGruppenToolApp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class NachrichtListOperation(Resource):

    # @secured
    def get(self):
        """Auslesen aller Nachrichten Objekte"""

        adm = LerngruppenAdministration()
        nachrichten = adm.get_alle_nachrichten()
        return nachrichten

    # @secured
    def put(self):
        """Update der Nachricht"""

        adm = LerngruppenAdministration()
        nachricht = adm.get_nachricht_by_id(id)

        adm.update_nachricht(nachricht)

@LernGruppenToolApp.route("/nachricht/<string:inhalt>")
@LernGruppenToolApp.response(500, "Falls es zu einen serverseitigen Fehler kommt")
@LernGruppenToolApp.param("inhalt")
class NachrichtByInhalt(Resource):
    @LernGruppenToolApp.marshal_list_with(nachricht)
    # @secured
    def get(self, inhalt):
        """Auslesen des Inhaltes einer Nachricht
        Das auszulesene Objekt wird über den Inhalt erfasst.
        """

        adm = LerngruppenAdministration()
        nach = adm.get_nachricht_by_inhalt(inhalt)
        return nach


@LernGruppenToolApp.route("/nachricht/<int:id>")
@LernGruppenToolApp.response(500, "Falls es zu einen serverseitigen Fehler kommt")
@LernGruppenToolApp.param("id")
class NachrichtById(Resource):
    @LernGruppenToolApp.marshal_list_with(nachricht)
    # @secured
    def get(self, id):
        """Auslesen eines bestimmten Nachricht Objekts.

        Das auszulesene Objekt wird über die Id bestimmt"""

        adm = LerngruppenAdministration()
        nach = adm.get_nachricht_by_id(id)
        return nach


# Profil Methoden

@LernGruppenToolApp.route("/profile")
@LernGruppenToolApp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class ProfilListOperation(Resource):
    @LernGruppenToolApp.marshal_list_with(profil)
    # @secured
    def get(self):
        """Auslesen aller Profile"""

        adm = LerngruppenAdministration()
        profile = adm.get_all_profils()
        return profile

    # @secured

    def put(self):
        """ Update des Profils"""

        id = request.args.get("id")
        name = request.args.get("name")
        adm = LerngruppenAdministration()
        profil = adm.get_profil_by_id(id)
        profil.set_faecher(faecher)
        profil.set_alter(alter)
        profil.set_about_me(about_me)
        profil.set_vorwissen(vorwissen)
        profil.set_lerntyp(lerntyp)
        profil.set_lernvorlieben(lernvorlieben)
        profil.set_semester(semester)
        profil.set_studiengang(studiengang)
        adm.update_student(student)

    # @secured
    def delete(self, id):
        """ Löschen eines Profils"""
        adm = LerngruppenAdministration()
        adm.delete_profil(id)



if __name__ == '__main__':
    app.run(debug=True)




