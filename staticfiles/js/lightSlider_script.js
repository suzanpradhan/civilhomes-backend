// JavaScript Document
 $(document).ready(function() {
    $('#autoWidth').lightSlider({
        autoWidth:true,
        loop:true,
        onSliderLoad: function() {
            $('#autoWidth').removeClass('cS-hidden');
        } 
    });  
    $('#companiesSlider').lightSlider({
        autoWidth:true,
        loop:true,
        speed: 400, //ms'
        auto: true,
        pauseOnHover: true, 
        pager:false,
        slideEndAnimation: true,
        pause: 2000,
        onSliderLoad: function() {
            $('#companiesSlider').removeClass('cS-hidden');
        } 
    });  
  });