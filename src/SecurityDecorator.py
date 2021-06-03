from flask import request
from google.auth.transport import requests
import google.oauth2.id_token

from server.LerngruppenAdministration import LerngruppenAdministration

def secured(function):
firebase_request_adapter = requests.Request()

    def wrapper(*args, **kwargs):
        '''
        Hier werden alle in Cookies, welche in der Anmeldung vergeben werden, abgefragt
        '''
        id_token = request.cookies.get("token")
        name = request.cookies.get("name")
        error_message = None
        claims = None
        objects = None

        if id_token:
            try:
                #hier wird der firebase token verifiziert
                claims = google.oauth2.id_token.verify_firebase_token(
                    id_token, firebase_request_adapter)

                if claims is not None:
                    adm = LerngruppenAdministration()

                    google_user_id = claims.get("user_id")
                    email = claims.get("email")
                    name = claims.get("name")
                    user = adm.get_user_by_google_user_id(google_user_id)

                    if user is not None:
                                ''' 
                                Der Student befindet sich bereits in der Datenbank.
                                Demnach wird das Student BO aktualisiert
                                '''
                            user.set_name(name)
                            user.set_email(email)
                            adm.save_user(user)
                    else:
                            '''
                            Das System kennt die Person nicht.
                            Es wird eine neue Person angelegt
                            '''
                        user = adm.create_user(name, email, google_user_id)

                    print(request.method, request.path, 'asked by:', name, email)

                    objects = function(*args, **kwargs)
                    return objects
            else:
                    return '', 401  # UNAUTHORIZED
        except ValueError as exc:
                '''
                If checks failed (token expired etc this exception will be raised)
                '''
                error_message = str(exc)
                return exc, 401  # UNAUTHORIZED
        return '', 401  # UNAUTHORIZED

    return wrapper
