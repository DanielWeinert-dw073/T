import StudentNBO from './StudentNBO';
import TeilnahmeBO from './TeilnahmeBO';
//import EmpfehlungBO from '../EmpfehlungBO';
import ProfilNBO from './ProfilNBO';
import GruppeNBO from './GruppeNBO';
//import KonversationBO from './KonversationBO';
import LerntypBO from './LerntypBO';
import LernvorliebenBO from './LernvorliebenBO';
import NachrichtBO from './NachrichtBO';


/** 
 * Singelton Abstraktion des backends REST Interface. 
 * Dabei handelt es sich um eine access Methode.
*/

export default class LernGruppenToolAPI {

    //singelton instance
    static #api = null;

    //Lokales Python backend
    #LernGruppenToolServerBaseURL = "/LernGruppenToolApp";

    //Lokales Python backend
    //#LerngruppenToolBaseURL = "https://lerngruppenapp.oa.r.appspot.com/LernGruppenToolApp";

    //Student-Related
    #getStudentenURL = () => `${this.#LernGruppenToolServerBaseURL}/studenten`;
    #addStudentenURL = () => `${this.#LernGruppenToolServerBaseURL}/studenten`;
    #getStudentenByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/studenten/${id}`;
    #getStudentenByGoogleIdURL = (google_user_id) => `${this.#LernGruppenToolServerBaseURL}/studenten/${google_user_id}`;
    #updateStudentenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/studenten/${id}`;
    #deleteStudentenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/studenten/${id}`;


    //Teilnahme Related
    #getTeilnahmenURL = () => `${this.#LernGruppenToolServerBaseURL}/teilnahmen`;
    #getTeilnahmenByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/teilnahmen/${id}`;
    #addTeilnahmenURL = () => `${this.#LernGruppenToolServerBaseURL}/teilnahmen`;
    #updateTeilnahmenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/teilnahmen/${id}`;
    #deleteTeilnahmenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/teilnahmen/${id}`;
    #getTeilnahmenByStudentenURL = (studenten) => `${this.#LernGruppenToolServerBaseURL}/teilnahmen-by-studenten/${studenten}`;


    //Profil-Related
    #getProfileURL = () => `${this.#LernGruppenToolServerBaseURL}/profile`;
    #getProfileByStudentenIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/studenten/${id}`;
    #getProfileByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/${id}`;
    #getProfileByLerntypen= (lerntypen_Id) => `${this.#LernGruppenToolServerBaseURL}/profile/${lerntypen_Id}`;
    #getProfileByLernvorlieben= (lernvorlieben_id) => `${this.#LernGruppenToolServerBaseURL}/profile/${lernvorlieben_id}`;
    #addProfileURL = () => `${this.#LernGruppenToolServerBaseURL}/profile`;
    #updateProfileURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/${id}`;
    #deleteProfileURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/${id}`;


    //Gruppe-Related
    #getGruppenURL = () => `${this.#LernGruppenToolServerBaseURL}/gruppen`;
    #getGruppenByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${id}`;
    #getGruppenByTeilnahmenURL = (teilnahmen) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${teilnahmen}`;
    #getGruppenByNamenURL = (namen) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${namen}`;
    #getGruppenByLernvorliebenURL = (lernvorlieben) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${lernvorlieben}`;
    #getGruppenByLerntypenURL = (lerntypen) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${lerntypen}`;
    #addGruppenURL = () => `${this.#LernGruppenToolServerBaseURL}/gruppen`;
    #updateGruppenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${id}`;
    #deleteGruppenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/gruppen/${id}`;


    //Lerntyp-Related
    #getLerntypenURL = () => `${this.#LernGruppenToolServerBaseURL}/lerntypen`;
    #getLerntypenByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lerntypen/${id}`;
    #addLerntypenURL = () => `${this.#LernGruppenToolServerBaseURL}/lerntypen`;
    #updateLerntypenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lerntypen/${id}`;
    #deleteLerntypenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lerntypen/${id}`;


