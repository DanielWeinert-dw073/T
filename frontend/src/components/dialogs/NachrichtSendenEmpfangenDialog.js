import React, { Component} from 'react';
import { withStyles, Button, Grid } from '@material-ui/core';
import Dialog from '@material-ui/core/Dialog';
import {default as DialogContent, default as DialogContentText} from '@material-ui/core/DialogContent';
import DialogTitle from '@material-ui/core/DialogTitle';
import TextField from '@material-ui/core/TextField';

class NachrichtSendenEmpfangenDialog extends React.Component {
    constructor(props) {
        super(props);
        this.state = {

        }
    }


    onDialogClose =()=>{
        this.props.onCloseProp()
    }

    render() {
        const {} = this.props;
        return(
            <Dialog open={} aria-labelledby="form-dialog-title">
                <DialogTitle id="form-dialog-title">Möchtest du eine Nachricht schreben oder empfangen?</DialogTitle>
            <DialogContent>
                <DialogContentText>
                Nachricht:
                </DialogContentText>
                <TextField  align="center" id="standard-number" type="number" InputLabelProps={{ shrink: true,}}></TextField>
                <Grid justify='space-between' alignItems='center'>
                    <Button style={{marginBottom: 10, marginTop: 10, color: 'white', backgroundColor: '#4caf50'}} onClick={this.onDialogClose} >Senden</Button> 
                    <Button style={{marginBottom: 10, marginTop: 10, color: 'white', backgroundColor: '#ff5722'}} onClick={this.onDialogClose} >Empfangen</Button>   
                    <Button style={{marginBottom: 10, marginTop: 10, color: 'white', backgroundColor: '#ff5722'}} onClick={this.onDialogClose} >Abbrechen</Button>   
                </Grid>     
            </DialogContent>

            </Dialog>
        );
    }

}

export default NachrichtSendenEmpfangenDialog;