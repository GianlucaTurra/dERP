const icon = document.getElementById("eraser");
const search = document.getElementById("searchbar");
icon.style.display = "none";

search.addEventListener("input", function () {
  if (search.value === "") {
    icon.style.display = "none";
  } else {
    icon.style.display = "inline-block";
  }
});

search.addEventListener("keydown", function(event) {
  console.log(event);
  if (event.key === "Escape") {
    clearSearchBar();
  }
});

function manageKeyShortcuts(event) {
  console.log(event);
  if (event.key === "Escape") {
    clearSearchBar();
  }
}

function clearSearchBar() {
  search.value = "";
  icon.style.display = "none";
}

/* function showMenu() {
  const opacity = document.getElementById("user-menu").style.opacity;
  if (opacity == 1) {
    document.getElementById("user-menu").style.opacity = 0;
  } else {
    document.getElementById("user-menu").style.opacity = 1;
  }
} */
