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
     if(item.category == "men's clothing" || item.category == "women's clothing")
      dataString+=`<div class="col-md-4 col-sm-6">
      <div class="box">
            <img src=${item.image} alt="" class="product-img" srcset="">
             <h2>${item.title}</h2>
             <p>${item.description.substring(0,122)}...</p>
             <a href="#" class="btn btn-primary">Add to cart</a>
      </div>
 </div>`
  })
  document.getElementById('row').innerHTML+=dataString
}

