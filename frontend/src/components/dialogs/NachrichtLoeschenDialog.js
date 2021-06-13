import React from 'react';
import { Button, Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle } from '@material-ui/core';

class NachrichtLoeschenDialog extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            deletingInProgress: false,
            deletingError: null,
            NachrichtenBOs: props.nachricht

        };
    }

    handleClose = () => {
        this.props.close();
    }

    deleteAlert = () => {
        alert("Löschen erfolgreich");
        this.handleClose()
    }

    render() {
        const { classes, show} = this.props;
        const {deletingError, NachrichtenBOs} = this.state;
        return (
            <Dialog open={show} onClose = {this.handleClose}>
                <DialogTitle id= "alert-dialog-title">
                    Bestätigungsmeldung
                </DialogTitle>
                <DialogContent>
                    <DialogContenttext id="alert-dialog-description">
                        Sind Sie sicher, dass sie die Nachricht "{NachrichtBOs.getId()}",
                        "{NachrichtBOs.getInhalt()}" wirklich löschen möchten?
                    </DialogContenttext>
                </DialogContent>
                <DialogActions>
                    <Button onClick={this.deleteAlert} color ='primary'>
                        Löschen
                    </Button>
                    <Button onClick={this.handleClose} color="secondary">
                        Abbrechen
                    </Button>
                </DialogActions>
            </Dialog>
        );
    }
}




export default NachrichtLoeschenDialog; 