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

if(document.getElementById("gmap")){
        var locations = [
            ['<div class="location_details"><b>Head Office</b><br/> 54 Hassan el mamoon st, Nasr City,<br />Cairo, Egypt<br/>info@hdlegypt.com<br/> 01208886888 </div>', 30.0628291, 31.3560101],
        ];
        var mapDiv = document.getElementById('gmap');
        var map = new google.maps.Map(mapDiv, {
            center: {lat: 30.0628291, lng: 31.3560101},
            zoom: 16
        });
        var infowindow = new google.maps.InfoWindow();
        var marker;
        var i;

        for (i = 0; i < locations.length; i++) {
             marker = new google.maps.Marker({
                position: new google.maps.LatLng(locations[i][1], locations[i][2]),
                map: map
            });
            google.maps.event.addListener(marker, 'click', (function(marker, i) {
                return function() {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
          })(marker, i));
        }
    }
