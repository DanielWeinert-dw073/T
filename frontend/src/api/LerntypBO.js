import BusinessObject from "./BusinessObject";

export default class LerntypBO extends BusinessObject {

    constructor(alerntyp){
        super();
        this.lerntyp =alerntyp;
    }

    /**
     * Auslesen des Lerntyps
     */

    getlerntyp(){
        return this.lerntyp;
    }

    /**
     * Setzen des Lerntyps
     */

    setlerntyp(alerntyp){
        this.lerntyp = alerntyp;
    }

    /**
     * Returns an Array of LerntypBO from a given JSON structur
     */

    static fromJSON(lerntypen) {
        let results = null;
        if (Array.isArray(lerntypen)) {
            results = [];
            lerntypen.forEach((c) => {
                Object.setPrototypeOf(c,LerntypBO.prototype);
                results.push(c);
            })
        } else {
            let c = lerntypen;
            Object.setPrototypeOf(c,LerntypBO.prototype); 
            results = c; 
        }
        return results;
    }

}
