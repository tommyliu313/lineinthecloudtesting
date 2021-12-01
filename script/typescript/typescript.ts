import Swal from 'sweetalert2'
import {CognitoUser, ISignUpResult} from 'amazon-cognito-identity-js'

Auth.configure({
    userPoolId:'',
    userPoolWebClientId:'',
})