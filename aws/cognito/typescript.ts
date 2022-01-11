import Swal from 'sweetalert2'
import {CognitoUser, ISignUpResult} from 'amazon-cognito-identity-js'
import { Auth } from 'aws-amplify'

// Setup the configuration
Auth.configure({
    userPoolId:'us-east-1_dqiapzBbr',
    userPoolWebClientId:'57a80fik1473v2up522vav7br2',
})

var currentUserNAme: 

function onResendConfirmationCode(){
 Auth.resend();

}

function onHostedUISignIn(){
    Auth.federatedSignIn().then(result =>{
        
    })
}

function onUserConfirmation(){}

function onResendConfirmationCode(){
    Auth.resendSignUp()
}

