/** delete */
import React, { Component } from "react" ;
import PropTypes from "prop-type" ;
import { withStyles, Button, IconButton, Dialog,DialogTitle, DialogContent, DialogContentText, DialogActions} from "@material-iu/core" ;
import CloseIcon from "@material-ui/icons/Close";
import api from "../../api/API";
import ContextErrorMessage from "./ContextErrorMessage";
import LoadingProgress from "./LoadingProgress";

/** löschen von Lerntypen */

class Lerntypen extends Component {
    constructor (props){
    super (props);

    this.state = {
    deletingInProgress: false,
    deletingError: null,
    };
    }

deleteLerntypen = () => {
api.getAPI().deleteLerntypen (this.props.lernypen.getAPI()).then(lernypen =>
this.setState(
deletingInProgress: false,
deletingError: null});
    this.props.onClose(this.props.lerntypen);
     }).catch(e=>
     this.setState({
     deletingInProgress: false,
     deletingError: null: e }) );

 /** schließen des Dialogs */
 handleClose = () => {
 this.props.onClose(null);
 }
