import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import firebase from 'firebase/app';
import 'firebase/auth';
import { withStyles, Button, Grid } from '@material-ui/core';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import ProfilUebersichtEintrag from './ProfilUebersichtEintrag'
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';
import LernGruppenToolAPI from '../api/LernGruppenToolAPI';








//Css Style für Tabellen Zellen
const StyledTableCell = withStyles((theme) => ({
    head: {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.common.white,
    },
    body: {
      fontSize: 14,
    },
  }))(TableCell);


//Css Style für Tabllen Zeilen
const StyledTableRow = withStyles((theme) => ({
    root: {
      '&:nth-of-type(4n+1)': {
        backgroundColor: theme.palette.action.hover,
      },
    },
  }))(TableRow);


class ProfilUebersicht extends React.Component {
    constructor(props) {
        super(props);
      
    

        this.state = {

            faecher: null,
            alter: null,
            studiengang: null,
            wohnort: null,
            semester: null,
            vorwissen: null,
            lernvorlieben: null,
            about_me: null,
            sprachen: null,
            error: null,
            loadingInProgress: false,
        };
    }

    getAllProfils = () => {
        LernGruppenToolAPI.getAPI().getProfils(this.props.currentProfil.uid)
        .then(profilNBOs =>
            this.setState({
                profile: profilNBOs,
                error:null,
                loadingInProgress: false,
            })).catch(e =>
                this.setState({
                    profile: [],
                    error: e,
                    loadingProgress: false,
                }));
        this.setState({
            error: null,
            loadingProgress: true,
            loadingProfileError: null
        });
    }

    componentDidMount() {
        //this.getAllProfils()
        
        }
    

    render() {

        const { classes} = this.props;
        const {profil, currentStudentId, currentStudentName, error, loadingProgress} = this.state;

        return(
            <div className={classes.root}>
                <Grid container  justify="flex-end" alignItems="center" spacing={2}>
                    <Grid item xs/>
                    <Grid item>
                    <Button variant="outlined" color="primary" >
                        

                    </Button>
                    </Grid>
                </Grid>
                <TableContainer component={Paper}>
                    <Table className = {classes.table} aria-label= "customized table">
                        <TableHead>
                            <StyledTableRow>
                        
                                <StyledTableCell>Profil</StyledTableCell>
                                <StyledTableCell align="center">Faecher</StyledTableCell>
                                <StyledTableCell align= "center">Alter</StyledTableCell>
                                <StyledTableCell align= "center">Studiengang</StyledTableCell>
                                <StyledTableCell align= "center">Wohnort</StyledTableCell>
                                <StyledTableCell align= "center">Semester</StyledTableCell>
                                <StyledTableCell align= "center">Vorwissen</StyledTableCell>
                                <StyledTableCell align= "center">Lernvorlieben</StyledTableCell>
                                <StyledTableCell align= "center">About Me</StyledTableCell>
                                <StyledTableCell align= "center">Sprachen</StyledTableCell>
                            </StyledTableRow>
                        </TableHead>
                        <TableBody>
                            {
                                profil ?
                                <>
                                {
                                    profil.map(profil =>
                                        <ProfilUebersichtEintrag key={profil.getId()} profil = {profil}
                                        getProfil = {this.getProfil}
                                        show={this.props.show} 
                                    />)
                                }
                                </>
                                : 
                                <></>
                            }
                        </TableBody>

                    </Table>
                    <LoadingProgress show = {loadingProgress} />
                    <ContextErrorMessage error={error} contextErrorMsg = {"Dein Profil konnte nicht geladen werden"} onReload = {this.getProfile} />
                </TableContainer>
                <Button variant = "contained" color = 'primary' size = "medium" className={classes.Button}>
                    Profil
                
                </Button> 

            </div>
        )
    }

}

/** Component specific styles */
const styles = theme => ({
        root: {
            width: '100%',
            marginTop: theme.spacing(2),
            marginBottom: theme.spacing(2),
        },
        content: {
            margin: theme.spacing(1),
        },
        table: {
            minWidth: 700,
        },
        header:{
            marginBottom: theme.spacing(1),
            paddingLeft: theme.spacing(1),
            paddingRight: theme.spacing(1),
        },
        button:{
            marginTop: theme.spacing(2),
            marginBottom: theme.spacing(3),
            float: 'right'
        }
    });

/** PropTypes */
ProfilUebersicht.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
    show: PropTypes.bool.isRequired
}


export default withRouter(withStyles(styles)(ProfilUebersicht));
