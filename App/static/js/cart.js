const cartContainer = document.getElementById("cart-container")
const priceContainer = document.getElementById("item-total")
const taxContainer = document.getElementById("tax")
const totalContainer = document.getElementById("total-bill")
let cartval = 0

const removeItem = async(product_id)=>{    
    let res = await fetch(`${window.location.origin}/api/remove_item_from_cart/${product_id}`)
    let data = await res.json()
    if(res.status === 200){
        renderCart()
    }
}


window.addEventListener("load", async () => {
    renderCart()
})


const renderCart = async()=>{
    let res = await fetch(`${window.location.origin}/api/fetch_cart_items`)
    let data = await res.json()
    let dataStr = ``
    cartval = 0
    data.forEach(ele => {
        let value = ele.product.price
        value = value.replace(",","")
        value = parseInt(value)
        cartval += value
        // todo
        // calculations for detail panel
        dataStr += `
            <div class="shadow-[0_2.8px_2.2px_rgba(0,_0,_0,_0.034),_0_6.7px_5.3px_rgba(0,_0,_0,_0.048),_0_12.5px_10px_rgba(0,_0,_0,_0.06),_0_22.3px_17.9px_rgba(0,_0,_0,_0.072),_0_41.8px_33.4px_rgba(0,_0,_0,_0.086),_0_100px_80px_rgba(0,_0,_0,_0.12)] bg-slate-700 my-5 mx-8 flex rounded-2xl space-x-10">
            <div class="block bg-white  px-3 rounded-l-2xl align-middle overflow-hidden">
                <img alt="ecommerce" class="object-cover mt-4 object-center block" src="${ele.product.image}">
            </div>
            <div class="mt-4 p-4">
                <h2 class="text-white title-font text-xl font-medium">${ele.product.name}</h2>
                <p>Rating : ${ele.product.rating}</p>
                <p>Discount : ${ele.product.discount}</p>
                <h1 class="mt-1 text-white font-bold text-xl">₹ ${ele.product.price}</h1>
                <a href="/details/${ele.category}/${ele.product.id}" type="button" class="cursor-pointer text-black mt-3 bg-yellow-400 hover:bg-yellow-500 focus:outline-none focus:ring-4 focus:ring-yellow-300 font-bold rounded-full text-sm px-3 py-1 text-center mr-2 mb-2 dark:focus:ring-yellow-900">View Details</a>
                <div class="mt-3">
                <button onclick="test()" type="button" class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-bold rounded-lg text-sm  px-4 py-2 text-center mr-2 mb-2">Buy Now</button>
                <button onclick="removeItem('${ele.product._id}')" , '${ele.product.id}')" type="button" class="text-gray-900 bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 font-bold rounded-lg text-sm px-4 py-2 text-center mr-2 mb-2">Remove from Cart</button>
                </div>
                </div>
            </div>
        `
    });
    cartContainer.innerHTML = dataStr    
    priceContainer.innerHTML = `₹ `+cartval
    taxContainer.innerHTML = `₹ `+0.18*cartval
    totalContainer.innerHTML = `₹ `+(1.18*cartval + 100)
}
