import BusinessObject from "./BusinessObject";

export default class TeilnahmeBO extends BusinessObject {

    constructor(ateilnehmer, agruppen_id,akonversations_id,anachricht_id) {
        super();
        this.teilnehmer = ateilnehmer;
        this.gruppen_id = agruppen_id;
        this.konversations_id = akonversations_id;
        this.nachricht_id = anachricht_id;
    }

    /**
     * Auslesen der Teilnehmer
     */

    getteilnehmer() { 
        return this.teilnehmer
    }

    /**
     * Setzen der Teilnehmer
     */

    setteilnehmer(ateilnehmer){
        this.teilnehmer = ateilnehmer;
    }

    /**
     * Auslesen der Gruppen Id
     */

    getgruppen_id(){
        return this.gruppen_id
    }

    /**
     * Setzen der Gruppen Id
     */

    setgruppen_id(agruppen_id){
        this.gruppen_id = agruppen_id
    }

    /**
     * Auslesen der Konversations Id 
     */

    getkonversations_id(){
        return this.konversations_id
    }

    /**
     * Setzen der Konversations Id 
     */

    setkonversations_id(akonversations_id) {
        this.konversations_id = akonversations_id
    }

    /**
     * Auslesen der Nachrich Id 
    */

    getnachricht_id(){
        return this.nachricht_id
    }

    /**
     * Setzen der Nachricht id 
     */

    setnachricht_id(anachricht_id){
        this.nachricht_id = anachricht_id;
    }

    /**
     * 
     */

    static fromJSON(teilnahmen){
        let result = [];
        if (Array.isArray(teilnahmen)) {
            
            teilnahmen.forEach((c) => {
                Object.setPrototypeOf(c, TeilnahmeBO.prototype);
                result.push(c);
            })
        } else {
            let c = teilnahmen;
            Object.setPrototypeOf(c, TeilnahmeBO.prototype);
            result.push(c);
        }
        return result;
    }



}