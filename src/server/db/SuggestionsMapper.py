#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Suggestion_Algorithmus import Suggestion_Algorithmus

class Suggestion_AlgorithmusMapper(Mapper):
    """Mapper-Klasse, die Suggestion_Algorithmusen Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Profile die durch den Suggestion_Algorithmus aus der Datenbank ausgeles

        :return Alle Suggestion_Algorithmus Objekte im System
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, lerntyp_Id, lernvorlieben_Id,profil_Id, gruppen_Id FROM Suggestion_Algorithmusen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, lerntyp, lernvorlieben, profil, gruppen) in tuples:
            suggestion_Algorithmus = Suggestion_Algorithmus()
            suggestion_Algorithmus.set_id(id)
            suggestion_Algorithmus.set_lerntyp_Id(lerntyp)
            suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben)
            suggestion_Algorithmus.set_profil_Id(profil)
            suggestion_Algorithmus.set_gruppen_Id(gruppen)
            result.append(Suggestion_Algorithmus)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_lerntyp_Id(self,lerntyp_Id):
        """Suchen eines Suggestion_Algorithmusen aus der Datenbank nach dem angegebenen Lerntyp
            :param Suggestion_Algorithmus_lerntyp_Id -> Suggestion_Algorithmus-Objekt
            return Suggestion_Algorithmus Objekt, welcher mit dem Lerntyp übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp_Id, lernvorlieben_Id, profil_Id, gruppen_Id FROM Suggestion_Algorithmusen WHERE lerntyp_Id='{}'".format(lerntyp_Id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, lerntyp, lernvorlieben, profil_Id,gruppen) = tuples[0]
                suggestion_Algorithmus = Suggestion_Algorithmus()
                suggestion_Algorithmus.set_id(id)
                suggestion_Algorithmus.set_lerntyp_Id(lerntyp)
                suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben)
                suggestion_Algorithmus.set_profil_Id(profil_Id)
                suggestion_Algorithmus.set_gruppen_Id(gruppen)
                result = Suggestion_Algorithmus

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_lernvorlieben_Id(self,lernvorlieben_Id):
        """Suchen eines Suggestion_Algorithmusen aus der Datenbank nach der angegebenen Lernvorliebe
            :param Suggestion_Algorithmus_lernvorlieben_Id -> Suggestion_Algorithmus-Objekt
            return Suggestion_Algorithmus Objekt, welcher mit der Lernvorliebe übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp_Id, lernvorlieben_Id, profil_Id, abc FROM Suggestion_Algorithmusen WHERE lernvorlieben_Id='{}'".format(lernvorlieben_Id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, lerntyp, lernvorlieben, profil_Id,gruppen) = tuples[0]
                suggestion_Algorithmus = Suggestion_Algorithmus()
                suggestion_Algorithmus.set_id(id)
                suggestion_Algorithmus.set_lerntyp_Id(lerntyp)
                suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben)
                suggestion_Algorithmus.set_profil_Id(profil_Id)
                suggestion_Algorithmus.set_gruppen_Id(gruppen)
                result = Suggestion_Algorithmus

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines Suggestion_Algorithmusen nach der übergebenen Id. 

        :param id Primärschlüsselattribut eines Suggestion_Algorithmusen aus der Datenbank
        :return Suggestion_Algorithmusen Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp_Id, lernvorlieben_Id, profil_Id, gruppen_Id FROM Suggestion_Algorithmusen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, lerntyp_Id, lernvorlieben_Id, profil,gruppen) = tuples[0]
            suggestion_Algorithmus = Suggestion_Algorithmus()
            suggestion_Algorithmus.set_id(id)
            suggestion_Algorithmus.set_lerntyp_Id(lerntyp_Id)
            suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben_Id)
            suggestion_Algorithmus.set_profil_Id(profil)
            suggestion_Algorithmus.set_gruppen_Id(gruppen)
            result = Suggestion_Algorithmus

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_profil_Id(self, profil_Id):
        """Suchen einer Suggestion_Algorithmus nach der übergebenen Profil ID. 

        :param profil_Id einer Suggestion_Algorithmus aus der Datenbank
        :return Suggestion_Algorithmus-Objekt, welche mit der Profil ID übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp_Id, lernvorlieben_Id, profil_Id FROM Suggestion_Algorithmusen WHERE profil_Id='{}'".format(
                profil_Id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, lerntyp_Id, lernvorlieben_Id, profil, gruppen) = tuples[0]
            suggestion_Algorithmus = Suggestion_Algorithmus()
            suggestion_Algorithmus.set_id(id)
            suggestion_Algorithmus.set_lerntyp_Id(lerntyp_Id)
            suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben_Id)
            suggestion_Algorithmus.set_profil_Id(profil)
            suggestion_Algorithmus.set_gruppen_Id(gruppen)
            result = Suggestion_Algorithmus
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def find_by_gruppen_Id(self, gruppen_Id):
        """Suchen einer Suggestion_Algorithmus nach der übergebenen Profil ID. 

        :param profil_Id einer Suggestion_Algorithmus aus der Datenbank
        :return Suggestion_Algorithmus-Objekt, welche mit der Profil ID übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._connection.cursor()
        command = "SELECT id, lerntyp_Id, lernvorlieben_Id, profil_Id FROM Suggestion_Algorithmusen WHERE profil_Id='{}'".format(
                gruppen_Id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, lerntyp_Id, lernvorlieben_Id, profil, gruppen) = tuples[0]
            suggestion_Algorithmus = Suggestion_Algorithmus()
            suggestion_Algorithmus.set_id(id)
            suggestion_Algorithmus.set_lerntyp_Id(lerntyp_Id)
            suggestion_Algorithmus.set_lernvorlieben_Id(lernvorlieben_Id)
            suggestion_Algorithmus.set_profil_Id(profil)
            suggestion_Algorithmus.set_gruppen_Id(gruppen)
            result = Suggestion_Algorithmus
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def insert(self, Suggestion_Algorithmus):
        """Einfügen eines Suggestion_Algorithmus Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft 

        :param Suggestion_Algorithmus das zu speichernde Suggestion_Algorithmusen Objekt
        :return das bereits übergebene Suggestion_Algorithmus Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM Suggestion_Algorithmusen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                Suggestion_Algorithmus.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                Suggestion_Algorithmus.set_id(1)

        command = "INSERT INTO Suggestion_Algorithmusen (id, lerntyp_Id, lernvorlieben_Id, profil_Id) VALUES (%s,%s,%s,%s)"
        data = (Suggestion_Algorithmus.get_id(), Suggestion_Algorithmus.get_lerntyp_Id(), Suggestion_Algorithmus.get_lernvorlieben_Id(), Suggestion_Algorithmus.get_profil_Id())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return Suggestion_Algorithmus

    def update(self, Suggestion_Algorithmus):
        """Überschreiben / Aktualisieren eines Suggestion_Algorithmus-Objekts in der DB

        :param Suggestion_Algorithmus -> Suggestion_Algorithmus-Objekt
        :return aktualisiertes Suggestion_Algorithmus-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE Suggestion_Algorithmusen " + "SET lerntyp_Id=%s, lernvorlieben_Id=%s WHERE profil_Id=%s"
        data = (Suggestion_Algorithmus.get_lerntyp_Id(), Suggestion_Algorithmus.get_lernvorlieben_Id(), Suggestion_Algorithmus.get_profil_Id())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def update_by_id(self, Suggestion_Algorithmus):
        """Überschreiben / Aktualisieren eines Suggestion_Algorithmus-Objekts in der DB

        :param Suggestion_Algorithmus -> Suggestion_Algorithmus-Objekt
        :return aktualisiertes Suggestion_Algorithmus-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE Suggestion_Algorithmusen " + "SET lerntyp_Id=%s, lernvorlieben_Id=%s,  WHERE id=%s"
        data = (Suggestion_Algorithmus.get_lerntyp_Id(), Suggestion_Algorithmus.get_lernvorlieben_Id(), Suggestion_Algorithmus.get_id())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, Suggestion_Algorithmus):
        """Löschen der Daten eines Suggestion_Algorithmusen aus der Datenbank

        :param Suggestion_Algorithmus -> Suggestion_Algorithmus-Objekt
        """
        cursor = self._connection.cursor()

        command = "DELETE FROM Suggestion_Algorithmusen WHERE id={}".format(Suggestion_Algorithmus.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with Suggestion_AlgorithmusMapper() as mapper:
        result = mapper.find_all()
        for Suggestion_Algorithmus in result:
            print(Suggestion_Algorithmus)