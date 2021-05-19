import BusinessObject from "./BusinessObject";

export default class LernvorliebenBO extends BusinessObject {

    constructor(afrequenz,ainternet_verbindung, apole_der_persönlichkeit){
        super();
        this.frequenz = afrequenz;
        this.internet_verbindung = ainternet_verbindung;
        this.pole_der_persönlichkeit = apole_der_persönlichkeit;
    }

    /**
     * Auslesen der frequenz
     */

    getfrequenz(){
        return this.frequenz;
    }
    
    /**
     * Setzen der Frequenz
    */

    setfrequenz(afrequenz){
        this.frequenz = afrequenz;
    }

    /** 
     * Auslesen der InternetVerbindung
    */

    getinternet_verbindung(){
        return this.internet_verbindung
    }

    /**
     * Setzen der InternetVerbindung
     */
    
    setinternet_verbindung(ainternet_verbindung){
        this.internet_verbindung = ainternet_verbindung;

    }

    /**
     * Auslesen der Pole pole_der_persönlichkeit
     */

    getpole_der_persönlichkeit(){
        return this.pole_der_persönlichkeit
    }

    /**
     * Setzen pole_der_persönlichkeit
     */

    set_pole_der_persönlichkeit(apole_der_persönlichkeit){
        this.pole_der_persönlichkeit = apole_der_persönlichkeit;
    }

    /**
     * Returns an Array of LernvorliebenBO from a given JSON structur
     */

    static fromJSON(lernvorlieben) {
        let results = null;
        if (Array.isArray(lernvorlieben)) {
            results = [];
            lerntypen.forEach((c) => {
                Object.setPrototypeOf(c,LernvorliebenBO.prototype);
                results.push(c);
            })
        } else {
            let c = lernvorlieben;
            Object.setPrototypeOf(c,LernvorliebenBO.prototype);
            results = c;
        }
        return results;
    }

}
