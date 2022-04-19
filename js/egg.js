var egg = 0;

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks the button, open the modal 
myEgg.onclick = function() {
  if (egg == 4){
    modal.style.display = "block";
    egg=-9999;
    span = document.getElementById("egg_text").textContent = "A veces es mejor empezar de cero para encontrar el camino.";   
  } else {
      egg++;
  }
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}