function toggleDropDown() {
    document.getElementById("themesDropDown").classList.toggle("show");
}

window.onclick = function(event) {
    if (!document.getElementById('themeSwitcher').contains(event.target)) {
        var dropdowns = document.getElementsByClassName("themesDropDown");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
          var openDropdown = dropdowns[i];
          if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
          }
        }
    }
    // if (!event.target.matches('.themeSwitcherBtn')) {

    // }
  }