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
from SecurityDecorator import secured


"""Flask wird hiermit instanziiert"""
app = Flask(__name__)

CORS(app, support_credentials=True, resources={r"/lerngruppentoolapp/*":{"origins": "*"}} )

api = Api(app, version="1.0", title="LernGruppenTool ", description="Web App zur Lerngruppen Findung der Hochschule")

"""Namespaces"""
toolapp = api.namespace("lerngruppentoolapp", description="Funktionen der LerngruppenTool App")

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
    "lerntyp_id": fields.Integer(attribute="_lerntyp_id", description="LerntypId"),
    "lernvorlieben_id": fields.Integer(attribute="_lernvorlieben_id", description="Lernvorlieben_Id"),
    "profil_id": fields.Integer(attribute="_profil_id", description="Profil_Id"),
    "gruppen_id": fields.Integer(attribute="_gruppen_id", description="Gruppen Id ")
})

#Student Methoden

@toolapp.route("/studenten")
@toolapp.response(500, 'Falls es zu einem Serverseitigen Fehler kommt.')
@toolapp.param("name", 'Dies ist der name des Studenten')
class StudentListOperations(Resource):
    @toolapp.marshal_list_with(student)

    @secured
    def get(self):
        """Auslesen aller Studenten"""

        adm = LerngruppenAdministration()
        studenten = adm.get_alle_studenten()
        return studenten

    @secured
    def put(self):

        student_Id = request.args.get("userId")
        name = request.args.get("name")
        email = request.args.get("email")
        adm = LerngruppenAdministration()
        student.set_name(name)
        student.set_email(email)
        adm.update_student_by_id(student_Id)

    @secured
    def delete(self):
        """Löschen eines Studenten"""
        adm = LerngruppenAdministration()
        adm.delete_student(id)

    @secured
    def update(self):
        """Update eines Studenten"""

        adm = LerngruppenAdministration()
        studenten = adm.get_student_by_id(id)

        adm.update(studenten)




@toolapp.route("/studenten-by-name/<string:name>")
@toolapp.response(500, 'Falls es zu einem Server-seitigen Fehler kommt.')
@toolapp.param("name", "Der Name des Studenten")
class StudentByNameOperations(Resource):
    @toolapp.marshal_list_with(student)

    @secured
    def get(self, name):
        """Auslesen eines bestimmten Studenten Objekt. Nachrichten

        Das auszulesene Objekt wird über den Namen bestimmt."""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_name(name)
        return stud

@toolapp.route("/studenten-by-google-user-id/<string:google_user_id>")
@toolapp.response(500, "Falls es zu einen serverseitigen Fehler kommt")
@toolapp.param("google_user_id", "GoogleUserId des Studenten")
class StudentByGoogle_User_Id(Resource):
    @toolapp.marshal_list_with(student)

    @secured
    def get (self, google_user_id):
        """Auslesen eines bestimmten Studenten Objekts.

        Das auszulesene Objekt wird über die GoogleUserId bestimmt."""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_google_user_id(google_user_id)
        return stud

@toolapp.route("/studenten/<int:id>")
@toolapp.response(500, "Falls es zu einen serverseitigen Fehler kommt.")
@toolapp.param("id", "Id eines Studenten")
class StudentOperations(Resource):
    @toolapp.marshal_with(student)

    @secured
    def get (self, id):
        """Auslesen eines bestimmten Studenten Objekts.

        Das auszulesene Objekt wird über die Id bestimmt"""

        adm = LerngruppenAdministration()
        stud = adm.get_student_by_id(id)
        return stud


