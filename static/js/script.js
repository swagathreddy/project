const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const register=document.querySelector("#register");
const login=document.querySelector("#login");
const container = document.querySelector(".container");
const cls=document.querySelectorAll("#close");
setTimeout(()=>{
  const x=document.querySelector(".container")
  x.style.display="flex";
},2000);

function closecont(){
  container.style.display="none";
}
function open_login(){
  closemenu();
  container.style.display="flex";
  container.classList.remove("sign-up-mode");
}

function closemenu(){
  let x=document.querySelector(".menu");
  x.style.display="none";
}
function openmenu(){
  let x=document.querySelector(".menu");
  x.style.display="flex";
}

function open_register(){
  closemenu();
  container.style.display="flex";
  container.classList.add("sign-up-mode");
}

register.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

login.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});

sign_up_btn.addEventListener("click", () => {
  container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
  container.classList.remove("sign-up-mode");
});
