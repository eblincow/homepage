

function showAbout() {
    $('li.selected').removeClass('selected');
    $('li.aboutlink').addClass('selected');
    $('.content').hide();
    $('#about').show();
    console.log("\nand you can sit and think about all those things");
    console.log("\nwhile sipping on whiskey and coke.");
}
function showLogin() {
    $('li.selected').removeClass('selected');
    $('li.loginlink').addClass('selected');
    $('.content').hide();
    $('#about').hide();
    $('#login').show();
    console.log("\n\nThis login feature sees about as much use as a snow-plough in Ecuador.");
}

function showContact() {
    $('li.selected').removeClass('selected');
    $('li.contactlink').addClass('selected');
    $('.content').hide();
    $('#about').hide();
    $('#contact').show();
}

function showPastWork() {
    $('li.selected').removeClass('selected');
    $('li.pastworklink').addClass('selected');
    $('.content').hide();
    $('#about').hide();
    $('#pastwork').show();
    console.log("\n\nStop looking in the goddamn console!");
}


$( document ).ready(function() {
    console.log("\nSometimes you say things in life you don't mean.");
    console.log("\nand ... it turns out there's no way to take them back.");


    $(".aboutlink").click(function(e) {
        e.preventDefault();
        showAbout();
    });
    $(".contactlink").click(function(e) {
        e.preventDefault();
        showContact();
    });
    $(".loginlink").click(function(e) {
        e.preventDefault();
        showLogin();
    });
    $(".pastworklink").click(function(e) {
        e.preventDefault();
        showPastWork();
    });


});