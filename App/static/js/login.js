let email = document.getElementById("email")
let password = document.getElementById("password")
let btn = document.getElementById("login-btn")

btn.addEventListener("click" , async()=>{
    console.log(email.value , password.value)
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
