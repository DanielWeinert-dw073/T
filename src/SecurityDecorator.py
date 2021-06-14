from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from server.LerngruppenAdministration import LerngruppenAdministration

def secured(function):

    firebase_request_adapter = requests.Request()

    def wrapper(*args, **kwargs):
        # Verify Firebase auth.
        id_token = request.cookies.get("token")
        name = request.cookies.get("name")
        email = request.cookies.get("email")
        error_message = None
        claims = None
        objects = None
        print("Security loaded")
        if id_token:
            try:
                # Verify the token against the Firebase Auth API. This example
                # verifies the token on each page load. For improved performance,
                # some applications may wish to cache results in an encrypted
                # session store (see for instance
                # http://flask.pocoo.org/docs/1.0/quickstart/#sessions).
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter)

                if claims is not None:
                    adm = LerngruppenAdministration()

                    google_user_id = claims.get("user_id")
                    email = claims.get("email")
                    name = claims.get("name")

                    student = adm.get_student_by_google_user_id(google_user_id)
                    if student is not None:
 
                        student.set_name(name)
                        student.set_email(email)
                        adm.save_student(student)
                        print("saved student")
                    else:
                        print("create student")
                        student = adm.create_student(name, email, google_user_id)

                    print(request.method, request.path, "angefragt durch:", name, email)

                    objects = function(*args, **kwargs)
                    return objects
                else:
                    return '', 401  # UNAUTHORIZED !!!
            except ValueError as exc:
                # This will be raised if the token is expired or any other
                # verification checks fail.
                error_message = str(exc)
                return exc, 401  # UNAUTHORIZED !!!

        return '', 401  # UNAUTHORIZED !!!

    return wrapper

