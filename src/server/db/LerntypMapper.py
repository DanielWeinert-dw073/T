#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import name
from server.db.Mapper import Mapper
from server.bo.Lerntyp import Lerntyp

class LerntypMapper(Mapper):
    """Mapper-Klasse, die Lerntypen Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Lerntypen aus der Datenbank

        :return Alle Lerntypen Objekte im System
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, lerntyp FROM lerntypen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, lerntyp) in tuples:
            lerntyp = Lerntyp()
            lerntyp.set_id(id)
            lerntyp.set_lerntyp(lerntyp)
            result.append(lerntyp)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_lerntyp(self, lerntyp):
        """Suchen eines Lerntyps aus der Datenbank nach dem angegebenen Lerntyp
            :param lerntyp_name -> lerntyp-Objekt
            return Lerntyp Objekt, welches mit dem Lerntyp übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp FROM lerntypen WHERE lerntyp='{}'".format(lerntyp)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, lerntyp) = tuples[0]
                lerntyp = Lerntyp()
                lerntyp.set_id(id)
                lerntyp.set_lerntyp(lerntyp)
                result = lerntyp

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines Lerntyps nach der übergebenen Id. 

        :param id Primärschlüsselattribut eines Lerntypen aus der Datenbank
        :return Lerntyp Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp FROM lerntypen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id,lerntyp) = tuples[0]
            lerntyp = Lerntyp()
            lerntyp.set_id(id)
            lerntyp.set_lerntyp(lerntyp)
            result = lerntyp

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, lerntyp):
        """Einfügen eines Lerntyp Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft 

        :param Lerntyp des zu speichernde Lerntyp Objekts
        :return das bereits übergebene lerntyp Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM lerntypen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                lerntyp.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                lerntyp.set_id(1)

        command = "INSERT INTO lerntypen (id, lerntyp) VALUES (%s,%s)"
        data = (lerntyp.get_id(), lerntyp.get_lerntyp())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return lerntyp

    def update(self, lerntyp):
        """Überschreiben / Aktualisieren eines lerntyp-Objekts in der DB

        :param lerntyp -> lerntyp-Objekt
        :return aktualisiertes lerntyp-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE lerntypen " + "SET lerntyp=%s,  WHERE lerntyp=%s"
        data = (lerntyp.get_id(),  lerntyp.get_lerntyp())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def update_by_id(self, lerntyp):
        """Überschreiben / Aktualisieren eines lerntyp-Objekts in der DB

        :param lerntyp -> lerntyp-Objekt
        :return aktualisiertes lerntyp-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE lerntypen " + "SET lerntyp=%s, WHERE id=%s"
        data = (lerntyp.get_lerntyp, lerntyp.get_id())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, lerntyp):
        """Löschen der Daten eines Studenten aus der Datenbank

        :param lerntyp -> lerntyp-Objekt
        """
        cursor = self._connection.cursor()

        command = "DELETE FROM lerntypen WHERE id={}".format(lerntyp.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with LerntypMapper() as mapper:
        result = mapper.find_all()
        for lerntyp in result:
            print(lerntyp)