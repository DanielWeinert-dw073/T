#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.BusinessObject import BusinessObject

class Teilnahme(BusinessObject):
    """Realisierung der Teilnahme bei einer Gruppe.
    Eine Teilnahme besitzt Teilnehmer, eine Gruppe, eine Konversation, die 
    ausgelesen und neu gesetzt werden können."""

    def __init__(self):
        super().__init__()
        self._teilnehmer = None
        self._gruppe = None
        self._konversation = None

        