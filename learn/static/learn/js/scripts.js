function myFunction() {
    var x = document.getElementById("demo");
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
    } else { 
      x.className = x.className.replace(" w3-show", "");
    }
  }
function w3_open() {
    document.getElementById("main").style.marginLeft = "25%";
    document.getElementById("mySidebar").style.width = "25%";
    document.getElementById("mySidebar").style.display = "block";
    document.getElementById("openNav").style.display = 'none';
  }
  function w3_close() {
    document.getElementById("main").style.marginLeft = "0%";
    document.getElementById("mySidebar").style.display = "none";
    document.getElementById("openNav").style.display = "inline-block";
  }
  /*slideshow*/
  sliderInt = 1;
sliderNext = 2;

$(document).ready(function() {
    $('.num#1').fadeIn(300);
    startSlider();
});

function startSlider() {
    count = $('.num').length;
    loop = setInterval(function() {
        
        if(sliderNext > count) {
            sliderNext = 1;
            sliderInt = 1;
        }
        
        $('.num').fadeOut(300);
        $('.num#' + sliderNext).fadeIn(300);
        
        sliderInt = sliderNext;
        sliderNext = sliderNext + 1;
        
    }, 2000)
    
    
}

function prev() {
    newSlide = sliderInt - 1;
    showSlide(newSlide);
}

function next() {
    newSlide = sliderInt + 1;
    showSlide(newSlide);
}

function stopLoop() {
    window.clearInterval(loop);
}

function showSlide(id) {
    stopLoop();
    if(id > count) {
            sliderNext = 1;
            sliderInt = 1;
        }
    else if(id < 1) {
        id = count;
    }
        
    $('.num').fadeOut(300);
    $('.num#' + id).fadeIn(300);
        
    sliderInt = id;
    sliderNext = id + 1;
    startSlider();
}

$('.num').hover(
    function() {
        stopLoop();
    },
    function() {
        startSlider();
    }
);
