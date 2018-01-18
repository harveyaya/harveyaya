$(document).ready(function() {
    var timer = null;
    $('.body-screen').mouseenter(function(){
        restBodyScreen = $(this).parent().children().not(this);
        restBodyScreen.find(".selectedImg").hide();
        restBodyScreen.find(".unselectedImg").show();
        restBodyScreen.find(".body-screen-title").hide();
        $(this).find(".unselectedImg").hide();
        $(this).animate({
            width: "85%"
        }, 200 );
        restBodyScreen.animate({
            width: "5%"
        }, 200 );
        $(this).find(".selectedImg").show();
        $(this).find(".body-screen-title").show();
        $(this).addClass("body-screen-background");
    });

    $(".web-header,.web-footer").mouseenter(function(element){
        $(".selectedImg").hide();
        $(".unselectedImg").show();
        $(".body-screen-title").show();
        $(".body-screen").removeClass("body-screen-background");
        $(".body-screen").css("width", "25%");
        // Timeout 200ms is for animation to be finished in mouseenter event.
        // without setTimeout, command above won't change width.
        setTimeout(function(){
            $(".body-screen").css("width", "25%");
        },200);
    })
});