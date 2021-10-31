jQuery(document).ready(function ($) {
    $('.marquee-frame').marquee({duration: 10000, pauseOnHover: true});
    jQuery(".ap_header .bars").click(function () {
        jQuery(".ap_header").toggleClass("active");
        jQuery("#site-navigation").toggleClass("active");
    });
    jQuery('#close-btn').click(function () {
        jQuery('#search-overlay').fadeOut();
        jQuery(".ap").removeClass("open-overlay");
        jQuery('#search-btn').show();
    });
    jQuery('#search-btn').click(function () {
        jQuery(this).hide();
        jQuery('#search-overlay').fadeIn();
        jQuery(".ap").addClass("open-overlay");
    });
    $('.main-top .polist').slick({
        centerMode: false,
        adaptiveHeight: false,
        infinite: false,
        speed: 300,
        slidesToShow: 4,
        variableWidth: false,
        dots: false,
        rtl: true,
        nextArrow: '<i class="fa fa-chevron-top button-next"></i>',
        prevArrow: '<i class="fa fa-chevron-right button-prev"></i>',
        responsive: [{breakpoint: 728, settings: {centerPadding: false, slidesToShow: 1,}},]
    });
    $('.ap_slider').slick({
        infinite: true,
        speed: 300,
        autoplay: true,
        autoplaySpeed: 5000,
        slidesToShow: 1,
        centerMode: false,
        variableWidth: false,
        dots: false,
        rtl: true,
        nextArrow: '<i class="fa fa-chevron-left button-next"></i>',
        prevArrow: '<i class="fa fa-chevron-right button-prev"></i>',
        draggable: true,
        fade: true,
        cssEase: 'cubic-bezier(0.7, 0, 0.3, 1)',
        touchThreshold: 100
    });
    $('.ap_news .ne_four .polist').slick({
        centerMode: false,
        adaptiveHeight: false,
        infinite: false,
        speed: 300,
        slidesToShow: 3,
        variableWidth: false,
        dots: false,
        rtl: true,
        nextArrow: '<i class="fa fa-chevron-left button-next"></i>',
        prevArrow: '<i class="fa fa-chevron-right button-prev"></i>',
        responsive: [{breakpoint: 450, settings: {centerPadding: false, slidesToShow: 1,}},]
    });
    $('.sidebar .ne_four .polist').slick({
        centerMode: false,
        adaptiveHeight: false,
        infinite: false,
        speed: 300,
        slidesToShow: 1,
        variableWidth: false,
        dots: false,
        rtl: true,
        nextArrow: '<i class="fa fa-chevron-left button-next"></i>',
        prevArrow: '<i class="fa fa-chevron-right button-prev"></i>',
    });
    $('.timeline .polist').slick({
        infinite: false,
        speed: 300,
        autoplay: false,
        dots: false,
        vertical: true,
        slidesToShow: 8,
        slidesToScroll: 1,
        verticalSwiping: false,
        nextArrow: '<i class="fa fa-chevron-up button-next"></i>',
        prevArrow: '<i class="fa fa-chevron-down button-prev"></i>',
    });
    var min = 8;
    var max = 40;
    var reset = $('p').css('fontSize');
    var elm = $('.entry');
    var size = str_replace(reset, 'px', '');
    $('.plustext').click(function () {
        if (size <= max) {
            size++;
            elm.css({'fontSize': size});
        }
        return false;
    });
    $('.minustext').click(function () {
        if (size >= min) {
            size--;
            elm.css({'fontSize': size});
        }
        return false;
    });

    function str_replace(haystack, needle, replacement) {
        var temp = haystack.split(needle);
        return temp.join(replacement);
    }

    $(".info-txt").hover(function () {
        h1 = parseInt($(this).find(".info-txt-titre").width());
        h2 = parseInt($(this).find("a").width());
        rightAnimation = (h1 - h2) + 45;
        leftAnimation = (h1 - h2) + 45;
        if (rightAnimation <= 45) {
            $(this).find(".info-txt-titre").stop().animate({right: rightAnimation}, 1400);
        }
        $(".info-txt").stop().animate({opacity: 0.4}, 200);
        $(this).stop().animate({opacity: 1}, 200);
    }, function (event) {
        var direction;
        $(this).find(".info-txt-titre").stop().animate({right: "55px"}, 1400);
        $(".info-txt").stop().animate({opacity: 1}, 200);
    });
});
$(window).scroll(function () {
    if ($(this).scrollTop() > 200) {
        $('.go-top').fadeIn(200);
    } else {
        $('.go-top').fadeOut(200);
    }
});
$('.go-top').click(function (event) {
    event.preventDefault();
    $('html, body').animate({scrollTop: 0}, 300);
})


function openNav() {
    document.getElementById("mySidenav").style.width = "300px";
    document.getElementById("main-re").style.marginLeft = "240px";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
    document.getElementById("main-re").style.marginLeft = "0";
}


/*------------ map ------------*/
$(function () {

    $("#IranMap svg g path").hover(function () {
        var c = $(this).attr("data-title");
        $('#IranMap .show-title').hide();
        $('#IranMap .show-title').html(c);
        $('#IranMap .show-title').fadeIn(200);
    }, function () {
        $('#IranMap .show-title').html("").css({
            display: "none"
        })
    });

    $("#IranMap").mousemove(function (d) {
        var c = 0;
        var h = 0;
        if (!d) {
            var d = window.event
        }
        if (d.pageX || d.pageY) {
            c = d.pageX;
            h = d.pageY
        } else {
            if (d.clientX || d.clientY) {
                c = d.clientX + document.body.scrollLeft + document.documentElement.scrollLeft;
                h = d.clientY + document.body.scrollTop + document.documentElement.scrollTop
            }
        }
        if ($("#IranMap .show-title").html()) {
            var f = $(this).offset();
            var b = (c - f.left + 25) + "px";
            var g = (h - f.top - 5) + "px";
            $("#IranMap .show-title").css({
                left: b,
                top: g
            })
        }
    });


});

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
        }
    }
}


$(document).ready(function () {
    document.cookie = 'name=alireza';
    console.log(document.cookie);

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');


    $("#IranMap svg g path").click(function () {


        if ($(this).attr("data-active") != "active") {
            var cityid;
            var city = $(this).attr("class");

            cityid = $(this).attr("cityid");
            $(".city-posts .posts").addClass("disable");
            $(".city-posts .more").addClass("disable");
            $(".city-posts h2").addClass("disable");
            $.ajax({
                url: '',
                type: 'post',
                data: {
                    text: $(this).text(),
                    cat: cityid,
                    ppp: 4,
                    csrfmiddlewaretoken: csrftoken,
                },
                success: function (post) {
                    $(".city-posts .posts").removeClass("disable");
                    $(".city-posts .more").removeClass("disable");
                    $(".city-posts h2").removeClass("disable");
                    $(".city-posts").empty();
                    $(".city-posts").append(post);
                },
            })

            // $.post(ajaxUrl, {
            //     action: "map_post_ajax",
            //     ppp: 4,
            //     cat: cityid
            // }).success(function (posts) {
            //     $(".city-posts .posts").removeClass("disable");
            //     $(".city-posts .more").removeClass("disable");
            //     $(".city-posts h2").removeClass("disable");
            //     $(".city-posts").empty();
            //     $(".city-posts").append(posts);
            //
            // });

        }
    });


});


