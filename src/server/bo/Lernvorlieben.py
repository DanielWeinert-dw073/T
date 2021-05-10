#!/usr/bin/python
# -*- coding: utf-8 -*-


class Lernvorlieben: 
    """ Realisierung der möglichen Lernvorlieben der Studenten, 
    welche genutzt werden um passende Gruppen zu bilden. Eine Lernvorliebe
    besitzt einen Namen der auslesbar sein soll und neu gesetzt werden kann."""

    def __init__(self,name):
        self.name = name

    def get_name(self):
        """ Auslesen des Namens der Lernvorliebe"""
        return self.name

    def set_name(self,name):
        """ Setzen des Namens der Lernvorliebe """
        self.name = name

    def __str__(self):
        """ Erzeugen einer textuellen Darstellung der 
        jeweiligen Rolle"""
        return self.name