    //Lernvorlieben-Related
    #getLernvorliebenURL = () => `${this.#LernGruppenToolServerBaseURL}/lernvorlieben`;
    #getLernvorliebenByIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lernvorlieben/${id}`;
    #addLernvorliebenURL = () => `${this.#LernGruppenToolServerBaseURL}/lernvorlieben`;
    #updateLernvorliebenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lernvorlieben/${id}`;
    #deleteLernvorliebenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/lernvorlieben/${id}`;


    //Nachricht-Related
    #getNachrichtenURL = () => `${this.#LernGruppenToolServerBaseURL}/nachrichten`;
    #getNachrichtenByProfileURL = () => `${this.#LernGruppenToolServerBaseURL}/nachrichten-by-profile`/$`{profile}`;
    #getInhaltByNachrichtenURL = () => `${this.#LernGruppenToolServerBaseURL}/inhalt-by-nachrichten/${nachrichten}`;
    #addNachrichtenURL = () => `${this.#LernGruppenToolServerBaseURL}/nachrichten`;
    #updateNachrichtenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/nachrichten/${id}`;
    #deleteNachrichtenURL = (id) => `${this.#LernGruppenToolServerBaseURL}/nachrichten/${id}`;


// Student-Methoden

    // Student anzeigen
  getStudenten(){
    return this.#fetchAdvanced(this.#getStudentenURL()).then((responseJSON) => {
      let studentNBOs = StudentNBO.fromJSON(responseJSON);
      // console.info(studentNBO);
      return new Promise(function (resolve) {
        resolve(studentNBOs);
      })
    })
   }

// Student hinzufügen
  addStudenten(studentNBO) {
    return this.#fetchAdvanced(this.#addStudentenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(studentNBO)
    }).then((responseJSON) => {
      // We always get an array of StudentNBO.fromJSON, but only need one object
      let responseStudentNBO = StudentNBO.fromJSON(responseJSON)[0];
      // console.info(studentNBO);
      return new Promise(function (resolve) {
        resolve(responseStudentNBO);
      })
    })
  }
//Studenten nach ID auslesen
  getStudenten(studenten_Id) {
    return this.#fetchAdvanced(this.#getStudentenByIdURL(studenten_Id)).then((responseJSON) => {
      // We always get an array of StudentBOs.fromJSON, but only need one object
      let responseStudentNBO = StudentNBO.fromJSON(responseJSON)[0];
      // console.info(responseStudentNBO);
      return new Promise(function (resolve) {
        resolve(responseStudentNBO);
      })
    })
  }
//Studenten nach Google ID auslesen
  getStudentenByGoogleId(google_user_id) {
    return this.#fetchAdvanced(this.#getStudentenByGoogleIdURL(google_user_id)).then((responseJSON) => {
      // We always get an array of StudentNBO.fromJSON, but only need one object
      let studentNBO = StudentNBO.fromJSON(responseJSON)[0];
      // console.info(responseStudentNBO);
      return new Promise(function (resolve) {
        resolve(studentNBO);
      })
    })
  }

//Studenten überarbeiten
  updateStudenten(studentNBO) {
    return this.#fetchAdvanced(this.#updateStudentenURL(studentNBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(studentNBO)
    }).then((responseJSON) => {
      // We always get an array of studentNBO.fromJSON
      let responseStudentNBO = StudentNBO.fromJSON(responseJSON)[0];
      // console.info(studentNBO);
      return new Promise(function (resolve) {
        resolve(responseStudentNBO);
      })
    })
  }
// Studenten löschen
  deleteStudenten(studenten_ID) {
    return this.#fetchAdvanced(this.#deleteStudentenURL(studenten_ID), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of StudentNBO.fromJSON
      let responseStudentNBO = StudentNBO.fromJSON(responseJSON)[0];
      // console.info(studentNBO);
      return new Promise(function (resolve) {
        resolve(responseStudentNBO);
      })
    })
  }

