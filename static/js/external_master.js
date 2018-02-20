$(document).ready(function() {
    $(".menu-tab").mouseenter(function(){
        $(this).find(".dropdown-content").css("display", "block");
        $(this).find(".menu-tab-title").css("color","#d36510");
        $(this).find(".arrow-up").show();
    })
    $(".menu-tab").mouseleave(function(){
        $(this).find(".dropdown-content").css("display", "none");
        $(this).find(".menu-tab-title").css("color","black");
        $(this).find(".arrow-up").hide();
    })
});