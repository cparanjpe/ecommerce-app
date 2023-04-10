let main_container = document.getElementById("main-container")


window.addEventListener("load", async () => {
    const res = await fetch(`${window.location.origin}/api/fetch_category?category=iphones`)
    const data = await res.json();
    let data_str = ``
    console.log(data)
    data.forEach((ele) => {
        data_str += `        
        <div class="lg:w-1/4 md:w-1/2 p-4 w-full bg-slate-700 m-5 flex space-x-10">
            <a class="block relative rounded overflow-hidden">
                <img alt="ecommerce" class="object-cover rounded object-center mx-auto block" src="${ele.image}">
            </a>
            <div class="mt-4">
                <h3 class="text-gray-500 text-xs tracking-widest title-font mb-1">CATEGORY</h3>
                <h2 class="text-white title-font text-lg font-medium">${ele.name}</h2>
                <p class="mt-1">$16.00</p>
            </div>
        </div>`
    })
    main_container.innerHTML += data_str
})