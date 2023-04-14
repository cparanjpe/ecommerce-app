window.addEventListener("load",async()=>{
    var scriptTag = document.querySelector('script[items]');
    var items = scriptTag.getAttribute('items');
    var res = await fetch(`${window.location.origin}/api/fetch_category?category=LED`)
    var data = await res.json();
    let data_str = ``
    data.forEach((ele) => {   
        if(items.includes(ele.id)){
            data_str +=  ` <div class="flex justify-between px-5">
            <img src="${ele.image}" alt="" class="w-1/4 ">
            <h2 class="w-2/3 font-bold">${ele.name}</h2>
            <h5 class="font-bold">₹${ele.price}</h5>
        </div> ` 
        }
    })
    
    document.getElementById("cart-display").innerHTML+=data_str
})
    