// Teilnahmen-Methoden

    //Teilnahmen anzeigen
  getTeilnahmen(){
    return this.#fetchAdvanced(this.#getTeilnahmenURL()).then((responseJSON) => {
      let teilnahmeBO = TeilnahmeBO.fromJSON(responseJSON);
      // console.info(teilnahmeBO);
      return new Promise(function (resolve) {
        resolve(teilnahmeBO);
      })
    })
   }

    //Teilnahmen durch ID auslesen
  getTeilnahmen(teilnahmen_Id) {
    return this.#fetchAdvanced(this.#getTeilnahmenByIdURL(teilnahmen_Id)).then((responseJSON) => {
      // We always get an array of TeilnahmeBO.fromJSON, but only need one object
      let responseTeilnahmeBO = TeilnahmeBO.fromJSON(responseJSON)[0];
      // console.info(responseTeilnahmeBO);
      return new Promise(function (resolve) {
        resolve(responseTeilnahmeBO);
      })
    })
  }
    //Teilnahmen hinzufügen
    addTeilnahmen(teilnahmeBO) {
    return this.#fetchAdvanced(this.#addTeilnahmenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(teilnahmeBO)
    }).then((responseJSON) => {
      // We always get an array of TeilnahmeBO.fromJSON, but only need one object
      let responseTeilnahmeBO = TeilnahmeBO.fromJSON(responseJSON)[0];
      // console.info(teilnahmeBO);
      return new Promise(function (resolve) {
        resolve(responseTeilnahmeBO);

      })
    })
  }

    //Teilnahmen überarbeiten
    updateTeilnahmen(teilnahmeBO) {
    return this.#fetchAdvanced(this.#updateTeilnahmenURL(teilnahmeBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(teilnahmeBO)
    }).then((responseJSON) => {
      // We always get an array of TeilnahmeBO.fromJSON
      let responseTeilnahmeBO = TeilnahmeBO.fromJSON(responseJSON)[0];
      // console.info(teilnahmeBO);
      return new Promise(function (resolve) {
        resolve(responseTeilnahmeBO);
      })
    })
  }

    //Teilnahmen löschen
  deleteTeilnahmen(teilnahmen_Id) {
    return this.#fetchAdvanced(this.#deleteTeilnahmenURL(teilnahmen_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of TeilnahmeBO.fromJSON
      let responseTeilnahmeBO = TeilnahmeBO.fromJSON(responseJSON)[0];
      // console.info(teilnahmeBO);
      return new Promise(function (resolve) {
        resolve(responseTeilnahmeBO);
      })
    })
  }
     //Teilnahmen durch Studenten auslesen
  getTeilnahmenByStudenten(studenten_Id) {
    return this.#fetchAdvanced(this.#getTeilnahmenByStudentenURL(studenten_Id)).then((responseJSON) => {
      // We always get an array of TeilnahmeBO.fromJSON, but only need one object
      let responseTeilnahmeBO = TeilnahmeBO.fromJSON(responseJSON)[0];
       //console.info(responseTeilnahmeBO);
      return new Promise(function (resolve) {
        resolve(responseTeilnahmeBO);
      })
    })
  }

