import React, {Component} from 'react';
import PropTypes from 'prop-types';

class SignIn extends Component {

    constructor(props) {
        super(props);

        this.state = {
            profil: null,
            profilEdited: false,


        };
    }
        // Handles the event of pressing  the SignIn button
        handleSignInButtonClicked = () => {

        }
        // Rendern der Komponente Sign In
        render() {
            const { 
                profil, 
                profilEdited,

            } = this.state;
            const { classes } = this.props;

            return <div>
                <Paper>
                    <Card>
                        <Typography className={classes.root} align="center" variant="h5">Willkommen zur Lerngruppen App</Typography>
                        <Grid container justify="center">
                            <Grid item>
                                <FormControl className={classes.formControl}>
                                    <InputLabel>Student Login</InputLabel>
                                    <Select required onChange={this.handleChange}>
                                        <Menuitem value= "Login">Login mit Profil</Menuitem>
                                        <Menuitem value= "Register">Register new Profil</Menuitem>
                                    </Select>
                                </FormControl>
 
                    

                            </Grid>
                        </Grid>
                    </Card>
                </Paper>
            </div>
        }
    
}


export default withStyles(styles)(SignIn)