#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Nachricht import Nachricht

class NachrichtMapper(Mapper):
    """Mapper-Klasse, die Nachricht Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Nachrichten aus der Datenbank

        :return Alle Nachrichten Objekte im System
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, nachricht FROM nachrichten"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, nachricht) in tuples:
            nachricht = nachricht()
            nachricht.set_id(id)
            nachricht.set_nachricht(nachricht)
            result.append(nachricht)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_nachricht(self, nachricht):
        """Suchen einer Nachricht aus der Datenbank nach dem angegebenen Nachricht
            :param nachricht_name -> nachricht-Objekt
            return nachricht Objekt, welches mit dem nachricht übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, nachricht FROM nachrichten WHERE nachricht='{}'".format(nachricht)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, nachricht) = tuples[0]
                nachricht = Nachricht()
                nachricht.set_id(id)
                nachricht.set_nachricht(nachricht)
                result = nachricht

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen einer Nachricht nach der übergebenen Id.

        :param id Primärschlüsselattribut einer Nachricht aus der Datenbank
        :return Nachricht Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, nachricht FROM nachrichten WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id,nachricht) = tuples[0]
            nachricht = nachricht()
            nachricht.set_id(id)
            nachricht.set_nachricht(nachricht)
            result = nachricht

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, nachricht):
        """Einfügen einer Nachricht Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param Nachricht des zu speichernde Nachricht Objekts
        :return das bereits übergebene Nachricht Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM nachrichten ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                nachricht.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                nachricht.set_id(1)

        command = "INSERT INTO nachrichten (id, nachricht) VALUES (%s,%s)"
        data = (nachricht.get_id(), nachricht.get_nachricht())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return nachricht

    def update(self, nachricht):
        """Überschreiben / Aktualisieren eines nachricht-Objekts in der DB

        :param nachricht -> nachricht-Objekt
        :return aktualisiertes nachricht-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE nachrichten " + "SET nachricht=%s,  WHERE nachricht=%s"
        data = (nachricht.get_id(),  nachricht.get_nachricht())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def update_by_id(self, nachricht):
        """Überschreiben / Aktualisieren eines nachricht-Objekts in der DB

        :param nachricht -> nachricht-Objekt
        :return aktualisiertes nachricht-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE nachrichten " + "SET nachricht=%s, WHERE id=%s"
        data = (nachricht.get_id, nachricht.get_nachricht())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, nachricht):
        """Löschen der Daten einer Nachricht aus der Datenbank

        :param nachricht -> nachricht-Objekt
        """
        cursor = self._connection.cursor()

        command = "DELETE FROM nachrichten WHERE id={}".format(nachricht.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with NachrichtMapper() as mapper:
        result = mapper.find_all()
        for nachricht in result:
            print(nachricht)