#!/usr/bin/python
# -*- coding: utf-8 -*-
import mysql.connector as connector
import os
from contextlib import AbstractContextManager
from abc import ABC, abstractmethod


class Mapper(AbstractContextManager, ABC):
    """Abstrakte Basisklasse für alle Mapper Klassen"""

    def __init__(self):
        self._connection = None

    def __enter__(self):

        if os.getenv('GAE_ENV', '').startswith('standard'):
            """Hier wird versucht ob der Code in der Cloud im sogennatem Production Mode läuft. Verbindungsaufbau zwischen Cloud SQL und Google
            App Engone hat hier stattgefunden"""

            self._connection = connector.connect(user='root', password='root',
                                                 unix_socket='/cloudsql/schlüssel_adresse_hier_einfügen',
                                                 database='Datenbankname')
        else:
            """Hier läuft der Code Lokal ab, im Development Mode.Dabei wird eine Verbindung zur lokalen SQL-DB erzeugt."""

            self._connection = connector.connect(user='root', password='',
                                                 host='127.0.0.1',
                                                 database='sw-project')

        return self


    def __exit__(self, exc_type, exc_val, exc_tb):

        """In order to close the connection we use the following statement. For example we quit working with the mapper class for now"""
        self._connection.close()

    """The following functions should be inherited by all Mapper-Subclasses"""

    @abstractmethod
    def find_all(self):
        """Reads all tuple and returns them as an object"""
        pass

    @abstractmethod
    def find_by_id(self):
        """Reads a tuple with a given ID"""
        pass

    @abstractmethod
    def insert(self):
        """Add the given object to the database"""
        pass

    @abstractmethod
    def update(self):
        """Update an already given object in the DB"""
        pass

    @abstractmethod
    def delete(self):
        """Delete an object from the DB"""
        pass
