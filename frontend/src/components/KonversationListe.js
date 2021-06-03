import React, { useState, useEffect } from "react";

import Nachricht from "NachrichtBO";

import KonversationListeEintrag from "./KonversationListeEintrag";

/**
 * Erstellt eine Liste von KonversationListeEintrag für jede Konversation
 */

class KonversationListe extends React.Component {

    constructor(props) {
        super(props);

        // Initialize an empty state object
        this.state = {
            nachrichtId: [],
            teilnehmer: [],
            herkunfts_id: [],
            ziel_id: [],
            inhalt: [],
        };
    }

    //API Anbindung um alle Konversationen vom Backend zu bekommen

    getKonversation = () => {
        LernGruppenToolAPI.getAPI().getKonversation()
        .then(KonversationBOs =>
            this.setState({
                konversationen:KonversationBOs,
                error: null,
                loadingInProgress: false,
            })).catch(e =>
                this.setState({
                    konversationen: [],
                    error: e,
                    loadingInProgress:false,
                }));
        this.setState({
            error: null,
            loadingInProgress: false,
            
        });        
    }

    // Funktion die einen print Befehl ausführt
    printKonversationliste = () => {
        window.print()
    }

    // Funktion, um bei Fahlern alle Infos zu laden 
    handelReload = () => {
        this.getInhalt();
        this.getHerkunftsId();
        this.getTeilnehmer();
        this.getZielId();
        this.getnachricht_id();
    }

    //Lifecyclemethode, wird aufgerufen wenn die Component in den DOM eingesetzt wird
    componentDidMount() {
        this.getInhalt();
        this.getHerkunftsId();
        this.getTeilnehmer();
        this.getZielId();
        this.getnachricht_id();

    }

    //API Anbindung um Konversationen des Profils vom backend zu bekommen
    getKonversation_by_profil = () => {
        LernGruppenToolAPI.getAPI().getKonversation_by_profil(this.state.konversation,this.state.profil)
        .then(konversationBOs => 
            this.setState({
                konversationen: konversationBOs,
                error = null,
                loadingInProgress: false,
            })).catch(e => 
                this.setState({
                    error: null,
                    loadingInProgress: true
                }));
        this.setState({
            error: null,
            loadingInProgress: true

        });
    }

    // Rendern der Komponente

    render () {

        const { classes } = this.props;
        const { profil_id, inhalt, herkunfts_id, ziel_id, teilnehmer, nachricht_id, loadingInProgress, error} = this.state;
        return 
    }

    
}

export default withRouter(withStyles(styles)(KonversationListe));