#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Konversation import Konversation

class KonversationMapper(Mapper):
    """Mapper-Klasse, die Konversation Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Konversationen aus der Datenbank

        :return Alle Konversationen Objekte im System
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt FROM konversationen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt) in tuples:
            konversation = Konversation()
            konversation.set_id(id)
            konversation.set_konversation(konversation)
            konversation.set_nachricht_id(nachricht_id)
            konversation.set_teilnehmer(teilnehmer)
            konversation.set_herkunfts_id(herkunfts_id)
            konversation.set_ziel_id(ziel_id)
            konversation.set_inhalt(inhalt)
            result.append(konversation)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_konversation(self,konversation):
        """Suchen einer Konversation aus der Datenbank nach dem angegebenen Namen
            :param konversation_konversation -> konversation-Objekt
            return konversation Objekt, welcher mit dem Namen übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt FROM konversationen WHERE konversation='{}'".format(konversation)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt) = tuples[0]
                konversation = Konversation()
                konversation.set_id(id)
                konversation.set_konversation(konversation)
                konversation.set_nachricht_id(nachricht_id)
                konversation.set_teilnehmer(teilnehmer)
                konversation.set_herkunfts_id(herkunfts_id)
                konversation.set_ziel_id(ziel_id)
                konversation.set_inhalt(inhalt)
                result = konversation

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen einer Konversation nach der übergebenen Id.

        :param id Primärschlüsselattribut einer Konversation aus der Datenbank
        :return konversationen Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt FROM konversationen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt) = tuples[0]
            konversation = Konversation()
            konversation.set_id(id)
            konversation.set_konversation(konversation)
            konversation.set_nachricht_id(nachricht_id)
            konversation.set_teilnehmer(teilnehmer)
            konversation.set_herkunfts_id(herkunfts_id)
            konversation.set_ziel_id(ziel_id)
            konversation.set_inhalt(inhalt)
            result = konversation

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_teilnehmer(self, teilnehmer):
        """Suchen einer Konversation nach dem übergebenen Teilnehmer.

        :param teilnehmer einer konversation aus der Datenbank
        :return teilnehmer-Objekt, welche mit der Gruppe übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._connection.cursor()
        command = "SELECT id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt  FROM konversationen WHERE teilnehmer='{}'".format(
                teilnehmer)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt) = tuples[0]
            konversation=Konversation()
            konversation.set_id(id)
            konversation.set_konversation(konversation)
            konversation.set_nachricht_id(nachricht_id)
            konversation.set_teilnehmer(teilnehmer)
            konversation.set_herkunfts_id(herkunfts_id)
            konversation.set_ziel_id(ziel_id)
            konversation.set_inhalt(inhalt)
            result = konversation

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def find_by_inhalt(self, inhalt):
        """Suchen einer Konversation nach dem übergebenen Inhalt.

        :param Inhalt einer Konversation aus der Datenbank
        :return Inhalt-Objekt, welche mit der Konversation übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._connection.cursor()
        command = "SELECT id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt  FROM konversationen WHERE inhalt='{}'".format(
                inhalt)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt) = tuples[0]
            konversation=Konversation()
            konversation.set_id(id)
            konversation.set_konversation(konversation)
            konversation.set_nachricht_id(nachricht_id)
            konversation.set_teilnehmer(teilnehmer)
            konversation.set_herkunfts_id(herkunfts_id)
            konversation.set_ziel_id(ziel_id)
            konversation.set_inhalt(inhalt)
            result=konversation

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result


    def insert(self, konversation):
        """Einfügen eines konversation Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param konversation das zu speichernde konversation Objekt
        :return das bereits übergebene konversation Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM konversationen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem Konversation-Objekt zu."""
                konversation.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                konversation.set_id(1)

        command = "INSERT INTO konversationen (id, konversation, nachricht_id, teilnehmer, herkunfts_id, ziel_id, inhalt ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (konversation.get_id(), konversation.get_konversation(), konversation.get_nachricht_id (), konversation.get_teilnehmer(), konversation.get_herkunfts_id(), konversation.get_ziel_id(), konversation.get_inhalt())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return konversation

    def update(self, konversation):
        """Überschreiben / Aktualisieren eines konversation-Objekts in der DB

        :param konversation -> konversation-Objekt
        :return aktualisiertes konversation-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE konversationen " + "SET konversation=%s, nachricht_id=%s,teilnehmer=%s,herkunfts_id=%s,ziel_id=%s,inhalt=%s ()=%s WHERE konversation=%s"
        data = (konversation.get_konversation(), konversation.get_nachricht_id (), konversation.get_teilnehmer(), konversation.get_herkunfts_id(), konversation.get_ziel_id(), konversation.get_inhalt())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def update_by_id(self, konversation):
        """Überschreiben / Aktualisieren eines konversation-Objekts in der DB

        :param konversation -> konversation-Objekt
        :return aktualisiertes konversation-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE konversationen " + "SET konversation=%s, nachricht_id=%s,teilnehmer=%s,herkunfts_id=%s,ziel_id=%s,inhalt=%s WHERE id=%s"
        data = (konversation.get_konversation(), konversation.get_nachricht_id (), konversation.get_teilnehmer(), konversation.get_herkunfts_id(), konversation.get_ziel_id(), konversation.get_inhalt())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, konversation):
        """Löschen der Daten eines konversation aus der Datenbank

        :param konversation -> konversation-Objekt
        """
        cursor = self._connection.cursor()

        command = "DELETE FROM konversationen WHERE id={}".format(konversation.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with KonversationMapper() as mapper:
        result = mapper.find_all()
        for konversation in result:
            print(konversation)