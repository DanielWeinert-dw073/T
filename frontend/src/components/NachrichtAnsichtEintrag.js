import React from 'react';
import { withStyles, Typography, Grid } from '@material-ui/core';
import { Button } from '@material-ui/core';
import NachrichtSendenEmpfangenDialog from "./dialogs/NachrichtSendenEmpfangenDialog";
import NachrichtLoeschenDialog from "./dialogs/NachrichtLoeschenDialog";


class NachrichtAnsichtEintrag extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            NachrichtBOs: props.nachricht,
            openDialogInfo: false,
            showDialog: false
        };

    }

    handleClick = () => {
        this.setState({
            showDialog: true
        });
    }

    closeDialog = () => {
        this.setState({
            showDialog: false
        });
    }

    openDialogInfo = () => {
        this.setState({
            openDialogInfo: true
        })
    }

    closeDialogInfo = () => {
        this.setState({
            openDialogInfo: false
        })

    };

    render() {
        const { classes} = this.props;
        const { NachrichtBOs, showDialog, openDialogInfo} = this.state;
        return (
            <div className={classes.root}>
                <Grid container spacing={1} justify= "space-between" alignItems = "center">
                    <React.Fragment>
                        <NachrichtSendenEmpfangenDialog
                            openInfo={openDialogInfo}
                            onCloseProp={this.closeDialogInfo}
                            nachricht={NachrichtBOs}
                        />
                    </React.Fragment>
                    <Grid style={{marginBottom: 10, marginTop: 10}}>
                        <Typography className={classes.heading}>
                            <b>{ NachrichtBOs.getId() }</b>

                        </Typography>
                        <Typography>
                            Inhalt: { NachrichtBOs.getInhalt()} Inhalt des Empfängers
                        </Typography>


                    </Grid>
                    <Grid>
                        <React.Fragment>
                            <NachrichtLoeschenDialog
                            show = {showDialog}
                            close = {this.closeDialog}
                            nachricht= {NachrichtBOs} 
                            />
                        </React.Fragment>
                    </Grid>

                </Grid>
            </div>

        )
    }
}

export default NachrichtAnsichtEintrag; 