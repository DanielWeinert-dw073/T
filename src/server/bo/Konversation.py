#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject

class Konversation(BusinessObject):
    """Realisierung der Konversations Klasse, die für die Kommunikation innerhalb der 
    Gruppen dient"""

    def __init__(self):
        super().__init__()
        self._nachricht_id = None
        self._teilnehmer = None
        self._herkunfts_id = None
        self._ziel_id = None
        self._inhalt = None


    def get_nachricht_id(self):
        """Auslesen der Nachricht"""
        return self._nachricht

    def set_nachricht_id(self, nachricht):
        """ Setzen der Nachricht"""
        self._nachricht = nachricht

    def get_teilnehmer(self):
        """Auslesen der Teilnehmer"""
        return self.get_teilnehmer

    def set_teilnehmer(self,teilnehmer):
        """Setzen der Teilnehmer"""
        self._teilnehmer = teilnehmer

    def get_herkunfts_id(self):
        """Auslesen der Teilnehmer"""
        return self.get_teilnehmer

    def set_herkunfts_id(self,teilnehmer):
        """Setzen der Teilnehmer"""
        self._teilnehmer = teilnehmer

    def get_ziel_id(self):
        """Auslesen der Ziel Id """
        return self._ziel_id

    def set_ziel_id(self,value):
        """Setzen der Ziel Id"""
        self._ziel_id = value

    def get_inhalt(self):
        """Auslesen des Inhaltes der Nachricht"""
        return self._inhalt

    def set_inhalt(self,value):
        """Setzen des Inhaltes der Nachrichten einer Konversation """
        self._inhalt = value

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Python Objekt Konversation()"""
        konversation = Konversation()
        konversation.set_id(dictionary["id"])
        konversation.set_teilnehmer(dictionary["teilnehmer"])
        konversation.set_nachricht_id(dictionary["nachricht_id"])
        konversation.set_herkunfts_id(dictionary["herkunfts_id"])
        konversation.set_ziel_id(dictionary["Ziel Id"])
        konversation.set_inhalt(dictionary["Inhalt der Nachricht"])
        return konversation
     
