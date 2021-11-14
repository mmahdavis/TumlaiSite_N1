/*

Template: BizBag - Multipurpose Business Startup HTML Template
Author: iqonicthemes.in
Version: 1.0
Design and Developed by: iqonicthemes.in


*/

/*----------------------------------------------
Index Of Script
------------------------------------------------

Page Loader
Isotope
Masonry
Back To Top
Tooltip
Sticky Header
Menu Bar
Accordion
Progress Bar
skrollr
Magnific Popup
Countdown
counter
Screenshots silder
Owl Carousel
Contact from

------------------------------------------------
Index Of Script
----------------------------------------------*/

$(window).on('load', function() {

    /*------------------------
     Page Loader
    --------------------------*/
    jQuery("#load").fadeOut();
    jQuery("#loading").delay(0).fadeOut("slow");


    $(".navbar a").on("click", function(event) {
        if (!$(event.target).closest(".nav-item.dropdown").length) {
            $(".navbar-collapse").collapse('hide');
        }
    });

    /*------------------------
    Isotope
    --------------------------*/
    $('.isotope').isotope({
        itemSelector: '.iq-grid-item',
    });

    // filter items on button click
    $('.isotope-filters').on('click', 'button', function() {
        var filterValue = $(this).attr('data-filter');
        $('.isotope').isotope({
            resizable: true,
            filter: filterValue
        });
        $('.isotope-filters button').removeClass('active');
        $(this).addClass('active');
    });

    /*------------------------
      Countdown
      --------------------------*/
    $('#countdown').countdown({
        date: '10/06/2020 23:59:59',
        day: 'Day',
        days: 'Days'
    });
    

    /*------------------------
    Masonry
    --------------------------*/

    var $msnry = $('.iq-masonry-block .iq-masonry');
    if ($msnry) {
        var $filter = $('.iq-masonry-block .isotope-filters');
        $msnry.isotope({
            percentPosition: true,
            resizable: true,
            itemSelector: '.iq-masonry-block .iq-masonry-item',
            masonry: {
                gutterWidth: 0
            }
        });
        // bind filter button click
        $filter.on('click', 'button', function() {
            var filterValue = $(this).attr('data-filter');
            $msnry.isotope({
                filter: filterValue
            });
        });

        $filter.each(function(i, buttonGroup) {
            var $buttonGroup = $(buttonGroup);
            $buttonGroup.on('click', 'button', function() {
                $buttonGroup.find('.active').removeClass('active');
                $(this).addClass('active');
            });
        });
    }
});



