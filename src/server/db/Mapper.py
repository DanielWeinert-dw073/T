#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper(AbstractContextManager, ABC):
    """Abstrakte Basisklasse für alle Mapper Klassen"""

    def __init__(self):
        self._cnx = None

    def __enter__(self):

        if os.getenv('GAE_ENV', '').startswith('standard'):
            """Hier wird versucht ob der Code in der Cloud im sogennatem Production Mode läuft. Verbindungsaufbau zwischen Cloud SQL und Google
            App Engone hat hier stattgefunden"""

            self._cnx = connector.connect(user='root', password='root',
                                                 unix_socket='/cloudsql/schlüssel_adresse_hier_einfügen',
                                                 database='Datenbankname')
        else:
            """Hier läuft der Code Lokal ab, im Development Mode.Dabei wird eine Verbindung zur lokalen SQL-DB erzeugt."""

            self._cnx = connector.connect(user='web173_2', password='by4pr6IhE5VuJRkF!',
                                                 host='s293.goserver.host',
                                                 database='web173_db2')


        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        """In order to close the connection we use the following statement. For example we quit working with the mapper class for now"""
        self._cnx.close()

    """The following functions should be inherited by all Mapper-Subclasses"""

    @abstractmethod
    def find_all(self):
        """Reads all tuple and returns them as an object"""
        pass

    @abstractmethod
    def find_by_id(self, key):
        """Reads a tuple with a given ID"""
        pass

    @abstractmethod
    def insert(self, object):
        """Add the given object to the database"""
        pass

    @abstractmethod
    def update(self, object):
        """Update an already given object in the DB"""
        pass

    @abstractmethod
    def delete(self, object):
        """Delete an object from the DB"""
        pass
