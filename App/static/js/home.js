let container = document.getElementById("main-container")


window.addEventListener("load", async () => {
    container.innerHTML = `<div class="flex justify-center relative top-[250px]"><div class="lds-facebook"><div></div><div></div><div></div></div></div>`
    const res = await fetch(`${window.location.origin}/api/homepage_content`)
    const data = await res.json();
    let sectionStr = ``
    let dataStr = ``
    for (const prop in data){
        dataStr = ``
        data[prop].forEach((ele) => {
            dataStr += `        
            <div class="w-[600px] shadow-[0_2.8px_2.2px_rgba(0,_0,_0,_0.034),_0_6.7px_5.3px_rgba(0,_0,_0,_0.048),_0_12.5px_10px_rgba(0,_0,_0,_0.06),_0_22.3px_17.9px_rgba(0,_0,_0,_0.072),_0_41.8px_33.4px_rgba(0,_0,_0,_0.086),_0_100px_80px_rgba(0,_0,_0,_0.12)] bg-slate-700 my-5 mx-8 flex rounded-2xl space-x-10">
                <div class="block bg-white  px-3 rounded-l-2xl align-middle overflow-hidden">
                    <img alt="ecommerce" class="object-cover mt-8 object-center block" src="${ele.image}">
                </div>
                <div class="mt-4 p-4">
                    <h2 class="text-white title-font text-lg font-medium">${ele.name}</h2>
                    <p>Rating : ${ele.rating}</p>
                    <p>Discount : ${ele.discount}</p>
                    <h1 class="mt-1 text-white font-bold text-xl">₹ ${ele.price}</h1>
                    <a href="/details/${prop}/${ele.id}" type="button" class="cursor-pointer text-black mt-3 bg-yellow-400 hover:bg-yellow-500 focus:outline-none focus:ring-4 focus:ring-yellow-300 font-bold rounded-full text-sm px-3 py-1 text-center mr-2 mb-2 dark:focus:ring-yellow-900">View Details</a>
                    <div class="mt-3">
                    <button type="button" class="text-white bg-gradient-to-br from-purple-600 to-blue-500 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-bold rounded-lg text-sm  px-4 py-2 text-center mr-2 mb-2">Buy Now</button>
                    <button name=${prop} type="button" class="text-gray-900 bg-gradient-to-r from-red-200 via-red-300 to-yellow-200 hover:bg-gradient-to-bl focus:ring-4 focus:outline-none focus:ring-red-100 dark:focus:ring-red-400 font-bold rounded-lg text-sm px-4 py-2 text-center mr-2 mb-2">Add to Cart</button>
                    </div>
                    </div>
            </div>`
        })
        sectionStr += `<div>
                        <h1 class="text-white text-2xl font-bold ml-28">${prop.toUpperCase()}</h1>
                        <div id="subContainer" class="flex flex-wrap justify-center mx-auto">
                            ${dataStr}
                        </div>  
                       </div>`
    }
    container.innerHTML = sectionStr
})
