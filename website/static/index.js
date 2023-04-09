// function deleteNote(noteId) {
//   fetch("/delete-note", {
//     method: "POST",
//     body: JSON.stringify({ noteId: noteId }),
//   }).then((_res) => {
//     window.location.href = "/";
//   });
// }
const fetchProducts = async ()=>{
  const response = await fetch('https://fakestoreapi.com/products');
  const data = await response.json();
  let dataString = ``
  data.map(item=>{
    //  if(item.category == "men's clothing" || item.category == "women's clothing")
      dataString+=`<div class="col-md-4 col-sm-6">
      <div class="box content-card" >
            <img src=${item.image} alt="" class="product-img" srcset="">
             <h2>${item.title}</h2>
             <p>${item.description.substring(0,122)}...</p>
             <div class="price-cartbutton">
             <h2>₹${Math.ceil(item.price*80)}</h2>
             <a href="/add_to_cart/${item.id}" class="btn btn-primary" id=${item.id} product_id=${item.id}>Add to cart</a>
             </div>
      </div>
 </div>`
  })
  document.getElementById('row').innerHTML+=dataString
}

