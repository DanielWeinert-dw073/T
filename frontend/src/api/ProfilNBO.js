import NamedBusinessObject from "./NamedBusinessObject";

export default class ProfilNBO extends NamedBusinessObject {
    constructor(afaecher,analter,astudiengang,awohnort,asemester,avorwissen,
        alernvorlieben, anabout_me,asprachen){
        super();
        this.faecher = afaecher;
        this.alter = analter;
        this.studiengang = astudiengang;
        this.wohnort = awohnort;
        this.semester = asemester
        this.vorwissen = avorwissen;
        this.lernvorlieben = alernvorlieben
        this.about_me = anabout_me;
        this.sprachen = asprachen;

    }

    /**
     * Auslesen der Fächer
     */

    getfaecher(){
        return this.faecher;
    }

    /**
     * Setzen der Fächer
     */

    setfaecher(afaecher){
        this.faecher = afaecher
    }

    /**
     * Auslesen des Alters
    */

    getalter(){
        return this.alter
    }

    /**
     * Setzen des Alters
     */

    setalter(analter){
        this.alter = analter
    }

    /**
     * Auslesen des studiengangs
    */

    getstudiengang(){
        return this.studiengang
    }

    /**
     * Setzen des Studiengangs
     */

    setstudiengang(astudiengang){
        this.studiengang = astudiengang
    }

    /**
     * Auslesen des Wohnortes
     */

    getwohnort(){
        return this.wohnort
    }

    /**
     * Setzen des Wohnortes
     */

    setwohnort(awohnort){
        this.wohnort = awohnort
    }

    /**
     * Auslesen des semester
    */

    getsemester(){
        return this.semester
    }

    /**
     * Setzen des Semesters
     */

    setsemester(asemester){
        this.semester = asemester
    }

    /**
     * Auslesen des Vorwissen
     */

    getvorwissen(){
        return this.vorwissen
    }

    /**
     * Setzen des Vorwissens 
    */

    setvorwissen(avorwissen){
        this.vorwissen  = avorwissen
    }

    /**
     * Auslesen der Vorlieben 
     */

    getlernvorlieben(){
        return this.lernvorlieben
    }

    /**
     * Setzen der Lernvorlieben
     */

    setlernvorlieben(alernvorlieben){
        this.lernvorlieben = alernvorlieben
    }

    /**
     * Auslesen des About ME 
     */

    getabout_me() {
        return this.about_me
    }

    /**
     * Setzen des About Me 
     */

    setabout_me(anabout_me) {
        this.about_me = anabout_me
    }

    /**
     * Auslesen der Sprache
     */

    getsprachen(){
        return this.sprachen
    }

    /**
     * Setzen der Sprachen
     */

    setspreachen(asprachen){
        this.sprachen = asprachen
    }

    /**
     * Returns an Array of ProfilNBO from a given JSON structur
     */

    static fromJSON(profile) {
        let results = null;
        if (Array.isArray(profile)) {
            results = [];
            profile.forEach((c) => {
                Object.setPrototypeOf(c,ProfilNBO.prototype);
                results.push(c);
            })
        } else {
            let c = profile;
            Object.setPrototypeOf(c,ProfilNBO.prototype);
            results = c;
        }
        return results;

    }
    
}