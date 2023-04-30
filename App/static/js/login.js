let email = document.getElementById("email")
let password = document.getElementById("password")
let btn = document.getElementById("login-btn")
let loader_container = document.getElementById("loader-container")

btn.addEventListener("click" , async()=>{
    loader_container.innerHTML = `<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
    </div>`
    let res = await fetch(`${window.location.origin}/api/user/login`, {
        method: "POST",
        body: JSON.stringify({ email: email.value, password: password.value }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    if(res.status === 200)
        window.location.href = "/"
})