# Nachrichten Methoden
@toolapp.route("/nachrichten")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class NachrichtListOperation(Resource):
    @toolapp.marshal_list_with(nachricht)

    @secured
    def get(self):
        """Auslesen aller Nachrichten Objekte"""

        
        adm = LerngruppenAdministration()
        nachricht = adm.get_all_nachricht()
        return nachricht

    @secured
    def put(self, id):
        """Update der Nachricht"""

        adm = LerngruppenAdministration()
        nachricht = adm.get_nachricht_by_id(id)

        adm.update(nachricht)

    @toolapp.marshal_list_with(nachricht, code= 200)
    @toolapp.expect(nachricht)
    @secured
    def post(self):
        """ Anlegen einer neuen Nachricht"""

        profil_Id = request.args.get("profil_Id")
        gruppen_id = request.args.get("gruppen_id")
        
        adm = LerngruppenAdministration()
        adm.create_nachricht(profil_Id, gruppen_id)
        nachricht = Nachricht.from_dict(api.playload)


        if nachricht is not None:
        
            n = adm.create_nachricht(nachricht)
            return n, 200
        else: 
            return '',500

    def delete(self, id):
            """ Löschen einer Nachricht"""
            adm = LerngruppenAdministration()
            nach = adm.get_nachricht_by_id(id)
            adm.delete_nachricht(nach)
            return "", 200


@toolapp.route("/nachricht/<int:id>")
@toolapp.response(500, "Falls es zu einen serverseitigen Fehler kommt")
@toolapp.param("id")
class NachrichtById(Resource):
    @toolapp.marshal_list_with(nachricht)
    @secured
    def get(self, id):
        """Auslesen eines bestimmten Nachricht Objekts.

        Das auszulesene Objekt wird über die Id bestimmt"""

        adm = LerngruppenAdministration()
        nach = adm.get_nachricht_by_id(id)
        return nach


# Profil Methoden

@toolapp.route("/profile")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class ProfilListOperation(Resource):
    @toolapp.marshal_list_with(profil)
    @secured
    def get(self):
        """Auslesen aller Profile"""

        adm = LerngruppenAdministration()
        profile = adm.get_all_profils()
        return profile

    @secured

    def put(self, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen):
        """ Update des Profils"""

        id = request.args.get("id")
        name = request.args.get("name")
        adm = LerngruppenAdministration()
        profil = adm.get_profil_by_id(id)
        profil.set_faecher(faecher)
        profil.set_alter(alter)
        profil.set_wohnort(wohnort)
        profil.set_about_me(about_me)
        profil.set_vorwissen(vorwissen)
        profil.set_lerntyp(lerntyp)
        profil.set_lernvorlieben(lernvorlieben)
        profil.set_semester(semester)
        profil.set_studiengang(studiengang)
        profil.set_sprachen(sprachen)
        adm.update_profil()

    @secured
    def delete(self, id):
        """ Löschen eines Profils"""
        adm = LerngruppenAdministration()
        adm.delete_profil(id)

    @toolapp.marshal_list_with(profil, code = 200)
    @toolapp.expect(profil)

    @secured
    def post(self):
        """ Anlegen eines Profils"""

        adm = LerngruppenAdministration()
        profil = Profil.from_dict(api.payload)
        adm.create_profil()

        if profil is not None:
            result = adm.create_profil(profil.set_name(),profil.set_alter(),
                                 profil.set_studiengang(),profil.set_wohnort(),profil.set_semester(),profil.set_about_me(),
                                 profil.set_vorwissen(),profil.set_lernvorlieben(),profil.set_sprachen())
            return result, 200
        else:
            return '', 500


# Teilnahme Methoden

@toolapp.route("/teilnahmen")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class TeilnahmeListOperation(Resource):
    @toolapp.marshal_list_with(teilnahme)
    @secured
    def get(self):
        """Auslesen aller Teilnahmen"""

        adm=LerngruppenAdministration()
        teilnahmen = adm.get_alle_teilnahmen()
        return teilnahmen

    @secured
    def put(self):
            """Update der Teilnahmen"""

            adm = LerngruppenAdministration()
            teilnahme = adm.get_teilnahme_id(id)

            adm.update(teilnahme)

    @secured
    def delete(self, id):
        """ Löschen einer Teilnahme"""
        adm = LerngruppenAdministration()
        adm.delete_teilnahme(id)

    @secured
    def post(self):
        """ Anlegen einer Teilnahme"""
        adm = LerngruppenAdministration()
        adm.post_teilnahme()

