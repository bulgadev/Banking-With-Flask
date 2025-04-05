document.addEventListener("DOMContentLoaded", () => {
    const error = document.body.dataset.error;
  
    if (error) {
      console.log("Erro:", error);
      alert(error); // ou mostrar num modal bonitão
    }
  });
  
  function openWith() {
    document.getElementById("withdraw").style.display = "block"
  }

  function closeWith() {
    document.getElementById("withdraw").style.display = "none"
  }

//detects click
window.onclick = function(event) {
    const modal = document.getElementById("withdraw")
    if (event.target == modal) {
        closeWith()
    }
}
//-----------------------------------------------------------
function openDepo() {
    document.getElementById("deposit").style.display = "block"
  }

  function closeDepo() {
    document.getElementById("deposit").style.display = "none"
  }

//detects click
window.onclick = function(event) {
    const modal = document.getElementById("deposit")
    if (event.target == modal) {
        closeDepo()
    }
}