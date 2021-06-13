import BusinessObject from "./BusinessObject";

export default class EmpfehlungBO extends BusinessObject {

    constructor(aempfehlung, aempfehlungListe, aempfehlungGruppe, aempfehlungProfil){
        super();
        this.empfehlung = aempfehlung;
        this.empfehlungListe = aempfehlungListe;
        this.empfehlungGruppe = aempfehlungGruppe;
        this.empfehlungProfil = aempfehlungProfil;
    }

	/*
	erhalte Empfehlung
	*/

    getempfehlung(){
        return this.empfehlung;
    }

	/*
	Setzen einer Empfehlung
	*/

    set_empfehlung(aempfehlung){
        this.empfehlung = aempfehlung;
    }

	/*
	erhalte Empfehlungsliste
	*/

    getempfehlung_Liste(){
        return this.empfehlungListe;
    }

	/*
	Setzen einer Empfehlungsliste
	*/

    set_empfehlung_Liste(aempfehlungListe){
        this.empfehlungListe = aempfehlungListe;
    }

	/*
	erhalte  Gruppenempfehlung
	*/

    getempfehlung_Gruppe(){
        return this.empfehlungGruppe;
    }

	/*
	Setzen einer Gruppenempfehlung
	*/

    set_empfehlung_Gruppe(aempfehlungGruppe){
        this.empfehlungGruppe = aempfehlungGruppe
    }

	/*
	erhalte Profilempfehlung
	*/

    getempfehlung_Profil(){
        return this.empfehlungProfil;
    }

	/*
	Setzen einer Profilempfehlung
	*/

    set_empfehlung_Profil(aempfehlungProfil){
        return this.empfehlungProfil = aempfehlungProfil
    }


    /**
     * Return Array von Empfehlungen (Objekte) aus einem JSON 
    */

    static fromJSON(empfehlungen) {
        let results = null;
        if (Array.isArray(empfehlungen)) {
            results = [];
            empfehlungen.forEach((c) => {
                Object.setPrototypeOf(c, EmpfehlungBO.prototype);
                results.push(c);
            })
             
        } else {
            let c = empfehlungen;
            Object.setPrototypeOf(c,EmpfehlungBO.prototype);
            results = c;
        }
        return results;
    }
}