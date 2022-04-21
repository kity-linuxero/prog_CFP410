var egg = 0;
var egg2 = 0;

// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("myBtn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

function egg_2(){
  if (egg2 ===4){
    if (egg < 0){
      alert("Te conviene empezar de nuevo :(")
    }else{
    alert("Estuviste cerca. Pero es el otro ;)");
    egg2=0;}
  }else{
    egg2++;
  }
}

function egg_fun() {
  if (egg === 4){
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
  if (event.target === modal) {
    modal.style.display = "none";
  }
}