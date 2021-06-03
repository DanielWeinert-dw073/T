#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.BusinessObject import BusinessObject

class Teilnahme(BusinessObject):
    """Realisierung der Teilnahme bei einer Gruppe.
    Eine Teilnahme besitzt Teilnehmer, eine Gruppe, eine Konversation, die 
    ausgelesen und neu gesetzt werden können."""

    def __init__(self):
        super().__init__()
        self._teilnehmer = None
        self._gruppen_id = None
        self._konversations_id = None
        self._nachricht_id = None

    def get_teilnehmer(self):
        """Auslesen der Teilnehmer"""
        return self._teilnehmer

    def set_teilnehmer(self,value):
        """Setzen der Teilnehmer"""
        self._teilnehmer = value

    def get_gruppen_id (self):
        """Auslesen der Gruppen Id"""
        return self._gruppen_id

    def set_gruppen_id(self,value):
        """Setzen der Gruppen Id"""
        self._gruppen_id = value

    def get_konversations_id(self):
        """Auslesen der Konversations Id """
        return self._konversations_id

    def set_konversations_id(self,value):
        """Setzen der Konversations Id"""
        self._konversations_id = value

    def get_nachricht_id(self):
        """Auslesen der Nachrichten Id """
        return self._nachricht_id

    def set_nachricht_id(self,value):
        """Setzen der Nachricht Id """
        self._nachricht_id = value

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandlung eines Python dict () in ein Python Objekt"""
        teilnahme = Teilnahme()
        teilnahme.set_id(dictionary["id"])
        teilnahme.set_gruppen_id(dictionary["Gruppen Id"])
        teilnahme.set_konversations_id(dictionary["KonversationsId"])
        teilnahme.set_nachricht_id(dictionary["Nachricht_Id"])
        teilnahme.set_teilnehmer(dictionary["Teilnehmer"])
        return teilnahme
