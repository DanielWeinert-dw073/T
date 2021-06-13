#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.NamedBusinessObject import NamedBusinessObject
from server.bo.Lerntyp import Lerntyp

class Student(NamedBusinessObject):
    """Realisierung der Studenten Klasse des Systems ein Student besitzt ein oder mehrere Profile 
    und hat bestimmte Lernvorlieben, welche in der Klasse seines Profils festgehalten werden"""

    """ Ein Student besitzt eine Email, mit der er sich einloggt, eine eindeutige Google User Id sowie einen
    Lerntyp, welche einem Student zugewiesen wird. Diese Lerntypen werden an das Profil weitergegeben um dort für die Gruppenzuordnung 
    genutzt wird."""

    def __init__(self):
        super().__init__()
        self._email = None #Die Email-Adresse des Studenten
        self._google_user_id = None #Die eindeutige Google User Id des Studenten
     

    def get_email(self):
        """ Auslesen der Email-Adresse"""
        return self._email

    def set_email(self, value):
        """ Setzen der Email """
        self._email = value

    def get_google_user_id(self):
        """ Auslesen der Google User Id"""
        return self._google_user_id

    def set_google_user_id(self, value):
        """ Setzen der Google User Id"""
        self._google_user_id = value

    def __str__(self):
        """ Umwandlung der Attributwerte eines Objekts in einen String"""
        return "Student: {}, {}, {}, {}".format(self.get_id(),self._name,self._email,self._google_user_id)

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandlung eines Python dict () in ein Python Objekt Student() """
        obj = Student ()
        obj.set_id(dictionary["id"]) # Teil der Business object Mutterklasse
        obj.set_name(dictionary["name"])
        obj.set_email(dictionary["email"])
        obj.set_google_user_id(dictionary["_google_user_id"])
        return obj
