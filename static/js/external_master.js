$(document).ready(function() {
    $(".menu-tab").mouseenter(function(){
        $(this).find("a").css("color","#d36510");
        $(this).find(".arrow-up").show();

    })
    $(".menu-tab").mouseleave(function(){
        $(this).find("a").css("color","black");
        $(this).find(".arrow-up").hide();
    })
});