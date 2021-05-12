#!/usr/bin/python
# -*- coding: utf-8 -*-
from server.bo.BusinessObject import BusinessObject

class Gruppenempfehlung(BusinessObject): 
    """ Realisierung der Gruppenempfehlungklasse die Profile und/oder Gruppen entsprechend der Lernvorlieben
    und des Lerntypens auflistet."""

    def __init__(self):
        super().__init__()
        
