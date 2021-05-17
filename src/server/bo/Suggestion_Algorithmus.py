#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject
from server.bo.Profil import Profil
from server.bo.Lerntyp import Lerntyp
from server.bo.Lernvorlieben import Lernvorlieben


class Suggestion_Algorithmus(BusinessObject):
    """Realisierung des Suggestions_Algorithmus, der für die Findung von 
    ähnlichen Profilen und lerngruppen im system ist. Die Suche befasst sich mit 
    den lerntypen und den lernverhalten von Gruppen und Individuen."""

    
    def __init__(self,lerntyp,lernvorlieben,profil,gruppen):
        self.lerntyp_Id = lerntyp
        self.lernvorlieben_Id = lernvorlieben
        self.profil_Id = profil
        self.gruppen_Id = gruppen

    def get_lerntyp_Id(self):
        """Auslesen der lerntyp_Id"""
        return self.lerntyp_Id

    def set_lerntyp_Id(self,lerntyp):
        """Setzen der Lerntyp id"""
        self.lerntyp_Id = lerntyp

    def get_lernvorlieben_Id(self):
        """Auslesen der Lernvorlieben Id"""
        return self.lernvorlieben_Id

    def set_lernvorlieben_Id(self,lernvorlieben):
        """Setzen der Lernvorlieben Id"""
        self.lernvorlieben_Id = lernvorlieben

    def get_profil_id(self):
        """Auslesen der Profil Id """
        return self.profil_Id

    def set_profil_Id(self,profil):
        """ Setzen der Profil_id"""
        self.profil_Id = profil

    def get_gruppen_Id(self): 
        """ Auslesen der der Gruppen Id"""
        return self.gruppen_Id

    def set_gruppen_Id(self,gruppe):
        """Setzen der Gruppen Id"""
        self.gruppen_Id = gruppe

    @staticmethod
    def from_dict(dictionary=dict()):
        obj =Suggestion_Algorithmus ()
        obj.set_lerntyp_Id(dictionary["Lerntyp Id"])
        obj.set_gruppen_Id(dictionary["Gruppen Id"])
        obj.set_id(dictionary["id"])
        obj.set_lernvorlieben_Id(dictionary["Lernvorlieben Id"])
        obj.setprofil_Id(dictionary["Profil Id"])
        return obj




    