# Empfehlungs Methoden

@toolapp.route("/empfehlungen")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class EmpfehlungListOperation(Resource):
    @toolapp.marshal_list_with(empfehlung)

    @secured
    def get(self):
        """Auslesen aller Empfehlungen"""

        adm = LerngruppenAdministration()
        empfehlungen = adm.get_all_empfehlungen()
        return empfehlungen

    @secured
    def put(self):
        """Update der Empfehlung"""

        adm = LerngruppenAdministration()
        empfehlungen = adm.get_empfehlung_by_id(id)
        adm.update(teilnahme)

    @secured
    def delete(self, id):
        """ Löschen einer Empfehlung"""

        adm = LerngruppenAdministration()
        adm.delete_empfehlung(id)

    @secured
    def post(self):
        """Anlegen einer Empfehlung"""
        adm= LerngruppenAdministration()
        adm.post_empfehlung()

# Lerntyp Methoden

@toolapp.route("/lerntypen")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class EmpfehlungListOperation(Resource):
    @toolapp.marshal_list_with(lerntyp)

    @secured
    def get(self):
        """Auslesen aller Lerntypen"""

        adm = LerngruppenAdministration()
        lerntypen = adm.get_all_lerntypen()
        return lerntypen

    @secured
    def put(self):
        """Update der Lerntypen"""

        adm = LerngruppenAdministration()
        lerntypen = adm.get_lerntyp_by_id(id)
        adm.update(lerntypen)

    @secured
    def delete(self, id):
        """ Löschen eines Lerntypen"""

        adm = LerngruppenAdministration()
        adm.delete_lerntyp(id)

    @secured
    def post(self):
        """Anlegen eines Lerntypen"""
        adm = LerngruppenAdministration()
        adm.post_lerntyp()

# Lernvorlieben Methoden

@toolapp.route("/lernvorlieben")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class EmpfehlungListOperation(Resource):
    @toolapp.marshal_list_with(lernvorlieben)

    @secured
    def get(self):
        """Auslesen aller Lernvorlieben"""

        adm = LerngruppenAdministration()
        lernvorlieben = adm.get_all_lernvorlieben()
        return lernvorlieben

    @secured
    def put(self):
        """Update der Lernvorlieben"""

        adm = LerngruppenAdministration()
        lernvorlieben = adm.get_lernvorliebe_by_id(id)
        adm.update(lernvorlieben)

    @secured
    def delete(self, id):
        """ Löschen einer Lernvorliebe"""

        adm = LerngruppenAdministration()
        adm.delete_lernvorlieben(id)

    @secured
    def post(self):
        """Anlegen einer Lernvorliebe"""
        adm = LerngruppenAdministration()
        adm.post_lernvorlieben()

@toolapp.route("/konversationen")
@toolapp.response(500, "Falls es zu einem serverseitigen Fehler kommt")
class KonversationListOperation(Resource):
    @toolapp.marshal_list_with(konversation)

    @secured
    def get(self):
        """Auslesen aller Konversationen"""

        adm = LerngruppenAdministration()
        konversationen = adm.get_all_konversationen()
        return konversationen

    @secured
    def put(self):
        """Update der Konversationen"""

        adm = LerngruppenAdministration()
        konversationen = adm.get_konversation_by_id(id)
        adm.update(konversationen)

    @secured
    def delete(self, id):
        """ Löschen einer Konversation"""

        adm = LerngruppenAdministration()
        adm.delete_konversation(id)

    @secured
    def post(self):
        """Anlegen einer Konversation"""
        adm= LerngruppenAdministration()
        adm.post_konversation()


if __name__ == '__main__':
    app.run(debug=True)




