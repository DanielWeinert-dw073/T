import BusinessObject from "./BusinessObject";

export default class NachrichtBO extends BusinessObject {

    constructor(ainhalt){
        super();
        this.inhalt = ainhalt
    }
    
    /**
    * erhalte Inhalte
    */
    getinhalt(){
        return this.inhalt;
    }

    /**setzen des Inhaltes */

    setinhalt(ainhalt){
        this.inhalt = ainhalt;
    }

    /**Returns an Array of NachrichtBO from a given JSON structure */

    static fromJSON(nachrichten){
        let results = null;
        if (Array.isArray(nachrichten)){
            results = [];
            nachrichten.forEach((c) => {
                Object.setPrototypeOf(c, NachrichtBO.prototype);
                results.push(c);
            })

        } else {
                
            let c = nachrichten;
            Object.setPrototypeOf(c, NachrichtBO.prototype);
            results = c;
        }
        return results;
    }

}

