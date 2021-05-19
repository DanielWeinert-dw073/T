#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import name
from server.db.Mapper import Mapper
from server.bo.Profil import Profil

class ProfilMapper(Mapper):
    """Mapper-Klasse, die Profil Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Profile aus der Datenbank

        :return Alle Profil Objekte im System
        """
        result = []

        cursor = self._connection.cursor()

        command = "SELECT id, name faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen FROM profile"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen) in tuples:
            profil = Profil()
            profil.set_id(id)
            profil.set_name(name)
            profil.set_faecher(faecher)
            profil.set_alter(alter)
            profil.set_studiengang(studiengang)
            profil.set_wohnort(wohnort)
            profil.set_semester(semester)
            profil.set_vorwissen(vorwissen)
            profil.set_lernvorlieben(lernvorlieben)
            profil.set_about_me(about_me)
            profil.set_sprachen(sprachen)
            result.append(profil)

        self._connection.commit()
        cursor.close()

        return result

    def find_by_name(self,name):
        """Suchen eines Profiles aus der Datenbank nach dem angegebenen Namen
            :param profil_name -> profil-Objekt
            return Profil Objekt, welcher mit dem Namen übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me FROM profil WHERE name='{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen) = tuples[0]
                profil = Profil()
                profil.set_id(id)
                profil.set_name(name)
                profil.set_faecher(faecher)
                profil.set_alter(alter)
                profil.set_studiengang(studiengang)
                profil.set_wohnort(wohnort)
                profil.set_semester(semester)
                profil.set_vorwissen(vorwissen)
                profil.set_lernvorlieben(lernvorlieben)
                profil.set_about_me(about_me)
                profil.set_sprachen(sprachen)
                result = profil

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines Profiles nach der übergebenen Id.

        :param id Primärschlüsselattribut eines Profiles aus der Datenbank
        :return Profil Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me,sprachen  FROM profile WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen ) = tuples[0]
            profil = Profil()
            profil.set_id(id)
            profil.set_name(name)
            profil.set_faecher(faecher)
            profil.set_alter(alter)
            profil.set_studiengang(studiengang)
            profil.set_wohnort(wohnort)
            profil.set_semester(semester)
            profil.set_vorwissen(vorwissen)
            profil.set_lernvorlieben(lernvorlieben)
            profil.set_about_me(about_me)
            profil.set_sprachen(sprachen)
            result = profil

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def find_by_lernvorlieben(self, lernvorlieben):
        """Suchen eines Profiles nach der übergebenen Lernvorlieben.

        :param Lernvorlieben Attribut eines Profiles aus der Datenbank
        :return Profil Objekt, welche mit den lernvorlieben übereinstimmen,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._connection.cursor()
        command = "SELECT id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me,sprachen  FROM profile WHERE lernvorlieben='{}'".format(lernvorlieben)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen ) = tuples[0]
            profil = Profil()
            profil.set_id(id)
            profil.set_name(name)
            profil.set_faecher(faecher)
            profil.set_alter(alter)
            profil.set_studiengang(studiengang)
            profil.set_wohnort(wohnort)
            profil.set_semester(semester)
            profil.set_vorwissen(vorwissen)
            profil.set_lernvorlieben(lernvorlieben)
            profil.set_about_me(about_me)
            profil.set_sprachen(sprachen)
            result = profil

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._connection.commit()
        cursor.close()
        return result

    def insert(self, profil):
        """Einfügen eines Profil Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft

        :param Profil das zu speichernde Profile Objekt
        :return das bereits übergebene profil Objekt mit aktualisierten Daten (id)
        """
        cursor = self._connection.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM profile ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                profil.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                profil.set_id(1)

        command = "INSERT INTO profile (id, name, faecher, alter, studiengang, wohnort, semester, vorwissen, lernvorlieben, about_me, sprachen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (profil.get_id(), profil.get_name(), profil.get_faecher(), profil.alter(), profil.get_studiengang(), profil.get_wohnort(), profil.get_semester(), profil.get_vorwissen(), profil.get_lernvorlieben(), profil.get_about_me(), profil.get_sprachen())
        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

        return profil

    def update(self, profil):
        """Überschreiben / Aktualisieren eines profil-Objekts in der DB

        :param profil -> profil-Objekt
        :return aktualisiertes profil-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE profile " + "SET name=%s WHERE id=%s"
        data = (profil.get_id(), profil.get_name(), profil.get_faecher(), profil.alter(), profil.get_studiengang(), profil.get_wohnort(), profil.get_semester(), profil.get_vorwissen(), profil.get_lernvorlieben(), profil.get_about_me(), profil.get_sprachen())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def update_by_id(self, profil):
        """Überschreiben / Aktualisieren eines student-Objekts in der DB

        :param profil -> profil-Objekt
        :return aktualisiertes profil-Objekt
        """
        cursor = self._connection.cursor()

        command = "UPDATE profile " + "SET name=%s, WHERE id=%s"
        data = (profil.get_name(), profil.get_id())

        cursor.execute(command, data)

        self._connection.commit()
        cursor.close()

    def delete(self, profil):
        """Löschen der Daten eines Profiles aus der Datenbank

        :param profil -> profil-Objekt
        """
        cursor = self._connection.cursor()

        command = "DELETE FROM profile WHERE id={}".format(profil.get_id())
        cursor.execute(command)

        self._connection.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with ProfilMapper() as mapper:
        result = mapper.find_all()
        for profil in result:
            print(profil)