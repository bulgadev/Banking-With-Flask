document.addEventListener("DOMContentLoaded", () => {
    const error = document.body.dataset.error;
  
    if (error) {
      console.log("Erro:", error);
      alert(error); // ou mostrar num modal bonitão
    }
  });
    //functions withdraw
  function openWith() {
    document.getElementById("withdraw").style.display = "block"
  }

  function closeWith() {
    document.getElementById("withdraw").style.display = "none"
  }

  //functions deposit
function openDepo() {
    document.getElementById("deposit").style.display = "block"
  }

  function closeDepo() {
    document.getElementById("deposit").style.display = "none"
  }
    //functions transfer
function openTransfer() {
    document.getElementById("transfer").style.display = "block"
  }

  function closeTransfer() {
    document.getElementById("transfer").style.display = "none"
  }

  //detects clcik
window.onclick = function(event) {
    const transfer = document.getElementById("transfer")
    const deposit = document.getElementById("deposit")
    const withdraw = document.getElementById("withdraw")
    if (event.target == transfer) {
        closeTransfer()
    }

    if (event.target == deposit) {
        closeDepo()
    }

    if (event.target == withdraw) {
        closeWith()
    }
}