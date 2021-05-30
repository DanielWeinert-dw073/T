#!/usr/bin/python
# -*- coding: utf-8 -*-

from server.db.Mapper import Mapper
from server.bo.Lernvorlieben import Lernvorlieben

class LernvorliebenMapper(Mapper):
    """Mapper-Klasse, die lernvorlieben Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller lernvorlieben aus der Datenbank

        :return Alle Studneten Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, frequenz, internet_verbindung, pole_der_persönlichkeit FROM lernvorlieben"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, frequenz, internet_verbindung, pole_der_persönlichkeit) in tuples:
            lernvorlieben = Lernvorlieben()
            lernvorlieben.set_id(id)
            lernvorlieben.set_frequenz(frequenz)
            lernvorlieben.set_internet_verbindung(internet_verbindung)
            lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)
            result.append(lernvorlieben)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_frequenz(self,frequenz):
        """Suchen eines lernvorlieben aus der Datenbank nach dem angegebenen Namen
            :param lernvorlieben_frequenz -> lernvorlieben-Objekt
            return lernvorlieben Objekt, welcher mit dem Namen übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, frequenz, internet_verbindung, pole_der_persönlichkeit FROM lernvorlieben WHERE frequenz='{}'".format(frequenz)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, frequenz, internet_verbindung, pole_der_persönlichkeit) = tuples[0]
                lernvorlieben = Lernvorlieben()
                lernvorlieben.set_id(id)
                lernvorlieben.set_frequenz(frequenz)
                lernvorlieben.set_internet_verbindung(internet_verbindung)
                lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)
                result = lernvorlieben

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines lernvorlieben nach der übergebenen Id. 

        :param id Primärschlüsselattribut eines lernvorlieben aus der Datenbank
        :return lernvorlieben Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, frequenz, internet_verbindung, pole_der_persönlichkeit FROM lernvorlieben WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, frequenz, internet_verbindung, pole_der_persönlichkeit) = tuples[0]
            lernvorlieben = Lernvorlieben()
            lernvorlieben.set_id(id)
            lernvorlieben.set_frequenz(frequenz)
            lernvorlieben.set_internet_verbindung(internet_verbindung)
            lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)
            result = lernvorlieben

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_pole_der_persönlichkeit(self, pole_der_persönlichkeit):
        """Suchen einer lernvorlieben nach der übergebener pole_der_persönlichkeit . 

        :param pole_der_persönlichkeit  einer lernvorlieben aus der Datenbank
        :return lernvorlieben-Objekt, welche mit der pole_der_persönlichkeit übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, frequenz, internet_verbindung, pole_der_persönlichkeit FROM lernvorlieben WHERE pole_der_persönlichkeit='{}'".format(
                pole_der_persönlichkeit)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, frequenz, internet_verbindung, pole_der_persönlichkeit) = tuples[0]
            lernvorlieben = Lernvorlieben()
            lernvorlieben.set_id(id)
            lernvorlieben.set_frequenz(frequenz)
            lernvorlieben.set_internet_verbindung(internet_verbindung)
            lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)
            result = lernvorlieben
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def find_by_internet_verbindung(self, internet_verbindung):
        """Suchen einer lernvorlieben nach der übergebenen internet_verbindungsinfos. 

        :param internet_verbindung einer lernvorlieben aus der Datenbank
        :return lernvorlieben-Objekt, welche mit der internet_verbindung übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, frequenz, internet_verbindung, pole_der_persönlichkeit FROM lernvorlieben WHERE internet_verbindung='{}'".format(
                internet_verbindung)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, frequenz, internet_verbindung, pole_der_persönlichkeit) = tuples[0]
            lernvorlieben = Lernvorlieben()
            lernvorlieben.set_id(id)
            lernvorlieben.set_frequenz(frequenz)
            lernvorlieben.set_internet_verbindung(internet_verbindung)
            lernvorlieben.set_pole_der_persönlichkeit(pole_der_persönlichkeit)
            result = lernvorlieben
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def insert(self, lernvorlieben):
        """Einfügen eines lernvorlieben Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft 

        :param lernvorlieben das zu speichernde lernvorlieben Objekt
        :return das bereits übergebene lernvorlieben Objekt mit aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM lernvorlieben ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                lernvorlieben.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                lernvorlieben.set_id(1)

        command = "INSERT INTO lernvorlieben (id, frequenz, internet_verbindung, pole_der_persönlichkeit) VALUES (%s,%s,%s,%s)"
        data = (lernvorlieben.get_id(), lernvorlieben.get_frequenz(), lernvorlieben.get_internet_verbindung(), lernvorlieben.get_pole_der_persönlichkeit())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return lernvorlieben

    def update(self, lernvorlieben):
        """Überschreiben / Aktualisieren eines lernvorlieben-Objekts in der DB

        :param lernvorlieben -> lernvorlieben-Objekt
        :return aktualisiertes lernvorlieben-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE lernvorlieben " + "SET frequenz=%s, internet_verbindung=%s WHERE pole_der_persönlichkeit=%s"
        data = (lernvorlieben.get_frequenz(), lernvorlieben.get_internet_verbindung(), lernvorlieben.get_pole_der_persönlichkeit())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_id(self, lernvorlieben):
        """Überschreiben / Aktualisieren eines lernvorlieben-Objekts in der DB

        :param lernvorlieben -> lernvorlieben-Objekt
        :return aktualisiertes lernvorlieben-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE lernvorlieben " + "SET frequenz=%s, internet_verbindung=%s,  WHERE id=%s"
        data = (lernvorlieben.get_frequenz(), lernvorlieben.get_internet_verbindung(), lernvorlieben.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, lernvorlieben):
        """Löschen der Daten eines lernvorlieben aus der Datenbank

        :param lernvorlieben -> lernvorlieben-Objekt
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM lernvorlieben WHERE id={}".format(lernvorlieben.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with LernvorliebenMapper() as mapper:
        result = mapper.find_all()
        for lernvorlieben in result:
            print(lernvorlieben)