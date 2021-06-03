#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Empfehlung import Empfehlung

class EmpfehlungMapper(Mapper):
    """Mapper-Klasse, die Empfehlungen Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """Auslesen aller Empfehlungen aus der Datenbank

        :return Alle Empfehlungen Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe FROM empfehlungen"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, empfehlung, empfehlungsListe, empfehlungGruppe, empfehlungProfil) in tuples:
            empfehlung = Empfehlung()
            empfehlung.set_id(id)
            empfehlung.set_empfehlung(empfehlung)
            empfehlung.set_empfehlungsListe(empfehlungsListe)
            empfehlung.set_empfehlungGruppe(empfehlungGruppe)
            empfehlung.set_empfehlungProfil(empfehlungProfil)
            result.append(empfehlung)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_empfehlung(self,empfehlung):
        """Suchen eines empfehlungen aus der Datenbank nach dem angegebenen Namen
            :param empfehlung_empfehlung -> empfehlung-Objekt
            return empfehlung Objekt, welcher mit dem Namen übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil FROM empfehlungen WHERE empfehlung='{}'".format(empfehlung)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, empfehlung, empfehlungsListe, empfehlungGruppe, empfehlungProfil) = tuples[0]
                empfehlung = Empfehlung()
                empfehlung.set_id(id)
                empfehlung.set_empfehlung(empfehlung)
                empfehlung.set_empfehlungsListe(empfehlungsListe)
                empfehlung.set_empfehlungGruppe(empfehlungGruppe)
                empfehlung.set_empfehlungProfil(empfehlungProfil)
                result = empfehlung

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines empfehlungen nach der übergebenen Id. 

        :param id Primärschlüsselattribut eines empfehlungen aus der Datenbank
        :return empfehlungen Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe, empfehlungProfil FROM empfehlungen WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil) = tuples[0]
            empfehlung = Empfehlung()
            empfehlung.set_id(id)
            empfehlung.set_empfehlung(empfehlung)
            empfehlung.set_empfehlungsListe(empfehlungsListe)
            empfehlung.set_empfehlungGruppe(empfehlungGruppe)
            empfehlung.set_empfehlungProfil(empfehlungProfil)
            result = empfehlung

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_empfehlungGruppe(self, empfehlungGruppe):
        """Suchen einer empfehlung nach der übergebenen Gruppenempfehlung. 

        :param empfehlungGruppe einer empfehlung aus der Datenbank
        :return empfehlung-Objekt, welche mit derGruppenempfehlung übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe, empfehlungProfil FROM empfehlungen WHERE empfehlungGruppe='{}'".format(
                empfehlungGruppe)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil) = tuples[0]
            empfehlung = Empfehlung()
            empfehlung.set_id(id)
            empfehlung.set_empfehlung(empfehlung)
            empfehlung.set_empfehlungsListe(empfehlungsListe)
            empfehlung.set_empfehlungGruppe(empfehlungGruppe)
            empfehlung.set_empfehlungProfil(empfehlungProfil)
            result = empfehlung
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def find_by_empfehlungsListe(self, empfehlungsListe):
        """Suchen einer empfehlung nach der übergebenen Empfehlung. 

        :param empfehlungGruppe einer empfehlung aus der Datenbank
        :return empfehlung-Objekt, welche mit der Empfehlung übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe FROM empfehlungen WHERE empfehlungGruppe='{}'".format(
                empfehlungsListe)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil) = tuples[0]
            empfehlung = Empfehlung()
            empfehlung.set_id(id)
            empfehlung.set_empfehlung(empfehlung)
            empfehlung.set_empfehlungsListe(empfehlungsListe)
            empfehlung.set_empfehlungGruppe(empfehlungGruppe)
            empfehlung.set_empfehlungProfil(empfehlungProfil)
            result = empfehlung
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def find_by_empfehlungProfil(self, empfehlungProfil):
        """Suchen einer empfehlung nach der übergebenen Empfehlung. 

        :param empfehlungGruppe einer empfehlung aus der Datenbank
        :return empfehlung-Objekt, welche mit der Empfehlung übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, empfehlung, empfehlungsListe, empfehlungGruppe FROM empfehlungen WHERE empfehlungGruppe='{}'".format(
                empfehlungProfil)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, empfehlung, empfehlungsListe, empfehlungGruppe,empfehlungProfil) = tuples[0]
            empfehlung = Empfehlung()
            empfehlung.set_id(id)
            empfehlung.set_empfehlung(empfehlung)
            empfehlung.set_empfehlungsListe(empfehlungsListe)
            empfehlung.set_empfehlungGruppe(empfehlungGruppe)
            empfehlung.set_empfehlungProfil(empfehlungProfil)
            result = empfehlung
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def insert(self, empfehlung):
        """Einfügen eines empfehlung Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft 

        :param empfehlung das zu speichernde empfehlungen Objekt
        :return das bereits übergebene empfehlung Objekt mit aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM empfehlungen ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem Empfehlung-Objekt zu."""
                empfehlung.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                empfehlung.set_id(1)

        command = "INSERT INTO empfehlungen (id, empfehlung, empfehlungsListe, empfehlungGruppe) VALUES (%s,%s,%s,%s,%s)"
        data = (empfehlung.get_id(), empfehlung.get_empfehlung(), empfehlung.get_empfehlungsListe(), empfehlung.get_empfehlungGruppe(),empfehlung.get_empfehlung_Profil())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return empfehlung

    def update(self, empfehlung):
        """Überschreiben / Aktualisieren eines empfehlung-Objekts in der DB

        :param empfehlung -> empfehlung-Objekt
        :return aktualisiertes empfehlung-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE empfehlungen " + "SET empfehlung=%s, empfehlungsListe=%s,empfehlungGruppe=%s,empfehlungProfil()=%s WHERE empfehlungGruppe=%s"
        data = (empfehlung.get_empfehlung(), empfehlung.get_empfehlungsListe(), empfehlung.get_empfehlungGruppe(), empfehlung.get_empfehlungProfil())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_id(self, empfehlung):
        """Überschreiben / Aktualisieren eines empfehlung-Objekts in der DB

        :param empfehlung -> empfehlung-Objekt
        :return aktualisiertes empfehlung-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE empfehlungen " + "SET empfehlung=%s, empfehlungsListe=%s, empfehlungGruppe=%s, empfehlungProfil=%s WHERE id=%s"
        data = (empfehlung.get_empfehlung(), empfehlung.get_empfehlungsListe(), empfehlung.get_id(), empfehlung.get_empfehlungGruppe(),
         empfehlung.get_empfehlungProfil())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, empfehlung):
        """Löschen der Daten eines empfehlungen aus der Datenbank

        :param empfehlung -> empfehlung-Objekt
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM empfehlungen WHERE id={}".format(empfehlung.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with EmpfehlungMapper() as mapper:
        result = mapper.find_all()
        for empfehlung in result:
            print(empfehlung)