import Swal from 'sweetalert2'
import {CognitoUser, ISignUpResult} from 'amazon-cognito-identity-js'
import { Auth } from 'aws-amplify'

// Setup the configuration
Auth.configure({
    userPoolId:'us-east-1_dqiapzBbr',
    userPoolWebClientId:'57a80fik1473v2up522vav7br2',
})

<<<<<<< HEAD
var currentUserNAme: 
=======
currentUserName = userData.username;
if
>>>>>>> 0c89f5a2de115f856e9bd5aff9f625df85cb633e

function onResendConfirmationCode(){
 Auth.resend();

}

function onHostedUISignIn(){
    Auth.federatedSignIn().then(result =>{
        
    })
}

function onUserConfirmation(){}

<<<<<<< HEAD
function onResendConfirmationCode(){
    Auth.resendSignUp()
=======
function onSignUp(){
    let userinfo = {
        username: document.getElementById("login").value,
        password: document.getElementById("password").value,
        
    }
>>>>>>> 0c89f5a2de115f856e9bd5aff9f625df85cb633e
}
