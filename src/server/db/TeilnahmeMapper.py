#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import name
from server.db.Mapper import Mapper
from server.bo.Teilnahme import Teilnahme

class TeilnahmeMapper(Mapper):
    """Mapper-Klasse, die Teilnahme Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Teilnahmen aus der Datenbank

        :return Alle Teilnahme Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, teilnehmer, gruppen_id, konversations_id, nachricht_id FROM teilnahmen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, teilnehmer, gruppen_id, konversations_id, nachricht_id) in tuples:
            teilnahme = Teilnahme()
            teilnahme.set_id(id)
            teilnahme.set_teilnehmer(teilnehmer)
            teilnahme.set_gruppen_id(gruppen_id)
            teilnahme.set_konversations_id(konversations_id)
            teilnahme.set_nachricht_id(nachricht_id)
            result.append(teilnahme)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_teilnehmer(self, teilnahme):
        """Suchen einer Teilnahme aus der Datenbank nach dem angegebenem Teilnehmer
            :param teilnahme_teilnehmer -> teilnahme-Objekt
            return Teilnahme Objekt, welches mit der Teilnahme übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, teilnahme FROM teilnahmen WHERE Teilnahme='{}'".format(teilnahme)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, gruppen_id, konversations_id, nachricht_id, teilnehmer_id) = tuples[0]
                teilnahme = Teilnahme()
                Teilnahme.set_id(id)
                teilnahme.set_gruppen_id(gruppen_id)
                teilnahme.set_konversations_id(konversations_id)
                teilnahme.set_nachricht_id(nachricht_id)
                teilnahme.set_teilnehmer_id(teilnehmer_id)
                result = teilnahme

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen einer Teilnahme nach der übergebenen Id.

        :param id Primärschlüsselattribut einer Teilnahme aus der Datenbank
        :return Teilnahme Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, gruppen_id, konversations_id, nachricht_id, teilnehmer_id FROM teilnahmen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, gruppen_id, konversations_id, nachricht_id, teilnehmer_id) = tuples[0]
            teilnahme = Teilnahme()
            teilnahme.set_id(id)
            teilnahme.set_teilnehmer_id(teilnehmer_id)
            teilnahme.set_gruppen_id(gruppen_id)
            teilnahme.set_konversations_id(konversations_id)
            teilnahme.set_nachricht_id(nachricht_id)
            result = teilnahme

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result
    
    def find_group(self,id): 
        """ Finde alle Teilnahmen von einer Gruppen ID"""
        result = []
        cursor = self._cnx.cursor()
        command = "SELECT group_id FROM teilnahmen WHERE id={}".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        for (group) in tuples:
            teilnahme = Teilnahme()
            teilnahme.set_le()
            result.append(teilnahme)

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, teilnahme):
        """Einfügen einer Teilnahme Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param Teilnahme des zu speichernden Teilnahme Objekts
        :return das bereits übergebene Teilnahme Objekt mit aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM teilnahmen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                teilnahme.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                teilnahme.set_id(1)

        command = "INSERT INTO teilnahmen (id, gruppen_id, konversations_id, nachricht_id, teilnehmer_id) VALUES (%s,%s,%s,%s,%s)"
        data = (teilnahme.get_id(),teilnahme.get_gruppen_id(), teilnahme.get_konversations_id(),teilnahme.get_nachricht_id(), teilnahme.get_teilnehmer_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return teilnahme

    def update(self, teilnahme):
        """Überschreiben / Aktualisieren eines teilnahme-Objekts in der DB

        :param teilnahme -> teilnahme-Objekt
        :return aktualisiertes teilnahme-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE teilnahmen " + "SET teilnahme=%s,  WHERE teilnahme=%s"
        data = (teilnahme.get_id(),teilnahme.get_gruppen_id(), teilnahme.get_konversations_id(),teilnahme.get_nachricht_id(), teilnahme.get_teilnehmer_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_id(self, teilnahme):
        """Überschreiben / Aktualisieren eines teilnahme-Objekts in der DB

        :param teilnahme -> teilnahme-Objekt
        :return aktualisiertes teilnahme-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE teilnahmen " + "SET teilnahme=%s, WHERE id=%s"
        data = (teilnahme.get_id(),teilnahme.get_gruppen_id(), teilnahme.get_konversations_id(),teilnahme.get_nachricht_id(), teilnahme.get_teilnehmer_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, teilnahme):
        """Löschen der Daten einer Teilnahme aus der Datenbank

        :param teilnahme -> teilnahme-Objekt
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM teilnahmen WHERE id={}".format(teilnahme.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with TeilnahmeMapper() as mapper:
        result = mapper.find_all()
        for teilnahme in result:
            print(teilnahme)