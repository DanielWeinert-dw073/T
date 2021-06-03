import React from 'react'
import { makeStyles, Paper, Typography, Link } from '@material-ui/core';
const useStyles = makeStyles(theme => ({
    root: {
      width: '100%',
      marginTop: theme.spacing(2),
      marginBottom: theme.spacing(2),
      padding: theme.spacing(1)
    },
    content: {
      margin: theme.spacing(1),
    }
  }));

function About() {

    const classes = useStyles();
  
    return (
      <Paper elevation={0} className={classes.root}>
        <div className={classes.content}>
            <Typography variant='h6'>
                Python Lerngruppen Tool
            </Typography>
            <br />
            <Typography variant='h6'>
                Link zum Repository <Link href ="https://github.com/SchenkTom/SW-Team19">Team 19</Link>
                </Typography>
            <Typography variant='body2'>
                © Hochschule der Medien 2020, all rights reserved.
            </Typography>
        </div>
      </Paper>
    )
}
export default About;