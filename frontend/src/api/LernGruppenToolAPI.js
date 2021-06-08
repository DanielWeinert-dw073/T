//import StudentNBO from '../StudentNBO';
//import TeilnahmeBO from '../TeilnahmeBO';
//import EmpfehlungBO from '../EmpfehlungBO';
import ProfilNBO from './ProfilNBO';
import GruppeNBO from './GruppeNBO';
import KonversationBO from './KonversationBO';
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
    #LernGruppenToolBaseURL = "/LerngruppenAdministration";

    //Lokales Python backend
    //#LerngruppenToolBaseURL = "https://lerngruppenapp.oa.r.appspot.com/LernGruppenToolApp";

    //Profil anzeigen
    #getProfileURL = () => `${this.#LernGruppenToolBaseURL}/profile`;
    #getProfileByStudentIdURL = (id) => `${this.#LernGruppenToolBaseURL}/profile/student/${id}`;
    #getProfileByStudentId = (student_id) => `${this.#LernGruppenToolBaseURL}/profile/student/${student_id}`;
    #deleteProfileURL = (student_id) => `${this.#LernGruppenToolBaseURL}/profile/${student_id}`;
    #addProfileURL = () => `${this.#LernGruppenToolBaseURL}/profile`;

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
   }
    //Profil bearbeiten/hinzufügen
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


    //Profil nach Id auslesen

    //Profil nach Lerntyp auslesen

    //Profil nach Lernvorlieben auslesen 


    //Gruppen anzeigen

    //Gruppen löschen

    //Gruppen nach Id auslesen

    //Gruppen nach Teilnehmer auslesen

    //Gruppen nach Namen auslesen 

    //Gruppen nach Lernvorlieben auslesen

    //Gruppen nach Lerntyp auslesen




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

    //gibt die Person mit der bestimmten GoogleUserID als BO zurück
	//getStudentByGoogleID(google_user_id){
		//return this.#fetchAdvanced(this.#getStudentByGoogleIDURL(google_user_id)).then((responseJSON) => {
			//let studentNBO = StudentNBO.fromJSON(responseJSON);
			//console.info(studentNBO)
			//return new Promise(function (resolve){
				//resolve(studentNBO)
			//})
		//})
	//}

	//Alle Studenten/User bekommen
    //#getUserURL = () => `${this.#LernGruppenToolBaseURL}/studenten`;



}