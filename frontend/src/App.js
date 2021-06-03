import React from 'react';
import Theme from './Theme';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@material-ui/core';
import firebase from 'firebase/app'; //Firebase module
import 'firebase/auth'; //Firebase module
import Header from './components/layout/Header';
import LerngruppenToolAPI from './api/LernGruppenToolAPI';
import TeilnahmeBO from './api/TeilnahmeBO'; 
import ProfilÜbersicht from './components/ProfilÜbersicht';
//import ProfilÜbersichtEintrag from './components/ProfilÜbersichtEintrag';
import SignIn from './components/pages/SignIn';
import ContextErrorMessage from './components/dialogs/ContextErrorMessage';
import LoadingProgress from './components/dialogs/LoadingProgress';
import firebaseConfig from './firebaseconfig'
import About from './components/pages/About';

/** 
 * Mainpage der LerngruppenApp. Verifizierung der nutzer über die firebase. Anschließend
 * erfolgt das Routing zu den Seiten via react router dom
*/

class App extends React.Component {

    // initialize firebase
    constructor(props) {
        super(props);

        // initialize empty values
        this.state = {
            currentUser: null,
            appError: null,
            authError: null,
            authLoading: false,
 
        };
    }


    static getDerivedStateFromError(error) {
        
        return {appError: error};

    }

    // handles all user login states with firebase
    handleAuthStateChange = user => {
        if (user) {
            this.setState({
              authLoading: true, 
            });
            // user signed in
            user.getIdToken().then(token => {
              // Token gets storend into cookie
              // Server (backend) can then read out that cookie
              // only token information, safety risk!
                document.cookie = `token=${token};path=/`;
              // set user when token arrives
                this.setState({
                    currentUser: user,
                    authError: null,
                    authLoading: false
                })}).then(() => {
                this.getUserByGoogleId()
            }).catch(e => {
                this.setState({
                    authError: e,
                    authLoading: false
                });
            });
        } else {
            // user loggend out -> clear id token
            document.cookie = 'token=;path=/';
      
            // Set the logged out user to null
            this.setState({
                currentUser: null,
                authLoading: false
            });
        }
    }
    //Handles the sign in component with firebase authentication() firebase.auth()
    handleSignIn = () => {
        this.setState({
            authLoading: true
        });
        const provider = new firebase.auth.GithubAuthProvider();
        firebase.auth().signInWithRedirect(provider);
    }

  
    //Lifecyclemethode
    componentDidMount() {
        firebase.initializeApp(firebaseConfig);
        firebase.auth().languageCode = 'en';
        firebase.auth().onAuthStateChanged(this.handleAuthStateChange);
    }

    render() {
        const { currentUser, appError, authLoading, authError, currentStudent, currentProfil} = this.state;

        return (
            <ThemeProvider theme={Theme}>
                <CssBaseline />
                <Router basename = {process.env.PUBLIC_URL}>
                    <Container maxWidth="md">
                        <Header user={currentUser} />

                        {
                            //user signed in? 
                            currentUser ?
                                <>
                                    <Redirect from="/" to="profil"/>
                                    <Route exact path="/profil" >
                                        <ProfilÜbersicht />
                                    </Route>

                                    <Route path="/about" component = {About}/>

                                  

                                </>
                                :
                                
                                //if not signed in show sign in page
                                <>
                                    <Redirect to="index.html"/>
                                    <SignIn onSignIn={this.handleSignIn}/>
                                </>
                            
                        }
                        <LoadingProgress show={authLoading} />
                        <ContextErrorMessage error={authError} contextErrorMessage={`Something went wrong during signIn process.`} onReload={this.handleSignIn} />
                        <ContextErrorMessage error={appError} contextErrorMessage={"Something went wrong inside the App. Please reload."}/>


                    </Container>
                </Router>

            </ThemeProvider>
        );
    }
    
}

export default App;