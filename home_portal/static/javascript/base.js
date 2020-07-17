const navSlide = () => {
  const burger = document.querySelector(".burger");
  const sidebar = document.querySelector(".side-bar");

  burger.addEventListener("click", () => {
    //Toggle Nav
    sidebar.classList.toggle("sidebar-active");

    // Burger Animation
    burger.classList.toggle("burger-animate");
  });
};

navSlide();
