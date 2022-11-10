//即時驗證
let inputs = document.querySelectorAll("input"); // inputs 為一個 NodeList (類陣列)
inputs.forEach(input => {
    input.addEventListener("input", function(){
        if (input.checkValidity()){
            input.classList.add("valid");
            input.classList.remove("invalid");
        }else{
            input.classList.remove("valid");
            input.classList.add("invalid");
        }
    })
})

// For loop
// for(let i = 0; i < inputs.length; i++){
//     console.log(inputs[i])
//     inputs[i].addEventListener("input", function(){
//         if (inputs[i].checkValidity()){
//             inputs[i].classList.add("valid");
//             inputs[i].classList.remove("invalid");
//         }else{
//             inputs[i].classList.remove("valid");
//             inputs[i].classList.add("invalid");
//         }
//     })
// }


// password-eye

let eye_signup = document.getElementById("eye_signup");
let eye_login = document.getElementById("eye_login");
let password_signup = document.getElementById("password_signup");
let password_login = document.getElementById("password_login");
eye_signup.addEventListener("click", function(e){
    if(e.target.classList.contains("fa-eye")){
        e.target.classList.remove("fa-eye");
        e.target.classList.add("fa-eye-slash");
        password_signup.setAttribute("type", "text");
    }else{
        password_signup.setAttribute("type", "password");
        e.target.classList.add("fa-eye");
        e.target.classList.remove("fa-eye-slash");
    };

});

eye_login.addEventListener("click", function(e){
    if(e.target.classList.contains("fa-eye")){
        e.target.classList.remove("fa-eye");
        e.target.classList.add("fa-eye-slash");
        password_login.setAttribute("type", "text");
    }else{
        password_login.setAttribute("type", "password");
        e.target.classList.add("fa-eye");
        e.target.classList.remove("fa-eye-slash");
    };
});