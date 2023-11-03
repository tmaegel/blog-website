let storageState = localStorage.getItem("theme");
if (storageState != null) {
  if (storageState == "dark") {
    document.documentElement.setAttribute("data-theme", "dark");
  } else if (storageState == "light") {
    document.documentElement.setAttribute("data-theme", "light");
  }
}

function toggleTheme() {
  let documentState = document.documentElement.getAttribute("data-theme");
  if (documentState == "dark") {
    localStorage.setItem("theme", "light");
    document.documentElement.setAttribute("data-theme", "light");
  } else if (documentState == "light") {
    localStorage.setItem("theme", "dark");
    document.documentElement.setAttribute("data-theme", "dark");
  } else {
    // Default
    document.documentElement.setAttribute("data-theme", "dark");
  }
}
