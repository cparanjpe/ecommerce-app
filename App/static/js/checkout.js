const addContainer = document.getElementById("add-container")
const priceContainer = document.getElementById("item-total1")
const taxContainer = document.getElementById("tax1")
const totalContainer = document.getElementById("total-bill1")
const placeOrder = document.getElementById("place-order")
let cartval = 0

window.addEventListener("load", async () => {
    renderPrice()
})
placeOrder.addEventListener("click",()=>{
    window.location.href = `/addorder/${1.18*cartval + 100}`;
})
const renderPrice = async()=>{
    let res = await fetch(`${window.location.origin}/api/fetch_cart_items`)
    let data = await res.json()
    cartval = 0
    data.forEach(ele => {
        let value = ele.product.price
        value = value.replace(",","")
        value = parseInt(value)
        cartval += value
        // alert(cartval)
        // todo
        // calculations for detail panel
    
        
    });
    // cartContainer.innerHTML = dataStr    
    priceContainer.innerHTML = `₹ `+cartval
    taxContainer.innerHTML = `₹ `+0.18*cartval
    totalContainer.innerHTML = `₹ `+(1.18*cartval + 100)
}