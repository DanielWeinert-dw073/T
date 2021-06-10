import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Paper, Typography, Tabs, Tab } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import ProfileDropDown from '../dialogs/ProfileDropDown';
import { withRouter } from 'react-router-dom';

/** 
 * Zeigt den Header mit den verfügbaren Tabs.
*/

class Header extends Component {
    constructor(props) {
        super(props);

        //init empty state
        this.state = {
            tabindex: 0
        };
    }
    // handles changes of the state of the Component
    handleTabChange = (e, newIndex) => {
        this.setState({
            tabindex: newIndex
        })
    };
    //Rendern der Komponenten
    render() {
        const {classes, user, currentUser} = this.props;
        return (
            <Paper variant = "outlined" >
                <ProfileDropDown user={user} />
                <Typography  variant = "h3" component = "h1" align = "center">
                    HdM LerngruppenTool
                </Typography>
                <Typography  variant = "h5" component = "h2" align = "center">
                    Powered by Gruppenalgorithmus
                </Typography>
                {
                    user ? 
                                    
                    <>
               
                        <>
                        <Paper variant = "outlined">
                            
                            <Tabs indicatorColor='secondary' textColor='secondary' variant='fullWidth' centered value={this.state.tabindex} onChange={this.handleTabChange}>
                                <Tab label='Profil' component={RouterLink} to={`/profile`} />
                                <Tab label="GruppenListe" component={RouterLink} to={'/gruppen'}/>
                                <Tab label="Chat" component={RouterLink} to={'/chat'}/>
                                <Tab label='About' component={RouterLink} to={`/about`} />
                            </Tabs>
                        </Paper>
                        </>
                     
                        
                    
                    
                    </>
                    :null
                
                }
            </Paper>
        )
    }

}

const styles = theme => ({
    root: {
        width: '100%',
    },
    tab: {
        minWidth: 150, // a number of your choice
        width: 150, // a number of your choice
    },
    text1: {
        paddingLeft: '64px',
        marginTop: theme.spacing(2)
    },
    text2: {
        marginBottom: theme.spacing(2),
    },
      
});
      
      
// Prop Type
Header.propTypes = {
    // logged in Firebase user/person
    user: PropTypes.object,
}
      


export default Header;