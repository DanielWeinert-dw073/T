import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles, Paper, Typography, Tabs, Tab } from '@material-ui/core';
import { Link as RouterLink } from 'react-router-dom';
import ProfileDropDown from '../dialogs/ProfileDropDown';
import { withRouter } from 'react-router-dom';

/** 
 * Zeigt den Header mit den verfügbaren Tabs.
*/

class Header extends React.Component {
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
            <Paper className= {classes.root} variant = "outlined" >
                <ProfileDropDown user={user} />
                <Typography className={classes.text1} variant = "h3" component = "h1" align = "center">
                    HdM LerngruppenTool
                </Typography>
                <Typography className={classes.text2} variant = "h5" component = "h2" align = "center">
                    Powered by Gruppenalgorithmus
                </Typography>
                {
                    user ? 
                                    
                    <>
                    {currentStudent ?
                        <>
                        <Paper variant = "outlined">

                        </Paper>
                        </> 
                        :null
                    
                    }

                    </>
                    :null

                    
                }

            </Paper>
        )
    }



}
export default Header;