//Profil-Methoden

    //Profil anzeigen
    getProfile() {
    return this.#fetchAdvanced(this.#getProfileURL()).then((responseJSON) => {
      // We always get an array of ProfilNBO.fromJSON, but only need one object
      let responseProfileNBO = ProfileNBO.fromJSON(responseJSON)[0];
       //console.info(responseProfileNBO);
      return new Promise(function (resolve) {
        resolve(responseProfileNBO);
      })
    })
  }

    //Profil löschen
    deleteProfile(profileID) {
      return this.#fetchAdvanced(this.#deleteProfileURL(profileID), {
        method: 'DELETE'
      }).then((responseJSON) => {
        let responseProfilNBO = ProfilNBO.fromJSON(responseJSON)[0];
        // console.info(accountBOs);
        return new Promise(function (resolve) {
          resolve(responseProfilNBO);
        })
      })
     };

    //Profil nach Id auslesen
    getProfileById(profile_Id) {
    return this.#fetchAdvanced(this.#getProfileByIdURL(profile_Id)).then((responseJSON) => {
      // We always get an array of ProfilNBO.fromJSON, but only need one object
      let responseProfilNBO = ProfilNBO.fromJSON(responseJSON)[0];
       //console.info(responseProfileNBO);
      return new Promise(function (resolve) {
        resolve(responseProfilNBO);
      })
    })
  }

    //Profil hinzufügen
    addProfile(profilNBO) {
      return this.#fetchAdvanced(this.#addProfileURL(), {
        method: 'POST',
        headers: {
          'Accept': 'application/json, text/plain',
          'Content-type': 'application/json',
        },
        body: JSON.stringify(profilNBO)
      }).then((responseJSON) => {
        // We always get an array of StudentBOs.fromJSON, but only need one object
        let responseProfilNBO = ProfilNBO.fromJSON(responseJSON)[0];
        // console.info(studentBOs);
        return new Promise(function (resolve) {
          resolve(responseProfilNBO);
        })
      })
    }

    //Profil nach Lerntyp auslesen
    getProfileByLerntypen(lerntypen_Id) {
    return this.#fetchAdvanced(this.#getProfileByLerntypenURL(lerntypen_Id)).then((responseJSON) => {
      // We always get an array of LerntypBO.fromJSON, but only need one object
      let responseLerntypBO = LerntypBO.fromJSON(responseJSON)[0];
       //console.info(responseLerntyBO);
      return new Promise(function (resolve) {
        resolve(responseLerntypBO);
      })
    })
  }

    //Profil nach Lernvorlieben auslesen
    getProfileByLernvorlieben(lernvorlieben_Id) {
    return this.#fetchAdvanced(this.#getProfileByLernvorliebenURL(lernvorlieben_Id)).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON, but only need one object
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
       //console.info(responseLernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
    //Profil überarbeiten
  updateProfile(profilNBO) {
    return this.#fetchAdvanced(this.#updateProfileURL(profilNBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(profilNBO)
    }).then((responseJSON) => {
      // We always get an array of ProfilNBO.fromJSON
      let responseProfilNBO = ProfilNBO.fromJSON(responseJSON)[0];
      // console.info(profilNBO);
      return new Promise(function (resolve) {
        resolve(responseProfilNBO);
      })
    })
  }
    //Profil nach Studenten auslesen
  getProfileByStudentenId(studenten_Id) {
    return this.#fetchAdvanced(this.#getProfileByStudentenURL(studenten_Id)).then((responseJSON) => {
      // We always get an array of ProfilNBO.fromJSON, but only need one object
      let responseProfilNBO = ProfilNBO.fromJSON(responseJSON)[0];
       //console.info(responseProfilNBO);
      return new Promise(function (resolve) {
        resolve(responseProfilNBO);
      })
    })
  }
    //Gruppen-Methoden

    //Gruppen anzeigen
    getGruppen() {
    return this.#fetchAdvanced(this.#getGruppenURL()).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen löschen
     deleteGruppen(gruppen_Id) {
    return this.#fetchAdvanced(this.#deleteGruppenURL(gruppen_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
      // console.info(gruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen nach Id auslesen
  getGruppenById(gruppen_Id) {
    return this.#fetchAdvanced(this.#getGruppenByIdURL(gruppen_Id)).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen nach Teilnehmer auslesen
    getGruppenByTeilnahmen(teilnahmen_Id) {
    return this.#fetchAdvanced(this.#getGruppenByTeilnahmenURL(teilnahmen_Id)).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen nach Namen auslesen
    getGruppenByNamen(namen_Id) {
    return this.#fetchAdvanced(this.#getGruppenByNamenURL(namen_Id)).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen nach Lernvorlieben auslesen
getGruppenByLernvorlieben(lernvorlieben_Id) {
    return this.#fetchAdvanced(this.#getGruppenByLernvorliebenURL(lernvorlieben_Id)).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

    //Gruppen nach Lerntyp auslesen
    getGruppenByLerntypen(lerntypen_Id) {
    return this.#fetchAdvanced(this.#getGruppenByLerntypenURL(lerntypen_Id)).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
       //console.info(responseGruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }
    //Gruppen hinzufügen
    addGruppen(gruppeNBO) {
    return this.#fetchAdvanced(this.#addGruppenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(gruppenNBO)
    }).then((responseJSON) => {
      // We always get an array of GruppenNBO.fromJSON, but only need one object
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
      // console.info(gruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }
    //Gruppen überarbeiten
    updateGruppen(gruppeNBO) {
    return this.#fetchAdvanced(this.#updateGruppenURL(gruppeNBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(gruppeNBO)
    }).then((responseJSON) => {
      // We always get an array of GruppeNBO.fromJSON
      let responseGruppeNBO = GruppeNBO.fromJSON(responseJSON)[0];
      // console.info(gruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }
    //Gruppen löschen
  deleteGruppen(gruppen_Id) {
    return this.#fetchAdvanced(this.#deleteGruppenURL(gruppen_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of GruppenNBO.fromJSON
      let responseGruppeNBO = GruppeBO.fromJSON(responseJSON)[0];
      // console.info(gruppeNBO);
      return new Promise(function (resolve) {
        resolve(responseGruppeNBO);
      })
    })
  }

//Lerntyp-Methoden

    //Lerntyp ausgeben
  getLerntypen() {
    return this.#fetchAdvanced(this.#getLerntypenURL()).then((responseJSON) => {
      let lerntypBO = LerntypBO.fromJSON(responseJSON);
      //console.info(lerntypBO);
      return new Promise(function (resolve) {
        resolve(lerntypBO);
      })
    })
  }

    //Lerntyp nach ID ausgeben
  getLerntypenById(lerntyp_Id) {
    return this.#fetchAdvanced(this.#getLerntypenByIdURL(lerntyp_Id)).then((responseJSON) => {
      // We always get an array of LerntypBO.fromJSON, but only need one object
      let responseLerntypBO = LerntypBO.fromJSON(responseJSON)[0];
      // console.info(responseLerntypBO);
      return new Promise(function (resolve) {
        resolve(responseLerntypBO);
      })
    })
  }

    //Lerntyp hinzufügen
  addLerntypen(lerntypBO) {
    return this.#fetchAdvanced(this.#addLerntypenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(lerntypBO)
    }).then((responseJSON) => {
      // We always get an array of LerntypBO.fromJSON, but only need one object
      let responseLerntypBO = LerntypBO.fromJSON(responseJSON)[0];
      // console.info(lerntypBO);
      return new Promise(function (resolve) {
        resolve(responseLerntypBO);
      })
    })
  }
    //Lerntyp überarbeiten
  updateLerntypen(lerntypBO) {
    return this.#fetchAdvanced(this.#updateLerntypenURL(lerntypBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(lerntypBO)
    }).then((responseJSON) => {
      // We always get an array of lerntypBO.fromJSON
      let responseLerntypBO = LerntypBO.fromJSON(responseJSON)[0];
      // console.info(lerntypBO);
      return new Promise(function (resolve) {
        resolve(responseLerntypBO);
      })
    })
  }
    //Lerntyp löschen
  deleteLerntypen(lerntyp_Id) {
    return this.#fetchAdvanced(this.#deleteLerntypenURL(lerntyp_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of LerntypBO.fromJSON
      let responseLerntypBO = LerntypBO.fromJSON(responseJSON)[0];
      // console.info(lerntypBO);
      return new Promise(function (resolve) {
        resolve(responseLerntypBO);
      })
    })
  }
