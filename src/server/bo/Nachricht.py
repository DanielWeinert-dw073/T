#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject

class Nachricht(BusinessObject):
    """Realisierung der Nachrichtenklasse des Systems. Nachrichten
    kommen in Konversationen vor und besitzen einen Inhalt und eine Id somit sie
    jederzeit einem Profil und einer Konversation zuordbar sind."""

    def __init__(self):
        super().__init__()
        self._inhalt = None


    def get_inhalt(self):
        """Auslesen des Inhaltes der Nachricht"""
        return self._inhalt

    def set_inhalt(self,value):
        """Setzen des Inhaltes der Nachrichten einer Konversation """
        self._inhalt = value

    def __str__(self):
        """textuelle Darstellung einer Nachricht"""

    @staticmethod
    def from_dict(dictionary=dict()):
        """Convert eines Python dict () in ein Python Objekt"""
        nachricht = Nachricht()
        nachricht.set_id(dictionary["id"])
        nachricht.set_inhalt(dictionary["Inhalt"])
        nachricht.set_erstellungszeitpunkt(dictionary["Erstellungszeitpunkt"])
        return nachricht
