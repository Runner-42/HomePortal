const navSlide = () => {
  const burger = document.querySelector(".burger");
  const sidebar = document.querySelector(".side-bar");
  const sidebarItems = document.querySelectorAll(".side-bar li");

  burger.addEventListener("click", () => {
    //Toggle Nav
    sidebar.classList.toggle("sidebar-active");

    // Animate Nav Items
    sidebarItems.forEach((sidebarItem, index) => {
      if (sidebarItem.style.animation) {
        sidebarItem.style.animation = "";
      } else {
        sidebarItem.style.animation =
          "sidebarItemsFade 0.5s ease forwards $(index/5 + 2)s";
      }
    });

    // Burger Animation
    burger.classList.toggle("burger-animate");
  });
};

navSlide();