//Lernvorlieben-Methoden

    //Lernvorlieben auslesen
  getLernvorlieben() {
    return this.#fetchAdvanced(this.#getLernvorliebenURL()).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON, but only need one object
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
       //console.info(responseLernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
    //Lernvorlieben nach ID auslesen
    getLernvorliebenById(lernvorlieben_Id) {
    return this.#fetchAdvanced(this.#getLernvorliebenByIdURL(lernvorlieben_Id)).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON, but only need one object
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
       //console.info(responseLernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
    //Lernvorlieben hinzufügen
    addLernvorlieben(lernvorliebenBO) {
    return this.#fetchAdvanced(this.#addLernvorliebenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(lernvorliebenBO)
    }).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON, but only need one object
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
      // console.info(lernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
    //Lernvorlieben überarbeiten
  updateLernvorlieben(lernvorliebenBO) {
    return this.#fetchAdvanced(this.#updateLernvorliebenURL(lernvorliebenBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(lernvorliebenBO)
    }).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
      // console.info(lernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
  //Lernvorlieben löschen
  deleteLernvorlieben(lernvorlieben_Id) {
    return this.#fetchAdvanced(this.#deleteLernvorliebenURL(lernvorlieben_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of LernvorliebenBO.fromJSON
      let responseLernvorliebenBO = LernvorliebenBO.fromJSON(responseJSON)[0];
      // console.info(lernvorliebenBO);
      return new Promise(function (resolve) {
        resolve(responseLernvorliebenBO);
      })
    })
  }
