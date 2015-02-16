

function showAbout() {
    $('li.selected').removeClass('selected');
    $('li.aboutlink').addClass('selected');
    $('.content').hide();

    $('#about').show();
}
function showLogin() {
    $('li.selected').removeClass('selected');
    $('li.loginlink').addClass('selected');
    $('.content').hide();
    $('#about').hide();
    $('#login').show();
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
}


$( document ).ready(function() {
    console.log( "Dont have your console open while looking at my webpage, fool!" );
    console.log("\nLook, I didn't mean it like that. Sometimes the things I say just get taken out of context.");
    console.log("\nDon't be like that. ");
    console.log("\nLets start over, can we?");
    console.log("\nSometimes you say things in life you don't mean.");
    console.log("\nand ... it turns out there's no way to take them back.");
    console.log("\nand you can sit and think about all those things");
    console.log("\nwhile sipping on whiskey and coke.");
    //<li class="aboutlink selected">about</li>
    //<li class="pastworklink">past work</li>
    //<li class="contactlink">contact</li>
    //<li class="loginlink">client login</li>)
    $('.aboutlink').onclick

    $(".aboutlink").click(function() {
        showAbout();
    });
    $(".contactlink").click(function() {
        showContact();
    });
    $(".loginlink").click(function() {
        showLogin();
    });
    $(".pastworklink").click(function() {
        showPastWork();
    });


});