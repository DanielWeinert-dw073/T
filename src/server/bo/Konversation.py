#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject

class Konversation(BusinessObject):
    """Realisierung der Konversations Klasse, die für die Kommunikation innerhalb der 
    Gruppen dient"""

    def __init__(self):
        super().__init__()
        self._nachricht = None
        self._teilnehmer = None

    def get_nachricht(self):
        """Auslesen der Nachricht"""
        return self._nachricht

    def set_nachricht(self, nachricht):
        """ Setzen der Nachricht"""
        self._nachricht = nachricht

    def get_teilnehmer(self):
        """Auslesen der Teilnehmer"""
        return self.get_teilnehmer

    def set_teilnehmer(self,teilnehmer):
        """Setzen der Teilnehmer"""
        self._teilnehmer = teilnehmer


    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Python Objekt Teilnahme()"""
        konversation = Konversation()
        konversation.set_id(dictionary["id"])
        konversation.set_teilnehmer(dictionary["teilnehmer"])
        konversation.set_nachricht (dictionary["nachricht"])
        return konversation
     
