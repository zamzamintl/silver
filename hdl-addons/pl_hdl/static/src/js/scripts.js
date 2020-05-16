    var headerHeight = $('header').outerHeight()
//    var headerHeight = $('.top-header').outerHeight();
    $(window).on("scroll", function() {
    if($(window).scrollTop() > 10) {
        $("header").addClass("sticky");
    } else {
        //remove the background property so it comes transparent again (defined in your css)
       $("header").removeClass("sticky");
    }
});
    $(window).on("scroll", function() {
    if($(window).scrollTop() > 500) {
        $(".scroll_top_btn").addClass("display_btn");
    } else {
        //remove the background property so it comes transparent again (defined in your css)
       $(".scroll_top_btn").removeClass("display_btn");
    }
});
