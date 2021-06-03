import NamedBusinessObject from "./NamedBusinessObject";

export default class ProfilNBO extends NamedBusinessObject {
    constructor(anemail, agoogle_user_id) {
        this.email = anemail;
        this.google_user_id = agoogle_user_id;
    }

    /**
     * Auslesen der Email
     */

    getemail() {
        return this.email;
    }

    /**
     * Setzen der Email
     */

    setemail(anemail) {
        this.email = anemail;
    }

    /**
     * Auslesen der Google User Id 
     */

    getgoogle_user_id() {
        return this.google_user_id;
    }

    /**
     * Setzen Google User Id 
     */

    setgoogle_user_id(agoogle_user_id) {
        this.google_user_id =agoogle_user_id
    }

    /**
     * Returns an Array of StudentNBO from a given JSON structur
     */

    static fromJSON(studenten) {
        let results = null;
        if (Array.isArray(studenten)) {
            results = [];
            studenten.forEach((c) => {
                Object.setPrototypeOf(c,StudentNBO.prototype);
                results.push(c);
            })
        } else {
            let c = studenten;
            Object.setPrototypeOf(c,StudentNBO.prototype);
            results = c;
        }
        return results;

    }

}