$(document).ready(function() {

    /*------------------------
    Back To Top
    --------------------------*/
    $('#back-to-top').fadeOut();
    $(window).on("scroll", function() {
        if ($(this).scrollTop() > 250) {
            $('#back-to-top').fadeIn(1400);
        } else {
            $('#back-to-top').fadeOut(400);
        }
    });
    // scroll body to 0px on click
    $('#top').on('click', function() {
        $('top').tooltip('hide');
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });


    /*------------------------
     Tooltip
    --------------------------*/
    $('[data-toggle="tooltip"]').tooltip()


    /*------------------------
     Sticky Header 
    --------------------------*/
    $(window).on('scroll', function() {
        if ($(this).scrollTop() > 100) {
            $('header').addClass('menu-sticky');
        } else {
            $('header').removeClass('menu-sticky');
        }
    });


    /*------------------------
    Menu Bar
    --------------------------*/
    jQuery('#menu-1').megaMenu({
        // DESKTOP MODE SETTINGS
        logo_align: 'left', // align the logo left or right. options (left) or (right)
        links_align: 'left', // align the links left or right. options (left) or (right)
        socialBar_align: 'left', // align the socialBar left or right. options (left) or (right)
        searchBar_align: 'right', // align the search bar left or right. options (left) or (right)
        trigger: 'hover', // show drop down using click or hover. options (hover) or (click)
        effect: 'fade', // drop down effects. options (fade), (scale), (expand-top), (expand-bottom), (expand-left), (expand-right)
        effect_speed: 400, // drop down show speed in milliseconds
        sibling: true, // hide the others showing drop downs if this option true. this option works on if the trigger option is "click". options (true) or (false)
        outside_click_close: true, // hide the showing drop downs when user click outside the menu. this option works if the trigger option is "click". options (true) or (false)
        top_fixed: false, // fixed the menu top of the screen. options (true) or (false)
        sticky_header: true, // menu fixed on top when scroll down down. options (true) or (false)
        sticky_header_height: 200, // sticky header height top of the screen. activate sticky header when meet the height. option change the height in px value.
        menu_position: 'horizontal', // change the menu position. options (horizontal), (vertical-left) or (vertical-right)
        full_width: true, // make menu full width. options (true) or (false)
        // MOBILE MODE SETTINGS
        mobile_settings: {
            collapse: true, // collapse the menu on click. options (true) or (false)
            sibling: true, // hide the others showing drop downs when click on current drop down. options (true) or (false)
            scrollBar: true, // enable the scroll bar. options (true) or (false)
            scrollBar_height: 400, // scroll bar height in px value. this option works if the scrollBar option true.
            top_fixed: false, // fixed menu top of the screen. options (true) or (false)
            sticky_header: true, // menu fixed on top when scroll down down. options (true) or (false)
            sticky_header_height: 200 // sticky header height top of the screen. activate sticky header when meet the height. option change the height in px value.
        }
    });



    /*------------------------
    Accordion
    --------------------------*/
    $('.iq-accordion .iq-accordion-block .iq-accordion-detail').hide();
    $('.iq-accordion .iq-accordion-block:first').addClass('ad-active').children().slideDown('slow');
    $('.iq-accordion .iq-accordion-block').on("click", function() {
        if ($(this).children('div').is(':hidden')) {
            $('.iq-accordion .iq-accordion-block').removeClass('ad-active').children('div').slideUp('slow');
            $(this).toggleClass('ad-active').children('div').slideDown('slow');
        }
    });



    /*------------------------
     Progress Bar
     --------------------------*/
    jQuery('.iq-progress-bar > span').each(function() {
        var jQuerythis = jQuery(this);
        var width = jQuery(this).data('percent');
        jQuerythis.css({
            'transition': 'width 2s'
        });
        setTimeout(function() {
            jQuerythis.appear(function() {
                jQuerythis.css('width', width + '%');
            });
        }, 500);
    });


    /*------------------------
    skrollr
    --------------------------*/
    skrollr.init({
        forceHeight: false
    });


    /*------------------------
    Magnific Popup
    --------------------------*/
    $('.popup-gallery').magnificPopup({
        delegate: 'a.popup-img',
        tLoading: 'Loading image #%curr%...',
        type: 'image',
        mainClass: 'mfp-img-mobile',
        gallery: {
            navigateByImgClick: true,
            enabled: true,
            preload: [0, 1]
        },
        image: {
            tError: '<a href="%url%">The image #%curr%</a> could not be loaded.'
        }
    });

    $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
        type: 'iframe',
        disableOn: 700,
        mainClass: 'mfp-fade',
        preloader: false,
        removalDelay: 160,
        fixedContentPos: false
    });


    /*------------------------
    counter
    --------------------------*/
    $('.timer').countTo();


    /*------------------------
    Screenshots silder
    --------------------------*/
    var slide = $('.slider-single');
    var slideTotal = slide.length - 1;
    var slideCurrent = -1;

    function slideInitial() {
        slide.addClass('proactivede');
        setTimeout(function() {
            slideRight();
        }, 500);
    }

    function slideRight() {
        if (slideCurrent < slideTotal) {
            slideCurrent++;
        } else {
            slideCurrent = 0;
        }

        if (slideCurrent > 0) {
            var preactiveSlide = slide.eq(slideCurrent - 1);
        } else {
            var preactiveSlide = slide.eq(slideTotal);
        }
        var activeSlide = slide.eq(slideCurrent);
        if (slideCurrent < slideTotal) {
            var proactiveSlide = slide.eq(slideCurrent + 1);
        } else {
            var proactiveSlide = slide.eq(0);

        }

        slide.each(function() {
            var thisSlide = $(this);
            if (thisSlide.hasClass('preactivede')) {
                thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
            }
            if (thisSlide.hasClass('preactive')) {
                thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
            }
        });
        preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
        activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
        proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
    }

    function slideLeft() {
        if (slideCurrent > 0) {
            slideCurrent--;
        } else {
            slideCurrent = slideTotal;
        }

        if (slideCurrent < slideTotal) {
            var proactiveSlide = slide.eq(slideCurrent + 1);
        } else {
            var proactiveSlide = slide.eq(0);
        }
        var activeSlide = slide.eq(slideCurrent);
        if (slideCurrent > 0) {
            var preactiveSlide = slide.eq(slideCurrent - 1);
        } else {
            var preactiveSlide = slide.eq(slideTotal);
        }
        slide.each(function() {
            var thisSlide = $(this);
            if (thisSlide.hasClass('proactivede')) {
                thisSlide.removeClass('preactive active proactive proactivede').addClass('preactivede');
            }
            if (thisSlide.hasClass('proactive')) {
                thisSlide.removeClass('preactivede preactive active proactive').addClass('proactivede');
            }
        });
        preactiveSlide.removeClass('preactivede active proactive proactivede').addClass('preactive');
        activeSlide.removeClass('preactivede preactive proactive proactivede').addClass('active');
        proactiveSlide.removeClass('preactivede preactive active proactivede').addClass('proactive');
    }

    var left = $('.slider-left');
    var right = $('.slider-right');
    left.on('click', function() {
        slideLeft();
    });
    right.on('click', function() {
        slideRight();
    });
    slideInitial();


    /*------------------------
    Owl Carousel
    --------------------------*/
    $('.owl-carousel').each(function() {
        var $carousel = $(this);
        $carousel.owlCarousel({
            items: $carousel.data("items"),
            loop: $carousel.data("loop"),
            margin: $carousel.data("margin"),
            nav: $carousel.data("nav"),
            dots: $carousel.data("dots"),
            autoplay: $carousel.data("autoplay"),
            autoplayTimeout: $carousel.data("autoplay-timeout"),
            navText: ['<i class="fas fa-chevron-left fa-2x"></i>', '<i class="fas fa-chevron-right fa-2x"></i>'],
            responsiveClass: true,
            responsive: {
                // breakpoint from 0 up
                0: {
                    items: $carousel.data("items-mobile-sm")
                },
                // breakpoint from 480 up
                480: {
                    items: $carousel.data("items-mobile")
                },
                // breakpoint from 786 up
                786: {
                    items: $carousel.data("items-tab")
                },
                // breakpoint from 1023 up
                1023: {
                    items: $carousel.data("items-laptop")
                },
                1199: {
                    items: $carousel.data("items")
                }
            }
        });
    });


    /*------------------------
    Contact From
    --------------------------*/
    $('#contact').submit(function(e) {

        var flag = 0;
        e.preventDefault(); // Prevent Default Submission
        $('.require').each(function() {
            if ($.trim($(this).val()) == '') {
                $(this).css("border", "1px solid red");
                e.preventDefault(); // Prevent Default Submission
                flag = 1;
            } else {
                $(this).css("border", "1px solid grey");
                flag = 0;
            }
        });

        if (flag == 0) {
            $.ajax({
                    url: 'php/contact-form.php',
                    type: 'POST',
                    data: $("#contact").serialize() // it will serialize the form data
                })
                .done(function(data) {
                    alert('Your Form is successfully Submited...');
                    $("#success").show();
                    $('#contact')[0].reset();
                })
                .fail(function() {
                    alert('Ajax Submit Failed ...');
                });
        }

    });

    
    /*---------------------------------------------------------------------
    Wow Animation
    -----------------------------------------------------------------------*/
    let wow = new WOW({
        boxClass: 'wow',
        animateClass: 'animated',
        offset: 0,
        mobile: false,
        live: true
    });
    wow.init();



});