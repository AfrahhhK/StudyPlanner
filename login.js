
// const loginForm = document.getElementById("login-form");
// const loginButton = document.getElementById("submit");
// const clearButton = document.getElementById("clear")
// const loginErrorMsg = document.getElementById("login-error-msg");

// loginButton.addEventListener("click", (e) => {
//     e.preventDefault();
//     const username = loginForm.username.value;
//     const password = loginForm.password.value;

//     if (username === "user" && password === "123") {
//         // alert("You have successfully logged in!");
//         document.getElementById('login').addEventListener('click', function () {
//             // Change the URL to the desired page
//             window.location.href = 'index.html';
//         });
        
//         // location.reload();

//     } else {
//         loginErrorMsg.style.opacity = 1;
//     }
// })





const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("submit");
const clearButton = document.getElementById("clear")
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    if (username === "user" && password === "123") {
        // Redirect to the index.html page
        window.location.href = 'index.html';
    } else {
        loginErrorMsg.style.opacity = 1;
    }
});
