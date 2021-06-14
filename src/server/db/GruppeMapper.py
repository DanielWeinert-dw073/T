#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Gruppe import Gruppe

class GruppeMapper(Mapper):
    """Mapper-Klasse, die Gruppen Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Gruppen aus der Datenbank

        :return Alle Gruppen Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, name FROM gruppen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, teilnehmerzahl, teilnehmerListe, max_teilnehmer) in tuples:
            gruppe = Gruppe()
            gruppe.set_id(id)
            gruppe.set_name(name)
            gruppe.set_teilnehmerzahl(teilnehmerzahl)
            gruppe.set_teilnehmerListe(teilnehmerListe)
            gruppe.set_max_teilnehmer(max_teilnehmer)
            result.append(gruppe)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_gruppe(self, gruppe):
        """Suchen einer Gruppe aus der Datenbank nach der angegebenen Gruppe
            :param gruppe_name -> gruppe-Objekt
            return Gruppe Objekt, welches mit der Gruppe übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, gruppe FROM gruppen WHERE gruppe='{}'".format(gruppe)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, name, Teilnehmerzahl, teilnehmerListe, max_teilnehmer) = tuples[0]
                gruppe = Gruppe()
                gruppe.set_id(id)
                gruppe.set_name(name)
                gruppe.set_teilnehmerzahl(teilnehmerzahl)
                gruppe.set_teilnehmerListe(teilnehmerListe)
                gruppe.set_max_teilnehmer(max_teilnehmer)
                result = gruppe

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen einer Gruppe nach der übergebenen Id.

        :param id Primärschlüsselattribut einer Gruppe aus der Datenbank
        :return Gruppe Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, name FROM gruppen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id,name, teilnehmerzahl, teilnehmerListe, max_teilnehmer) = tuples[0]
            gruppe = Gruppen()
            gruppe.set_id(id)
            gruppe.set_name(name)
            gruppe.set_teilnehmerzahl(teilnehmerzahl)
            gruppe.set_teilnehmerListe(teilnehmerListe)
            gruppe.set_max_teilnehmer(max_teilnehmer)
            result = gruppe

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def insert(self, gruppe):
        """Einfügen eines Gruppen Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param Gruppe des zu speichernde Gruppen Objekts
        :return das bereits übergebene Gruppen Objekt mit aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM gruppen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                gruppe.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                gruppe.set_id(1)

        command = "INSERT INTO gruppen (id, name, teilnehmerzahl, teilnehmerListe, max_teilnehmer) VALUES (%s,%s,%s,%s,%s)"
        data = (gruppe.get_id(), gruppe.get_name(), gruppe.get_teilnehmerzahl(), gruppe.get_teilnehmerListe(), gruppe.get_max_teilnehmer())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return gruppe

    def update(self, gruppe):
        """Überschreiben / Aktualisieren eines Gruppen-Objekts in der DB

        :param gruppe -> gruppe-Objekt
        :return aktualisiertes gruppe-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE gruppen " + "SET gruppe=%s,  WHERE gruppe=%s"
        data = (gruppe.get_id(), gruppe.get_name(), gruppe.get_teilnehmerzahl(), gruppe.get_teilnehmerListe(), gruppe.get_max_teilnehmer())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_id(self, gruppe):
        """Überschreiben / Aktualisieren eines Gruppen-Objekts in der DB

        :param gruppe -> gruppe-Objekt
        :return aktualisiertes gruppe-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE gruppen " + "SET gruppe=%s, WHERE id=%s"
        data = (gruppe.get_id(), gruppe.get_name(), gruppe.get_teilnehmerzahl(), gruppe.get_teilnehmerListe(), gruppe.get_max_teilnehmer())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, gruppe):
        """Löschen der Daten einer Gruppe aus der Datenbank

        :param gruppe -> gruppe-Objekt
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM gruppen WHERE id={}".format(gruppe.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with GruppeMapper() as mapper:
        result = mapper.find_all()
        for gruppe in result:
            print(gruppe)