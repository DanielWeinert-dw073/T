#!/usr/bin/python
# -*- coding: utf-8 -*-

from .bo.Profil import Profil
from .bo.Student import Student
from .bo.Teilnahme import Teilnahme
from .bo.Konversation import Konversation
from .bo.Gruppe import Gruppe
from .bo.Empfehlung import Empfehlung
from .bo.Nachricht import Nachricht
from .bo.Lerntyp import Lerntyp
from .bo.Lernvorlieben import Lernvorlieben

from .db.ProfilMapper import ProfilMapper
from .db.StudentMapper import StudentMapper
from .db.TeilnahmeMapper import TeilnahmeMapper
from .db.KonversationMapper import KonversationMapper
from .db.GruppeMapper import GruppeMapper
from .db.NachrichtMapper import NachrichtMapper
from .db.EmpfehlungMapper import EmpfehlungMapper
from .db.LerntypMapper import LerntypMapper
from .db.LernvorliebenMapper import LernvorliebenMapper


def get_student_by_google_user_id(google_user_id):
    """Einen Studenten anhand seiner Google User Id auslesen"""
    with StudentMapper() as mapper:
        return mapper.find_by_google_user_id(google_user_id)


class LerngruppenAdministration(object):

    """ Diese Klasse ist für die Verbindung der API via Flask (siehe main.py) 
    mit der DB-Anbindung (Mapper-Klassen) zuständig."""

    def __init__(self):
        pass

    """
    Student Methoden
    """

    def create_student(self, name, email, google_user_id):
        """Einen Studenten anlegen"""

        user = Student()
        user.set_name(name)
        user.set_email(email)
        user.set_google_user_id(google_user_id)
        user.set_id(1)

        with StudentMapper() as mapper:
            return mapper.insert(user)

    def get_alle_studenten(self):
        """Alle Studenten auslesen"""
        with StudentMapper() as mapper:
            return mapper.find_all()

    def get_student_by_name(self, name):
        """Einen Studenten über seinen Namen bekommen"""
        with StudentMapper() as mapper:
            return mapper.find_by_name(name)

    def get_student_by_id(self, id):
        """Einen Studenten über seine Id bekommen"""
        with StudentMapper() as mapper:
            return mapper.find_by_id(id)

    def save_student(self, student):
        """Einen Studenten speichern"""
        with StudentMapper() as mapper:
            return mapper.update(student)

    """
    Profil Methoden
    """

    def create_profil(self, name, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen):
        """Ein Profil erstellen"""
        user = Profil()
        user.set_name(name)
        user.set_alter(alter)
        user.set_studiengang(studiengang)
        user.set_wohnort(wohnort)
        user.set_semester(semester)
        user.set_vorwissen(vorwissen)
        user.set_lernvorlieben(lernvorlieben)
        user.set_about_me(about_me)
        user.set_sprachen(sprachen)
        user.set_id(1)

        with ProfilMapper() as mapper:
            return mapper.insert(user)

    def get_profil_by_id(self, id):
        """Ein Profil mit einer bestimmten Id auslesen"""
        with ProfilMapper() as mapper:
            return mapper.find_by_id(id)

    def get_all_profils(self):
        """Alle Profile auslesen"""
        with ProfilMapper() as mapper:
            return mapper.find_all()

    def get_profil_by_name(self, name):
        """Ein Profil über den Namen bekommen"""
        with ProfilMapper() as mapper:
            return mapper.find_by_name(name)

    def save_profil(self,profil):
        """Einen Studenten speichern"""
        with ProfilMapper() as mapper:
            mapper.update(profil)

    def delete_profil(self,profil):
        """Das gewählte Profil löschen"""
        with ProfilMapper() as mapper:
            mapper.delete(profil)

    def delete_profil(self,id):
        """Das gewählte Profil löschen über die Id"""
        with ProfilMapper() as mapper:
            mapper.delete(id)

    def get_profil_by_lernvorlieben(self, lernvorlieben):
        """ Profile nach Lernvorlieben auslesen"""
        with ProfilMapper() as mapper:
            return mapper.find_by_lernvorlieben(lernvorlieben)

    def get_profil_by_lerntyp_Id(self,lerntyp_id):
        """ Profile nach dem Lerntyp ausgeben"""
        with ProfilMapper() as mapper:
            return mapper.find_by_lerntyp_Id(lerntyp_id)

    def update_profil(self, id):
        with ProfilMapper() as mapper:
            mapper.profil

    """
    Lerntyp Methoden
    """

    def create_lerntyp(self, id,lerntyp):
        """Lerntyp anlegen"""
        lerntyp = Lerntyp()
        lerntyp.set_id(id)
        lerntyp.set_lerntyp(lerntyp)
        
        with LerntypMapper() as mapper:
            return mapper.insert(lerntyp)

    def get_lerntyp_by_lerntyp(self, lerntyp):
        """Den gewählten Lerntyp auslesen"""
        with LerntypMapper() as mapper:
            return mapper.find_by_lerntyp(lerntyp)

    def get_lerntyp_by_id(self, id):
        """Den gewählten Lerntyp über die Id auslesen"""
        with LerntypMapper() as mapper:
            return mapper.find_by_id(id)

    def save_lerntyp(self, lerntyp):
        """Lerntyp speichern"""
        with LerntypMapper() as mapper:
            return mapper.update(lerntyp)

    def delete(self, lerntyp):
        """Lerntyp löschen"""
        with LerntypMapper() as mapper:
            return mapper.delete(lerntyp)


    """
    Lernvorlieben Methoden
    """

    def create_lernvorlieben(self, id, frequenz, internet_verbindung, pole_der_persönlichkeit):
        """Lernvorlieben anlegen"""
        lernvorlieben = Lernvorlieben()
        lernvorlieben.set_id(id)
        lernvorlieben.set_frequenz(frequenz)
        lernvorlieben.set_internet_verbindung(internet_verbindung)
        lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)

        with LernvorliebenMapper() as mapper:
            return mapper.insert(lernvorlieben)

    def save_lernvorlieben(self, lernvorlieben):
        """Lernvolieben speichern"""
        with LernvorliebenMapper() as mapper:
            return mapper.update(lernvorlieben)

    def delete(self,lernvorlieben):
        """Lernvorlieben löschen"""
        with LerntypMapper() as mapper:
            return mapper.delete(lernvorlieben)

    def get_lernvorlieben(self,id):
        """Ausgeben der Lernvorlieben über die ID"""
        with LernvorliebenMapper() as mapper:
            return mapper.find_by_id(id)


    """
    Gruppen Methoden
    """

    def create_gruppe(self,id, name, anzahlTeilnehmer, teilnehmerListe, max_teilnehmer):
        """Gruppe erstellen"""
        gruppe = Gruppe()
        gruppe.set_id(id)
        gruppe.set_name(name)
        gruppe.set_anzahlTeilnehmer(anzahlTeilnehmer)
        gruppe.set_teilnehmerListe(teilnehmerListe)
        gruppe.set_max_teilnehmer(max_teilnehmer)

        with GruppeMapper() as mapper:
            return mapper.insert(gruppe)

    def save_gruppe(self,gruppe):
        """Eine Gruppe speichern"""
        with GruppeMapper() as mapper:
            return mapper.update(gruppe)

    def delete(self,gruppe):
        """Gruppe löschen"""
        with GruppeMapper() as mapper:
            return mapper.delete(gruppe)

    """ 
    Nachricht Methoden
    """

    def create_nachricht(self,id, inhalt):
        """Nachricht erstellen"""
        nachricht = Nachricht()
        nachricht.set_id(id)
        nachricht.set_inhalt(inhalt)

        with NachrichtMapper() as mapper:
            return mapper.insert(nachricht)

    def save_nachricht(self, nachricht):
        """Nachricht speichern"""
        with NachrichtMapper() as mapper:
            return mapper.update(nachricht)

    def delete(self, nachricht):
        """Nachricht löschen"""
        with NachrichtMapper() as mapper:
            return mapper.delete(nachricht)

    def get_nachricht_by_id(self, id):
        """Nachricht nach id auslesen"""
        with NachrichtMapper() as mapper:
            return mapper.find_by_id(id)

    def get_all_nachricht(self):
        """Nachricht nach id auslesen"""
        with NachrichtMapper() as mapper:
            return mapper.find_all()

    def update(self, nachricht):
        """Überschreiben oder Aktualisieren einer Nachricht"""
        with NachrichtMapper() as mapper:
            return mapper.update(nachricht)

    """ 
    Konversation Methoden
    """

    def create_konversation(self, id, nachricht_id, teilnehmer, sender_id, ziel_id, inhalt):
        """ Erstellen einer Konversation"""
        konversation = Konversation()
        konversation.set_id(id)
        konversation.set_nachricht_id(nachricht_id)
        konversation.set_teilnehmer(teilnehmer)
        konversation.set_herkunfts_id(sender_id)
        konversation.set_ziel_id(ziel_id)
        konversation.set_inhalt(inhalt)

        with KonversationMapper() as mapper:
            return mapper.insert(konversation)

    def save_(self, konversation):
        """Konversation speichern"""

        with KonversationMapper() as mapper:
            return mapper.update(konversation)

    def delete(self, konversation):
        """Konversation löschen"""
        with KonversationMapper() as mapper:
            return mapper.delete(konversation)

    def get_konversation_by_id(self, id):
        """Konversation über die Konversations Id auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_by_id(id)

    def get_konversation_by_nachricht_id(self, nachricht_id):
        """Nachricht einer Konversation über die Nachricht Id auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_by_nachricht_id(nachricht_id)

    def get_konversation_by_teilnehmer(self, teilnehmer):
        """Teilnehmer einer Konversation auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_by_teilnehmer(teilnehmer)

    def get_konversation_by_herkunfts_id(self, herkunfts_id):
        """Konversation über herkunfts Id auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_by_herkunfts_id(herkunfts_id)

    def get_konversation_by_ziel_id(self, ziel_id):
        """Konversation über Ziel Id auslesen"""
        with KonversationMapper() as mapper:
            return mapper.find_by_ziel_id(ziel_id)

    """
    Teilnahme Methoden
    """

    def create_teilnahme(self, id, teilnehmer, gruppen_id, konversations_id, nachricht_id):
        """Teilnahme erstellen"""
        teilnahme = Teilnahme()
        teilnahme.set_id(id)
        teilnahme.set_teilnehmer(teilnehmer)
        teilnahme.set_gruppen_id(gruppen_id)
        teilnahme.set_konversations_id(konversations_id)
        teilnahme.set_nachricht_id(nachricht_id)

        with TeilnahmeMapper() as mapper:
            return mapper.insert(teilnahme)

    def save_teilnahme(self, teilnahme):
        """Teilnahme speichern"""
        with TeilnahmeMapper() as mapper:
            return mapper.update(teilnahme)

    def delete(self, teilnahme):
        """Teilnahme löschen"""
        with TeilnahmeMapper () as mapper:
            return mapper.delete(teilnahme)

    def get_teilnahme_id(self, id):
        """Auslesen der Teilnahme Id"""
        with TeilnahmeMapper () as mapper:
            return mapper.find_by_id(id)
    
    def get_gruppen_id(self,gruppen_id):
        """Auslesen der Gruppen Id über die Teilnahme"""
        with TeilnahmeMapper () as mapper:
            return mapper.find_by_gruppen_id(gruppen_id)

    def get_konversation_by_konversations_id(self,konversations_id):
        """Teilnahme an einer Konversation über die konversations_id"""
        with TeilnahmeMapper() as mapper:
            return mapper.find_by_konversation_id(konversations_id)



    """
    Empfehlungs Methoden
    """
    
    def create_empfehlung(self,id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil):
        """ Empfehlungs erstellen"""
        empfehlung = Empfehlung()
        empfehlung.set_id(id)
        empfehlung.set_empfehlung(empfehlung)
        empfehlung.set_empfehlungsListe(empfehlungsListe)
        empfehlung.set_empfehlungGruppe(empfehlungGruppe)
        empfehlung.set_empfehlungProfil(empfehlungProfil)

        with EmpfehlungMapper() as mapper:
            return mapper.insert(empfehlung)

    def save_empfehlung(self, empfehlung):
        """ Save empfehlung"""
        with EmpfehlungMapper() as mapper:
            return mapper.update(empfehlung)

    def delete(self,empfehlung):
        """Empfehlung löschen"""
        with EmpfehlungMapper() as mapper:
            return mapper.delete(empfehlung)
    
    def get_empfehlung_by_id(self, id):
        """Get empfehlung by id"""
        with EmpfehlungMapper() as mapper:
            return mapper.find_by_id(id)

    def get_empfehlung_Liste(self, empfehlungsListe):
        """Auslesen der Empfehlungs Liste"""
        with EmpfehlungMapper() as mapper:
            return mapper.find_by_empfehlungsListe(empfehlungsListe)

    def get_empfehlung_Gruppe(self, empfehlungGruppe):
        """Auslesen derGruppenempfehlung """
        with EmpfehlungMapper() as mapper:
            return mapper.find_by_empfehlungGruppe(empfehlungGruppe)

