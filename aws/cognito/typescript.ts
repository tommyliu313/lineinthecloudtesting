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


async function Swal_Success_Button(){
return Swal.fire({
title:'You are successfully login now.',
'success'

});
}

const Swal_Fail_Button = {

   
})

}