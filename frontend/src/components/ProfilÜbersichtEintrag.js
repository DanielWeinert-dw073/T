import React, { Component } from 'react';
import PropTypes from 'prop-types';
import LernGruppenToolAPI from '../api/LernGruppenToolAPI';
import { withStyles } from '@material-ui/core/styles';
import LoadingProgress from './dialogs/LoadingProgress';
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableRow from '@material-ui/core/TableRow';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import { withRouter } from 'react-router-dom';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';





//Css Style Klassen für die Tabellen Zellen
const StyledTableCell = withStyles((theme) => ({
    head: {
      backgroundColor: theme.palette.primary.main,
      color: theme.palette.common.white,
    },
    body: {
      fontSize: 14,
    },
}))(TableCell);
  
  //Css Style Klassen für die Tabellen Zeilen
  const StyledTableRow = withStyles((theme) => ({
    root: {
      '&:nth-of-type(4n+1)': {
        backgroundColor: theme.palette.action.hover,
      },
    },
  }))(TableRow);
  
class ProfilÜbersichtEintrag extends React.Component {
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
            loadingIndicator: false
        };
    }

    getProfil = () => {
        LernGruppenToolAPI.getAPI().getProfil(this.props.profil)
        .then(profilNBO => 
            this.setState({
                profile: profilNBO,
                profilid: profilNBO.id,
                profilName:profilNBO.name,
                loadingInProgress:false,
                error: null,
            })).then(() => {
                this.getStudent()
                this.getLernvorlieben()
                this.getLerntyp()
            })
            .catch(e => 
                this.setState({
                    profil: null,
                    profilId: null,
                    profilName: null,
                    loadingInProgress:false,
                    error: e,
                }));
        this.setState({
            loadingInProgress:true,
            error:null
        });
    }

    getlerntyp_by_profil_id = () => {
        LernGruppenToolAPI.getAPI().getlerntyp_by_profil_id(this.state.profil.getlerntyp())
        .then(lerntypBOs => 
            this.setState({
                lerntypen: lerntypBOs.lerntyp,
                error: null,
                loadingInProgress:false,
            }))
            .catch(e =>
                this.setState({
                    lerntypen: null,
                    error: e,
                    loadingInProgress:false,
                }));
        this.setState({
            error: null,
            loadingInProgress:true
        });    

    }

    getlernvorlieben_by_profil_id = () => {
        LernGruppenToolAPI.getAPI().getlernvorlieben_by_profil_id(this.state.lernvorlieben)
        .then(lernvorliebenBOs =>
            this.setState({
                lernvorlieben: lernvorliebenBOs,
                error: null,
                loadingInProgress:false,
            }))
            .catch(e =>
                this.setState({
                    lernvorlieben: null,
                    error:e,
                    loadingInProgress:false,
                }));
        this.setState({
            error: null,
            loadingInProgress:true
        });
    }


    componentDidMount() {
        this.getProfil();
    }

    componentDidUpdate(prevProps) {
        if((this.props.show) &&(this.props.show !== prevProps.show)) {
            this.getProfil();
        }
    }

    render() {

        const { classes, student, profil } = this.props;
        const { profilId,faecher, profilName,lernvorlieben,alter,wohnort,vorwissen,
                    about_me, lerntyp, loadingInProgress, error,sprachen
                    } = this.state;

        return (
            <>
                <StyledTableRow key={profilId}>
                  <StyledTableCell align="left">{profilName}</StyledTableCell>
                  <StyledTableCell align="center">{faecher}</StyledTableCell>
                  <StyledTableCell align="center">{lerntyp}</StyledTableCell>
                  <StyledTableCell align="center">{lernvorlieben}</StyledTableCell> 
                  <StyledTableCell align="center">{alter}</StyledTableCell> 
                  <StyledTableCell align="center">{wohnort}</StyledTableCell>
                  <StyledTableCell align="center">{vorwissen}</StyledTableCell>
                  <StyledTableCell align="center">{sprachen}</StyledTableCell>
                  <StyledTableCell align="center">{about_me}</StyledTableCell>     
                  <StyledTableCell align="right" className={classes.breite}>               

                  </StyledTableCell>
                  </StyledTableRow>
                  <StyledTableRow> 
                    <StyledTableCell colspan="10" className={classes.laden}>
                      <LoadingProgress show={loadingInProgress}></LoadingProgress>
                      <ContextErrorMessage error={error} contextErrorMsg = {'Dieses Profil konnte nicht geladen werden'} onReload={this.getProfileByStudentId} />
                    </StyledTableCell>
                  </StyledTableRow>
          </>  

        );
    }

}
/** Component specific styles */
const styles = theme => ({
    root: {
        width: '100%',
        marginTop: theme.spacing(2),
        marginBottom: theme.spacing(2),
        padding: theme.spacing(1),
    },
    content: {
        margin: theme.spacing(1),
      },
    table: {
        minWidth: 700,
      },
    formControl: {
        margin: theme.spacing(1),
        minWidth: 200,
        textAlign: "left"
    },
    button: {
        margin: theme.spacing(1),
        },
    laden: {
      padding: 0
    },
    breite: {
      width: 220
    }
    });

/** PropTypes */
ProfilÜbersichtEintrag.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    profil: PropTypes.object.isRequired,
    show: PropTypes.bool.isRequired
  }
  
export default withStyles(styles)(ProfilÜbersichtEintrag);