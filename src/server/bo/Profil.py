#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.bo.NamedBusinessObject import NamedBusinessObject
from server.bo.Student import Student

class Profil(NamedBusinessObject,Student):
    """Realisierung der Profil Klasse, welche einen Studenten und seine Lernvorlieben/Lerntyp
    im System repräsentiert und zur Bestimmung von Gruppen genutzt wird. Desweiteren dient das Profil zum
    Kommunikativen Austausch innerhalb des Systems."""

    def __init__(self):
        super().__init__()
        self._faecher = None
