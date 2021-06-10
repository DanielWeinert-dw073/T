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
    return this.#fetchAdvanced(this.#getStudentenByIDURL(studenten_Id)).then((responseJSON) => {
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

//  Studenten überarbeiten

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
    //Profil anzeigen
    #getProfileURL = () => `${this.#LernGruppenToolServerBaseURL}/profile`;
    #getProfileByStudentIdURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/student/${id}`;
    #getProfileByStudentID = (student_id) => `${this.#LernGruppenToolServerBaseURL}/profile/student/${student_id}`;
    
    //Profil löschen
    #deleteProfileURL = (student_id) => `${this.#LernGruppenToolServerBaseURL}/profile/${student_id}`;

    //Profil nach Id auslesen
    #getProfileByIDURL = (id) => `${this.#LernGruppenToolServerBaseURL}/profile/${id}`;

    //Profil hinzufügen
    #addProfileURL = () => `${this.#LernGruppenToolServerBaseURL}/profile`;

    //Profil nach Lerntyp auslesen
    #getProfileByLerntyp= (lerntyp_id) => `${this.#LernGruppenToolServerBaseURL}/profile/${lerntyp_id}`;

    //Profil nach Lernvorlieben auslesen
    #getProfileByLernvorlieben= (lernvorlieben_id) => `${this.#LernGruppenToolServerBaseURL}/profile/${lernvorlieben_id}`;

    //Gruppen anzeigen
    #getGruppenURL = () => `${this.#LernGruppenToolServerBaseURL}/gruppen`;

    //Gruppen löschen
    #deleteGruppenURL = () => `${this.#LernGruppenToolServerBaseURL}/gruppen`;

    //Gruppen nach Id auslesen
     #getGruppenByIDURL = (id) => `${this.#LernGruppenToolServerBaseURL}/gruppe/${id}`;

    //Gruppen nach Teilnehmer auslesen
    //#selectGruppenURL = (Teilnehmer) => `${this.#LernGruppenToolServerBaseURL}/gruppe/${Teilnehmer}`;

    //Gruppen nach Namen auslesen
    //#selectGruppenURL = (Namen) => `${this.#LernGruppenToolServerBaseURL}/gruppe/${Namen}`;

    //Gruppen nach Lernvorlieben auslesen
    //#selectGruppenURL = (Lernvorlieben) => `${this.#LernGruppenToolServerBaseURL}/gruppe/${Lernvorlieben}`;

    //Gruppen nach Lerntyp auslesen
    //#selectGruppenURL = (Lerntyp) => `${this.#LernGruppenToolServerBaseURL}/gruppe/${Lerntyp}`;




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
	/*
	Gebe alle BO's zuruck
	*/

    // gibt alle Profile als BO zuruck
  getProfile() {
        return this.#fetchAdvanced(this.#getProfileURL(),{method:"GET"}).then((responseJSON)=>{
            let profileNBOs = ProfilNBO.fromJSON(responseJSON);
            console.info(profileNBOs)
            return new Promise(function (resolve){
                resolve(profileNBOs);
            })
        })
    }

  getProfileByStudentId(student_id) {
        return this.#fetchAdvanced(this.#getProfileByStudentIdURL(student_id),{method: "GET"}).then((responseJSON) =>{
            let profileNBOs = ProfilNBO.fromJSON(responseJSON);
            return new Promise (function (resolve){
                resolve(profileNBOs)
            })
        } )
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

    //Delete Profile
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

     //Gruppen auslesne
  getGruppen() {
    return this.#fetchAdvanced(this.#getGruppenURL(),{method:"GET"}).then((responseJSON)=>{
          let GruppeNBOs = GruppeNBO.fromJSON(responseJSON);
          console.info(gruppenNBOs)
          return new Promise(function (resolve){
              resolve(gruppenNBOs);
          })
      })
  }

  
   


	//Alle Studenten/User bekommen
    //#getUserURL = () => `${this.#LernGruppenToolServerBaseURL}/studenten`;



}