import Button from '@material-ui/core/Button';
import { withStyles } from '@material-ui/core/styles';
import React, { Component } from 'react';
import {Link} from 'react-router-dom';
import Typography from '@material-ui/core/Typography';

class StartSeite extends React.Component {

    constructor(props) {
        super(props);

    }
    render() {
        return(
            <div>
                <center>
                    <Typography>
                        
                        Navigation zu deinen Nachrichten, deinem Profil und der Gruppenübersicht
                        
                    </Typography>
                    <Link to='/nachrichten'>
                        <Button
                            size= "large"
                            variant="contained"
                            color="primary">  
                            Nachrichten                            
                        </Button>
                    </Link>
                    <Link to='/profile'>
                        <Button
                            size= "large"
                            variant="contained"
                            color="primary">  
                            Profil                                
                        </Button>
                    </Link>
                    <Link to='/gruppen'>
                        <Button
                            size= "large"
                            variant="contained"
                            color="primary">  
                            Gruppen                              
                        </Button>
                    </Link>
                    <Link to='/about'>
                        <Button
                            size= "medium"
                            variant="contained"
                            color="primary">  
                            About                            
                        </Button>
                    </Link>

                </center>
            </div>
        );
    }


}

export default StartSeite;
