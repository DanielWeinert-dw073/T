import React, {Component} from 'react';

import ContextErrorMessage from './dialogs/ContextErrorMessage';
import LoadingProgress from './dialogs/LoadingProgress';


import PropTypes from 'prop-types';
import { withRouter } from 'react-router-dom';
import Style from ''



class GruppenListe extends React.Component {

    constructor(props) {
        super(props);

        this.state = {
            gruppen: [],
            loadingProgress: false,
            error: null
        };
    }

    componentDidMount(){
        this.getGruppen();
    }


    render() {
        const {classes} = this.props
        return (
            <div>
                <Grid justify= "flex-end" >
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