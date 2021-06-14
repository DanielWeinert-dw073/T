#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject

class Lernvorlieben(BusinessObject):
    """Realisierung der Lernvorlieben einer Gruppe oder einer Einzelperson im System"""

    def __init__(self): 
        super().__init__()
        self._frequenz = None
        self._internet_verbindung = None
        self._pole_der_persoenlichkeit = None

    def get_frequenz(self):
        """Auslesen der Fequenz"""
        return self._frequenz

    def set_frequenz(self,value):
        """Setzrn der Fequenz"""
        self._frequenz = value

    def get_pole_der_persoenlichkeit(self):
        """Auslesen der PoleDerPersönlichkeit"""
        return self._pole_der_persoenlichkeit

    def set_pole_der_persoenlichkeit(self,value):
        """Setzen der Pole PoleDerPersönlichkeit"""
        self._pole_der_persoenlichkeit = value

    def get_internet_verbindung(self):
        """Auslesen der set_internet_verbindung"""
        return self._internet_verbindung

    def set_internet_verbindung(self,value):
        """Setzen der InternetVerbindung"""
        self._internet_verbindung = value

    def __str__(self):
        """textuelle Replikation des BOs"""
        return "Lernvorliebe: {}, {}, {}, {}, {}".format(self.get_id(),

                                                    self._frequenz,
                                                    self._internet_verbindung,
                                                    self._pole_der_persoenlichkeit)


    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandlung eines Python dict () in ein Python Objekt"""
        obj = Lernvorlieben()
        obj.set_id(dictionary["id"])
        obj.set_frequenz(dictionary["frequenz"])
        obj.set_internet_verbindung(dictionary["InternetVerbindung"])
        obj.set_pole_der_persoenlichkeit(dictionary["PoleDerPersönlichkeit"])

        return obj