//Nachricht-Methoden

    //Nachrichten auslesen
  getNachrichten() {
    return this.#fetchAdvanced(this.#getNachrichtenURL()).then((responseJSON) => {
      // We always get an array of NachrichtBO.fromJSON, but only need one object
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
       //console.info(responseNachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
    //Nachricht auslesen nach Profil
  getNachrichtenByProfile(profile_id) {
    return this.#fetchAdvanced(this.#getNachrichtenByProfileURL(profile_Id)).then((responseJSON) => {
      // We always get an array of NachrichtBO.fromJSON, but only need one object
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
       //console.info(responseNachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
    //Nachrichten auslesen nach Inhalt
    getNachrichtenByInhalt(inhalt_Id) {
    return this.#fetchAdvanced(this.#getNachrichtenByInhaltURL(inhalt_Id)).then((responseJSON) => {
      // We always get an array of NachrichtBO.fromJSON, but only need one object
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
       //console.info(responseNachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
    //Nachrichten hinzufügen
  addNachrichten(nachrichtBO) {
    return this.#fetchAdvanced(this.#addNachrichtenURL(), {
      method: 'POST',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(nachrichtBO)
    }).then((responseJSON) => {
      // We always get an array of NachrichtBO.fromJSON, but only need one object
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
      // console.info(nachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
    //Nachrichten überarbeiten
  updateNachrichten(nachrichtBO) {
    return this.#fetchAdvanced(this.#updateNachrichtenURL(nachrichtBO.getID()), {
      method: 'PUT',
      headers: {
        'Accept': 'application/json, text/plain',
        'Content-type': 'application/json',
      },
      body: JSON.stringify(nachrichtBO)
    }).then((responseJSON) => {
      // We always get an array of CustomerBOs.fromJSON
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
      // console.info(nachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
    //Nachrichten löschen
  deleteNachrichten(nachricht_Id) {
    return this.#fetchAdvanced(this.#deleteNachrichtenURL(nachricht_Id), {
      method: 'DELETE'
    }).then((responseJSON) => {
      // We always get an array of NachrichtBO.fromJSON
      let responseNachrichtBO = NachrichtBO.fromJSON(responseJSON)[0];
      // console.info(nachrichtBO);
      return new Promise(function (resolve) {
        resolve(responseNachrichtBO);
      })
    })
  }
	/*
	Singleton/Einzelstuck instanz erhalten
	*/
	static getAPI() {
		if (this.#api == null) {
			this.#api = new LernGruppenToolAPI();
		} 
		return this.#api;
	}

	/*
	Gibt einen Error zuruck auf JSON Basis. fetch() gibt keine Errors wie 404 oder 500 zuruck. Deshaltb die func fetchAdvanced 
	*/
	#fetchAdvanced = (url, init) => fetch(url, init, {credentials: 'include'})
		.then(res => {
			//fetch() gibt keine Errors wie 404 oder 500 zuruck
			if (!res.ok) {
				throw Error(`${res.status} ${res.statusText}`);
				//throw Error(`Fail`);
			}
			return res.json();
		})

	//Alle Studenten/User bekommen
    //#getUserURL = () => `${this.#LernGruppenToolServerBaseURL}/studenten`;



}