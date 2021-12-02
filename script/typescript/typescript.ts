import Swal from 'sweetalert2'
import {CognitoUser, ISignUpResult} from 'amazon-cognito-identity-js'
import { Auth } from 'aws-amplify'
Auth.configure({
    userPoolId:'',
    userPoolWebClientId:'',
})

function onResendConfirmationCode(){
 Auth.resend;

}