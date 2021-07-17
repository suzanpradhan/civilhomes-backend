function navigationNav() {
    var x = document.getElementById("reponsiveNavBar");
    if (x.className === "navigation") {
      x.className += " responsive";
    } else {
      x.className = "navigation";
    }
  }

document.getElementById('videoSpeed').playbackRate = 0.5;