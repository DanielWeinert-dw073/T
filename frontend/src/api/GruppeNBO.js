import NamedBusinessObject from "./NamedBusinessObject";

export default class GruppeNBO extends NamedBusinessObject {

    constructor(ananzahl_teilnehmer,ateilnehmer_liste,amax_teilnehmer){
        super();
        this.anzahl_teilnehmer = ananzahl_teilnehmer;
        this.teilnehmer_liste = ateilnehmer_liste;
        this.max_teilnehmer = amax_teilnehmer;
    }

	/*
	auslesen Anzahl an Teilnehmern
	*/

    getanzahl_teilnehmer(){
        return this.anzahl_teilnehmer;
    }

	/*
	Setzen einer Teilnehmeranzahl
	*/

    setanzahl_teilnehmer(ananzahl_teilnehmer){
        this.anzahl_teilnehmer = ananzahl_teilnehmer;
    }

    /**
     * 
     * Ausgeben der TeilnehmerListe
     */

    getteilnehmer_liste(){
        return this.teilnehmer_liste
    }

    /**Setzen 
     * der TeilnehmerListe 
    */

    setteilnehmer_liste(ateilnehmer_liste){
        this.teilnehmer_liste = ateilnehmer_liste
    }

    /**
     *Auslesen der max_teilnehmer
     */

    getmax_teilnehmer(){
        return this.max_teilnehmer
    }

    /**
     * Setzen der max_teilnehmer
     */

    setmax_teilnehmer(amax_teilnehmer){
        this.max_teilnehmer = amax_teilnehmer
    }

    /**Returns Array von Gruppen (Objekte) aus einer JSON Struktur */

    static fromJSON(gruppen) {
        let results = null;
        if (Array.isArray(gruppen)) {
            results = [];
            gruppen.forEach((c) => {
                Object.setPrototypeOf(c,GruppeNBO.prototype);
                results.push(c);
            })
        } else {
            let c = gruppen;
            Object.setPrototypeOf(c,GruppeNBO.prototype);
            results = c;
        }
        return results;
    }
    
}
