import React from 'react';
import { BrowserRouter as Router, Route, Redirect } from 'react-router-dom';
import { Container, ThemeProvider, CssBaseline } from '@material-ui/core';
import firebase from 'firebase/app'; //Firebase module
import 'firebase/auth'; //Firebase module
import Header from './components/layout/Header';
import LerngruppenToolAPI from './api/LernGruppenToolAPI';

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
            currentStudent: null,
            currentProfil: null
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
                this.getUserByGoogleID()
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

    //aktuell eingeloggter Student im backend abfragen
    getUserByGoogleID = () => {
        LerngruppenToolAPI.getAPI().getStudentByGoogleID(this.state.currentUser.uid)
            .then(studentNbo => 
                this.setState({
                    currentStudent: studentNbo,
                    error: null,
                    loadingInProgress: false
                })
                ).catch(e =>
                    this.setState({
                        currentStudent:null,
                        error: e,
                        loadingInProgress: false
                    }));
            this.setState({
                error: null,
                loadingInProgress: true
            });


    }

    //Lifecyclemethode
    componentDidMount() {
        firebase.initializeApp(firebaseConfig);
        firebase.auth().onAuthStateChanged(this.handleAuthStateChange);
    }

    render() {
        const { currentUser, appError, authLoading, authError, currentStudent, currentProfil} = this.state;

        return (
            <ThemeProvider theme={Theme}>
                <CssBaseline />
                <Router basename = {process.env.PUBLIC_URL}>
                    <Container maxWidth="md">
                        <Header user={currentUser} currentStudent={currentStudent} currentProfil={currentProfil}/>

                        {
                            //user signed in? 
                            currentUser && (currentStudent || currentProfil ) ?
                                <>
                                    <Redirect from="/" to="profil"/>
                                    <Route path="/projekte" component = {ProfilListe}>
                                        <ProfilListe current Student = {currentStudent} currentProfil = {currentProfil}/>
                                    </Route>

                                </>
                                :
                                
                                //if not signed in show sign in page
                                <>
                                    <Redirect to="index.html"/>
                                    <SignIn onSignIn={this.handleSignIn}/>
                                </>
                            
                        }
                        <LoadingInProgress show={authLoading} />
                        <ContextErrorMessage error={authError} contextErrorMessage={`Something went wrong during signIn process.`} onReload={this.handleSignIn} />
                        <ContextErrorMessage error={appError} contextErrorMessage={"Something went wrong inside the App. Please reload."}/>


                    </Container>
                </Router>

            </ThemeProvider>
        )
    }
    
}

export default App;