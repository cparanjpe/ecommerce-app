let username = document.getElementById("username")
let email = document.getElementById("email")
// let age = document.getElementById("age")
let gender = document.getElementById("gender")
let password = document.getElementById("password")
let btn = document.getElementById("signup-btn")
let age = document.getElementById("minmax-range")
let label = document.getElementById("age-label")


btn.addEventListener("click", async () => {
    console.log(username.value)
    console.log(email.value)
    console.log(age.value)
    console.log(password.value)
    console.log(gender.value)
    let res = await fetch(`${window.location.origin}/api/user/signup`, {
        method: "POST",
        body: JSON.stringify({ name: username.value, email: email.value, age: age.value, gender: gender.value, password: password.value }),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
    if(res.status === 200)
        window.location.href = "/"
})
age.addEventListener("change" , ()=>{
    label.innerText = `Age : ${age.value}`
})
