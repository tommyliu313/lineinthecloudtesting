import Swal from 'sweetalert2'
import {CognitoUser, ISignUpResult} from 'amazon-cognito-identity-js'
import { Auth } from 'aws-amplify'
// Setup the configuration
Auth.configure({
    userPoolId:'',
    userPoolWebClientId:'',
})

function onResendConfirmationCode(){
 Auth.resend();

}

function onHostedUISignIn(){
    Auth.federatedSignIn().then(result =>{
        
    })
}
