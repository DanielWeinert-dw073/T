#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.NamedBusinessObject import NamedBusinessObject

class Gruppe(NamedBusinessObject):

    def __init__(self):
        super().__init__()
        self._anzahlTeilnehmer = None 
        self._teilnehmerListe = None
        self._max_teilnehmer = None

    def get_max_teilnehmer(self):
        """Auslesen der maximalen Teilnehmeranzahl"""
        return self._max_teilnehmer

    def set_max_teilnehmer(self,value):
        """setzen der maximalen Teilnehmeranzahl"""
        self._max_teilnehmer = value

    def get_anzahlTeilnehmer(self):
        """Auslesen der gesamten Teilnehmer"""
        return self._anzahlTeilnehmer

    def set_anzahlTeilnehmer(self,value):
        """Setzen der Teilnehmer"""
        self._anzahlTeilnehmer = value

    def get_teilnehmerListe(self):
        """Auslesen der Teilnehmer"""
        return self._teilnehmerListe

    def set_teilnehmerListe(self,value):
        """Setzen der Teilnehmer"""
        self._teilnehmerListe = value

    def __str__(self):

        return "Gruppe: {}, {}, {}, {}, {}, {}".format (self.get_id(),
                                                        self.get_name(),
                                                        self._anzahlTeilnehmer,
                                                        self.get_erstellungszeitpunkt(),
                                                        self._max_teilnehmer,
                                                        self._teilnehmerListe)

    @staticmethod
    def from_dict(dictionary=dict()):
        """dict() -> gruppe"""
        obj = Gruppe()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["name"])
        obj.set_max_teilnehmer(dictionary["_max_teilnehmer"])
        obj.set_anzahlTeilnehmer(dictionary["_anzahlTeilnehmer"])
        obj.set_teilnehmerListe(dictionary["teilnehmerListe"])
        return obj