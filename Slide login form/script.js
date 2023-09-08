// import Swal from 'sweetalert2/dist/sweetalert2.js'

document.addEventListener("DOMContentLoaded", function () {
    const login = document.querySelector('.login')
    const signup = document.querySelector('.signup')

    signup.addEventListener('submit', function(event){
        event.preventDefault();

        const email = document.getElementById('signup_email').value
        const confirm_email = document.getElementById('confirm_email').value
        const password = document.getElementById('signup_password').value
        const confirm_password = document.getElementById('confirm_password').value

        if(email == confirm_email && password == confirm_password){
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Registration Successful !!',
                showConfirmButton: false,
                timer: 1500
              })
            // localStorage.setItem('email', signup_email)
            // localStorage.setItem('password', signup_password)

            let user_records = new Array();
            user_records = JSON.parse(localStorage.getItem('users'))?JSON.parse(localStorage.getItem('users')):[]
            if(user_records.some((v) => {
                return v.email == email
            })){
                Swal.fire({
                    icon: 'error',
                    title: 'Oops...',
                    text: 'This account already exists!!',
                  })
            }
            else{
                user_records.push({
                    "email" : email,
                    "password" : password,
                })
                localStorage.setItem('users', JSON.stringify(user_records));
            }
        }
        else{
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Wrong credentials!, Please try again..',
              })
        }

    })

    login.addEventListener('submit', function(event){
        event.preventDefault();

        const email = document.getElementById('login_email').value
        const password = document.getElementById('login_password').value

        let user_records = JSON.parse(localStorage.getItem('users'))?JSON.parse(localStorage.getItem('users')):[]
        if(user_records.some((v) =>{
            return v.email == email && v.password == password
        })){
            Swal.fire({
                position: 'center',
                icon: 'success',
                title: 'Login Successful',
                showConfirmButton: false,
                timer: 1500
              })

            let current_user = user_records.filter((v)=>{
                return v.email == email && v.password == password
            })[0]
        }
        else{
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong!, Please try again',
              })
        }

    })
})


/* array bana kr usmai push krwao phir uss pori array ko local storage mai daal do */