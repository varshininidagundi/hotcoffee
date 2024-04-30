 // Get the "Add to Cart" button element by its id
 var addToCartButton = document.getElementById("addToCartBtn");

 // Add a click event listener to the button
 addToCartButton.addEventListener("click", function () {
     // Get the current quantity value
     var quantityElement = document.getElementById("cartQuantity");
     var currentQuantity = parseInt(quantityElement.innerText);

     // Increase the quantity by 1
     var newQuantity = currentQuantity + 1;

     // Update the quantity display
     quantityElement.innerText = newQuantity;
 });