const navSlide = () => {
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-items');
    const navItems = document.querySelectorAll('.nav-items li');


    burger.addEventListener('click',()=>{
        //Toggle Nav
        nav.classList.toggle('nav-active');

        // Animate Nav Items
        navItems.forEach((navItem, index)=>{
            if(navItem.style.animation) {
                navItem.style.animation = ''
            } else {
                navItem.style.animation = 'navItemsFade 0.5s ease forwards $(index/5 + 2)s';
            }
            
        });

        // Burger Animation
        burger.classList.toggle('burger-animate');
    });
    
}

navSlide();