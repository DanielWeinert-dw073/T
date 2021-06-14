import React from 'react'; 
import HighlightOffIcon from '@material-ui/icons/HighlightOff';
import { withRouter } from 'react-router-dom';
import LoadingProgress from './dialogs/LoadingProgress';
import { withStyles, Paper, Button, Typography, Grid, TextField, InputAdornment, IconButton } from '@material-ui/core';
import { AccessAlarm, ThreeDRotation, HighlightOff } from '@material-ui/icons';
import NachrichtAnsichtEintrag from './NachrichtAnsichtEintrag';
import ContextErrorMessage from './dialogs/ContextErrorMessage';
import Theme from './../Theme';
import LernGruppenToolAPI from '../api/LernGruppenToolAPI';
import PropTypes from 'prop-types';


class NachrichtAnsicht extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            nachricht: [],
            filteredNachricht: [],
            nachrichtFilter:"",
            error: null,
            loadingProgress: false
        }
    }

    getAlleNachrichten = () => {
        LernGruppenToolAPI.getAPI().getAlleNachrichten().then(nachrichtBOs => {
            this.setState({
                nachrichten: nachrichtBOs,
                filteredNachricht : [...nachrichtBOs],
                loadingProgress: false,
                error: null,
            });
        }
        ).catch((e) =>
            this.setState({
                nachrichten: [],
                filteredNachricht: [],
                loadingProgress: false,
                error: e,
            })
        );
        this.setState({
            LoadingProgress: true,
            error: null,
        });
    };

    componentDidMount() {
        //this.getAlleNachrichten();
    }


    /**filterNachrichten = event => {
        const searchterm = event.target.value.toLowerCase();
        this.setState({
            filteredNachrichten: this.state.nachrichten.filter(nachricht => {
                let nachrichtInhaltContainsValue = nachricht.getInhalt().toLowerCase().includes(searchterm);
                return nachrichtInhaltContains
            }),
            nachrichtFilter: searchterm,
        });

    }

    clearNachrichtenFilter = () => {
        this.setState({
            filteredNachrichten: [...this.state.nachrichten],
            nachrichtFilter: "",
        })
    }
*/

        render() {
            const { classes} = this.props;
            const { error, LoadingProgress, nachricht, nachrichtFilter, filteredNachricht, filterNachricht} = this.state;
            return (
                <div className={classes.root}>
                <Paper style={{paddingTop: 15, paddingLeft: 15, paddingRight: 15, paddingBottom: 15, marginTop: 15}} elevation={0}>
               
                    <Grid container spacing={1} justify='flex-start' alignItems='center'>
                        <Button style={{width: '100%', paddingBottom: 10, paddingLeft: 10, marginTop: 10}} variant="contained">
                            Meine Chats
                        </Button>
                    </Grid>
                    <Grid>
                        <Typography>
                            Meine Chats durchsuchen
                        </Typography>
                        <TextField
                            autoFocus type = "text"
                            value = {nachrichtFilter}
                            onChange={this.filterNachricht}
                            InputProps = {{
                                endAdornment:
                                    <InputAdornment position="end">
                                        <IconButton onClick={this.clearNachrichtFilter}>
                                            <HighlightOffIcon />

                                        </IconButton>

                                    </InputAdornment>
                            }}

                        />
                    </Grid>
                    <Grid style = {{width: '100%', paddingBottom: 10, paddingLeft: 10, marginTop: 10}}>
                        <Typography>
                            Hier kannst du deine Nachrichten anschauen:
                        </Typography>
                        {
                            nachricht.length > 0 ?
                            filteredNachricht.map(nachricht =>
                                <NachrichtAnsichtEintrag key={nachricht.getId()} nachricht= {nachricht} />)
                                :
                                null
                        }
                    </Grid>
                </Paper>
                </div>
            );

        }
}


const styles = theme => ({
    root: {
        width: '100%',
    }
});

NachrichtAnsicht.propTypes = {
    classes: PropTypes.object.isRequired,
    location: PropTypes.object.isRequired,
};

export default withRouter(withStyles(styles)(NachrichtAnsicht));