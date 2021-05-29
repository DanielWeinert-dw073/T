#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.NamedBusinessObject import NamedBusinessObject
from server.bo.Student import Student
from server.bo.Lerntyp import Lerntyp
from server.bo.Lernvorlieben import Lernvorlieben

class Profil(NamedBusinessObject):
    """Realisierung der Profil Klasse, welche einen Studenten und seine Lernvorlieben/Lerntyp
    im System repräsentiert und zur Bestimmung von Gruppen genutzt wird. Desweiteren dient das Profil zum
    Kommunikativen Austausch innerhalb des Systems."""

    LERNTYP_AUDITIV = Lerntyp ("Auditiv") # Klassenvariable für den Lerntyp Auditiv, instanziiert das Python Objekt Lerntyp
    LERNTYP_VISUELL = Lerntyp ("Visuell") # Klassenvariable für den Lerntyp Visuell, instanziiert das Python Objekt Lerntyp
    LERNTYP_KOMMUNIKATIV = Lerntyp ("Kommunikativ") # Klassenvariable für den Lerntyp Kommunikativ, instanziiert das Python Objekt Lerntyp
    LERNTYP_MOTORISCH = Lerntyp ("Motorisch") # Klassenvariable für den Lerntyp Motorisch, instanziiert das Python Objekt Lerntyp

    def __init__(self):
        super().__init__()
        self._faecher = None
        self._alter = None
        self._studiengang = None
        self._wohnort = None
        self._semester = None
        self._vorwissen = None
        self._lernvorlieben = None
        self._about_me = None
        self._sprachen = None

    def get_faecher(self):
        """Auslesen der Fächer"""
        return self._faecher

    def set_faecher(self,value):
        """Setzen der Fächer"""
        self._faecher = value

    def get_alter(self):
        """Auslesen des Alters """
        return self._alter

    def set_alter(self,value):
        """Setzen des Alters"""
        self._alter = value

    def get_studiengang(self):
        """Auslesen des Studiengangs"""
        return self._studiengang

    def set_studiengang(self,value):
        """Setzen des Studiengangs"""
        self._studiengang = value

    def get_wohnort(self):
        """Auslesen des Wohnortes"""
        return self._wohnort

    def set_wohnort(self,value):
        """Setzen des Wohnortes"""
        self._wohnort = value 

    def get_semester(self):
        """Auslesen des Semesters"""
        return self._semester

    def set_semester(self,value):
        """Setzen des Semesters"""
        self._semester = value

    def get_vorwissen(self):
        """Auslesen des Vorwissen"""
        return self._vorwissen

    def set_vorwissen(self,value):
        """Setzen des Vorwissen"""
        self._vorwissen = value

    def get_lernvorlieben(self):
        """Setzen der Lernvorlieben"""
        return self._lernvorlieben

    def set_lernvorlieben(self,value):
        """Setzen der Lernvorlieben"""
        self._lernvorlieben = value

    def get_about_me(self):
        """Auslesen des AboutMe"""
        return self._about_me

    def set_about_me(self,value):
        """Setzen des AboutMe"""
        self._about_me = value
    
    def get_sprachen(self):
        """Auslesen der Sprachen"""
        return self._sprachen

    def set_sprachen(self,value):
        """Setzen der Sprachen"""
        self._sprachen = value

    def get_lerntyp(self):
        """Auslesen des Lerntypes"""
        return self.get_lerntyp

    def set_lerntyp(self,value):
        """Setzen des Lerntypes"""
        self._lerntyp = value

    def __str__(self):
        """ Erzeugen und Ausgabe einer textuellen Replikation des BOs"""
        return "Profil: {}, {}, {}, {}".format(
                                                            self.get_id(),
                                                            self.get_name(),
                                                            self.get_erstellungszeitpunkt(),
                                                            self.get_lernvorlieben())

    @staticmethod
    def from_dict(dictionary=dict()):
        """Umwandlung eines Python dict () in ein Python Objekt"""
        profil = Profil()
        profil.set_id(dictionary["id"])
        profil.set_name(dictionary["Name"])
        profil.set_alter(dictionary["Alter"])
        profil.set_lernvorlieben(dictionary["Lernvorlieben"])
        profil.set_faecher(dictionary["Faecher"])
        profil.set_semester(dictionary["Semester"])
        profil.set_about_me(dictionary["About_Me"])
        profil.set_sprachen(dictionary["Sprachen"])
        profil.set_studiengang(dictionary["Studiengang"])
        profil.set_lerntyp(dictionary["Lerntyp"])
        profil.set_vorwissen(dictionary["Vorwissen"])
        profil.set_wohnort(dictionary["Wohnort"])
        return profil

 
        


