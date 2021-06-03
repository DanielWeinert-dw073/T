import React, {Component} from 'react';
import PropTypes from 'prop-types';
import { Button, Grid, Typography, withStyles, Paper, Card } from '@material-ui/core';




class SignIn extends Component {


    
        // Handles the event of pressing  the SignIn button
        handleSignInButtonClicked = () => {
            this.props.onSignIn();

        }
        // Rendern der Komponente Sign In
        render() {
    
            const { classes } = this.props;

            return <div>
                <Paper>
                    <Card>
                        <Typography className={classes.root} align="center" variant="h5">Willkommen zur Lerngruppen App</Typography>
                        <Grid container justify="center">
                            <Grid item>
                                <Button variant='contained' color='primary' onClick={this.handleSignInButtonClicked}>
							        Sign in with Google
      			                </Button>
 
                    

                            </Grid>
                        </Grid>
                    </Card>
                </Paper>
            </div>
        }
    
}
/** Component specific styles */
const styles = theme => ({
	root: {
		margin: theme.spacing(2)
	}
});

/** PropTypes */
SignIn.propTypes = {
	/** @ignore */
	classes: PropTypes.object.isRequired,
	/** 
	 * Handler function, which is called if the user wants to sign in.
	 */
	onSignIn: PropTypes.func.isRequired,
}


export default withStyles(styles)(SignIn)