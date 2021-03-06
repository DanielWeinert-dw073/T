
#!/usr/bin/python
# -*- coding: utf-8 -*-


from server.db.Mapper import Mapper
from server.bo.Student import Student

class StudentMapper(Mapper):
    """Mapper-Klasse, die Studenten Objekte auf der relationealen Datenbank abbildet.
    Die Klasse ermöglicht die Umwandlung von Objekten in Datenbankstrukturen und umgekehrt
    """

    def __init__(self):
        super().__init__()
        _cnx = None
    def find_all(self):
        """Auslesen aller Studenten aus der Datenbank

        :return Alle Studenten Objekte im System
        """
        result = []

        cursor = self._cnx.cursor()

        command = "SELECT id, name, email, google_user_id FROM studenten"

        cursor.execute(command)
        tuples = cursor.fetchall()

        for (id, name, email, google_user_id) in tuples:
            student = Student()
            student.set_id(id)
            student.set_name(name)
            student.set_email(email)
            student.set_google_user_id(google_user_id)
            result.append(student)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_name(self, name):
        """Suchen eines Studenten aus der Datenbank nach dem angegebenen Namen
            :param student_name -> student-Objekt
            return Student Objekt, welcher mit dem Namen übereinstimmt
            None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, name, email, google_user_id FROM studenten WHERE name='{}'".format(name)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
                (id, name, email, google_user_id) = tuples[0]
                student = Student()
                student.set_id(id)
                student.set_name(name)
                student.set_email(email)
                student.set_google_user_id(google_user_id)
                result = student

        except IndexError:
                """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			    keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
        result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_id(self, id):
        """Suchen eines Studenten nach der übergebenen Id. 

        :param id Primärschlüsselattribut eines Studenten aus der Datenbank
        :return Studenten Objekt, welche mit der Id übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None
        cursor = self._cnx.cursor()
        command = "SELECT id, name, email, google_user_id FROM studenten WHERE id='{}'".format(id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, email, google_user_id) = tuples[0]
            student = Student()
            student.set_id(id)
            student.set_name(name)
            student.set_email(email)
            student.set_google_user_id(google_user_id)
            result = student

        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
			keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None

        self._cnx.commit()
        cursor.close()
        return result

    def find_by_google_user_id(self, google_user_id):
        """Suchen einer student nach der übergebenen Google User ID. 

        :param google_user_id Google User ID einer student aus der Datenbank
        :return student-Objekt, welche mit der Google User ID übereinstimmt,
                None wenn kein Eintrag gefunden wurde
        """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT id, name, email, google_user_id FROM studenten WHERE google_user_id='{}'".format(
                google_user_id)
        cursor.execute(command)
        tuples = cursor.fetchall()

        try:
            (id, name, email, google_user_id) = tuples[0]
            student = Student()
            student.set_id(id)
            student.set_name(name)
            student.set_email(email)
            student.set_google_user_id(google_user_id)
            result = student
        except IndexError:
            """Der IndexError wird oben beim Zugriff auf tuples[0] auftreten, wenn der vorherige SELECT-Aufruf
            keine Tupel liefert, sondern tuples = cursor.fetchall() eine leere Sequenz zurück gibt."""
            result = None
        return result

    def insert(self, student):
        """Einfügen eines Student Objekts in die DB

        Dabei wird auch der Primärschlüssel des übergebenen Objekts geprüft 

        :param Student das zu speichernde Studenten Objekt
        :return das bereits übergebene student Objekt mit aktualisierten Daten (id)
        """
        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(id) AS maxid FROM studenten ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            if maxid[0] is not None:
                """Wenn wir eine maximale ID festellen konnten, zählen wir diese
                um 1 hoch und weisen diesen Wert als ID dem User-Objekt zu."""
                student.set_id(maxid[0] + 1)
            else:
                """Wenn wir KEINE maximale ID feststellen konnten, dann gehen wir
                davon aus, dass die Tabelle leer ist und wir mit der ID 1 beginnen können."""
                student.set_id(1)

        command = "INSERT INTO studenten (id, name, email, google_user_id) VALUES (%s,%s,%s,%s)"
        data = (student.get_id(), student.get_name(), student.get_email(), student.get_google_user_id())
        cursor.execute(command, data)
        print("User anlegen" & student.get_email())
        self._cnx.commit()
        cursor.close()

        return student

    def update(self, student):
        """Überschreiben / Aktualisieren eines student-Objekts in der DB

        :param student -> student-Objekt
        :return aktualisiertes student-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE studenten SET name=%s, email=%s WHERE google_user_id=%s"
        data = (student.get_name(), student.get_email(), student.get_google_user_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_id(self, student):
        """Überschreiben / Aktualisieren eines student-Objekts in der DB

        :param student -> student-Objekt
        :return aktualisiertes student-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE studenten " + "SET name=%s, email=%s,  WHERE id=%s"
        data = (student.get_name(), student.get_email(), student.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def update_by_google_user_id(self, student):
        """Überschreiben / Aktualisieren eines student-Objekts in der DB

        :param student -> student-Objekt
        :return aktualisiertes student-Objekt
        """
        cursor = self._cnx.cursor()

        command = "UPDATE studenten " + "SET name=%s, email=%s,  WHERE id=%s"
        data = (student.get_name(), student.get_email(), student.get_id())

        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def delete(self, student):
        """Löschen der Daten eines Studenten aus der Datenbank

        :param student -> student-Objekt
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM studenten WHERE id={}".format(student.get_id())
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()



'''Tester'''

if (__name__ == "__main__"):
    with StudentMapper() as mapper:
        result = mapper.find_all()
        for student in result:
            print(student)