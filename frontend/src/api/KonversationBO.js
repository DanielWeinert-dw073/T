import BusinessObject from "./BusinessObject";

export default class KonversationBO extends BusinessObject {

    constructor(anachricht_id,ateilnehmer,aherkunfts_id,aziel_id,aninhalt){
        super();
        this.nachricht_id = anachricht_id;
        this.teilnehmer = ateilnehmer;
        this.ziel_id = aziel_id;
        this.herkunfts_id = aherkunfts_id;
        this.inhalt = aninhalt;

     
    }

    /**
     * Auslesen der nachrichts Id
     */

    getnachricht_id(){
        return this.nachricht_id;
    }

    /**
     * Setzen der Nachrichts Id 
    */

    setnachricht_id(anachricht_id){
        this.nachricht_id = anachricht_id;
    }

    /**
     * Auslesen der Teilnehmer
     */

    getteilnehmer(){
        return this.teilnehmer;
    }

    /**
     * Setzen der Teilnehmer
    */

    setteilnehmer(ateilnehmer){
        this.teilnehmer = ateilnehmer;
    }

    /**
     * Auslesen der Ziel Id 
     */

    getziel_id(){
        return this.ziel_id;
    }

    /**
     * Setzen der  Ziel Id
    */

    setziel_id(aziel_id){
        this.ziel_id = aziel_id;
    }

    /**
     * Auslesen der Herkunfts Id 
     */

    getherkunfts_id(){
        return this.herkunfts_id;
    }

    /**
     * Setzen der Herkunfts Id 
    */

    setherkunfts_id(aherkunfts_id){
        this.herkunfts_id = aherkunfts_id;
    }

    /**
     * Auslesen des Inhaltes
     */

    getinhalt(){
        return this.inhalt;
    }


    /**
     * Setzen des Inhaltes
    */

    setinhalt(ainhalt){
        this.inhalt = ainhalt;
    }

    /** 
     * Ausgeben eines Array von einer KonversationBO aus einer JSONstruktur
    */

    static fromJSON(konversationen) {
        let results = null;
        if (Array.isArray(konversationen)) {
            results = [];
            konversationen.forEach((c) => {
                Object.setPrototypeOf(c,KonversationBO.prototype);
                results.push(c);
            })
        } else {
            let c = konversationen;
            Object.setPrototypeOf(c,KonversationBO.prototype);
            results = c;

        }
        return results;
    }

}