#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject
from server.bo.Suggestion_Algorithmus import Suggestion_Algorithmus

class Empfehlung(BusinessObject): 
    """ Realisierung der Empfehlungklasse die Profile und/oder Gruppen entsprechend der Lernvorlieben
    und des Lerntypens auflistet."""



    def __init__(self):
        super().__init__()
        self._empfehlung = None
        self._empfehlungsListe = None
        self._empfehlungGruppe = None
        self._empfehlungProfil = None

    
    def get_empfehlung(self):
        """Auslesen der Empfehlung"""
        return self._empfehlung

    def set_empfehlung(self,value):
        """setzen der Empfehlung"""
        self._empfehlung= value

    def get_empfehlungsListe(self):
        """Auslesen der EmpfehlungsListe"""
        return self._empfehlungsListe

    def set_empfehlungsListe(self,value):
        """setzen der EmpfehlungsListe"""
        self._empfehlungsListe = value

    def get_empfehlungGruppe(self):
        """Auslesen der empfehlungGruppe"""
        return self._empfehlungGruppe

    def set_empfehlungGruppe(self,value):
        """setzen der empfehlungGruppe"""
        self._empfehlungGruppe = value

    def get_empfehlungProfil(self):
        """Auslesen der empfohlenen Profile """
        return self._empfehlungProfil

    def set_empfehlungProfil(self,value):
        """Setzen der Profilempfehlung"""
        self._empfehlungProfil = value

    @staticmethod
    def from_dict(dictionary=dict()):
        empfehlung = Empfehlung ()
        empfehlung.set_id(dictionary["id"])
        empfehlung.set_empfehlung(dictionary["Empfehlung"])
        empfehlung.set_empfehlungsListe(dictionary["EmpfehlungsListe"])
        empfehlung.set_empfehlungGruppe(dictionary["EmpfehlungGruppe"])
        empfehlung.set_empfehlungProfil(dictionary["EmpfehlungProfil"])
        return empfehlung
        
