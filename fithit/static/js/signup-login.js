const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const signup_submit = document.getElementById('signup-submit');
const login_submit = document.getElementById('login-submit');

const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});
// signup_submit.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});
// login_submit.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });