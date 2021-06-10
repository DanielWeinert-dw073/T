import React from 'react';
import { withStyles, Typography, Grid } from '@material-ui/core';
import LernGruppenToolAPI from '../api/LernGruppenToolAPI';

import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';


import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';




class GruppenListe extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            gruppe: [],
            loadingProgress: false,
            error: null
        };
    }

        getGruppen = () => {
            LernGruppenToolAPI.getAPI().getGruppen()
                .then(gruppeNBOs =>
                    this.setState({
                        gruppe: gruppeNBOs,
                        loadingProgress: false,
                        error: null,

                    })).catch(e =>
                        this.setState({
                            gruppe: [],
                            loadingProgress: false,
                            error:e
                        }));
            this.setState({
                loadingInProgress: true,
                error: null
            });

        } 

    componentDidMount(){
        this.getGruppen();
    }


    render() {
        const {classes} = this.props;
        const { loadingProgress, error, gruppen } = this.state;
        return (
            <div className={classes.root}>
                <Grid justify= "flex-end" container spacing={1} alignItems='space-between'>
                    <Typography>
                        Test Gruppe 
                    </Typography>

                </Grid>

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
GruppenListe.propTypes = {
    /** @ignore */
    classes: PropTypes.object.isRequired,
    /** @ignore */
    location: PropTypes.object.isRequired,
    show: PropTypes.bool.isRequired
}


export default withRouter(withStyles(styles)(GruppenListe));