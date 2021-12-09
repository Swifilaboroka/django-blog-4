const navbar_toggle = () => {
  const toggler = document.getElementById("navbar_toggler");
  const toggleable_navbar = document.getElementById("toggleable_navbar");

  toggler.addEventListener("click", (e) => {
    console.log("CLicked");
    toggleable_navbar.classList.toggle("active");
  });
};

const app = () => {
  navbar_toggle();
  console.log("Working");
};

app();
