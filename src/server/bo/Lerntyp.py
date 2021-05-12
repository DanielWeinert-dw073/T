#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.BusinessObject import BusinessObject

class Lerntyp(BusinessObject): 
    """ Realisierung der mögliche Lerntypen der Studenten, 
    welche genutzt werden um passende Gruppen zu bilden. Ein Lerntyp
    besitzt einen Namen der auslesbar sein soll und neu gesetzt werden kann."""

    def __init__(self):
        super().__init__()
        self.lerntyp = None

    def get_lerntyp(self):
        """ Auslesen des Namens der Lerntypen"""
        return self.lerntyp

    def set_lerntyp(self,lerntyp):
        """ Setzen des Namens der Lerntypen """
        self.lerntyp = lerntyp

    def __str__(self):
        """ Erzeugen einer textuellen Darstellung des 
        jeweiligen Lerntyps"""
        return self.lerntyp

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandlung eines Python dict () in ein Python Objekt"""
        obj = Lerntyp ()
        obj.set_id(dictionary["id"])
        obj.set_lerntyp(dictionary["Lerntyp"])
        return obj


