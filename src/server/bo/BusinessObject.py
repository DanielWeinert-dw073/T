#!/usr/bin/python
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
import datetime 

class BusinessObject(ABC):

    """Basisklasse für alle BusinessObjekte der Anwendung
    alle BOs enthalten eine Id und ein Erstellungszeitpunkt"""

    def __init__(self):
        self._id = 0 # Die eindeutige Id für die Instanzen dieser Klasse 
        self._erstellungszeitpunkt = datetime.datetime.now() 
        # das Datum zu der das BO erstellt wurde 

    def get_id(self):
        """Auslesen der Id"""
        return self._id 

    def set_id(self,value):
        """Setzen der Id"""
        self._id = value

    def get_erstellungszeitpunkt(self):
        """Auslesen der Erstellungszeitpunkt"""
        return self._erstellungszeitpunkt