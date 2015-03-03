// show and hide page elements
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
    console.log("\nStop looking in the goddamn console!");
}


function homepageJS() {
    // bind click handlers for links
    // to show and hide html
    $(document).ready(function () {
        console.log("\nSometimes you say things in life you don't mean.");
        console.log("\nand ... it turns out there's no way to take them back.");

        $(".aboutlink").click(function (e) {
            e.preventDefault();
            showAbout();
        });
        $(".contactlink").click(function (e) {
            e.preventDefault();
            showContact();
        });
        $(".loginlink").click(function (e) {
            e.preventDefault();
            showLogin();
        });
        $(".pastworklink").click(function (e) {
            e.preventDefault();
            showPastWork();
        });


    });
}


// loading and deferring
function defer(method) {
    // check for jquery, when loaded call method
    if (window.$)
        method();
    else
        setTimeout(function () {
            defer(method);
        }, 50);
}

function downloadJqueryAtOnload() {
    // defer certain images and download jquery
    var imgDefer = document.getElementsByTagName('img');
    for (var i = 0; i < imgDefer.length; i++) {
        if (imgDefer[i].getAttribute('data-src')) {
            imgDefer[i].setAttribute('src', imgDefer[i].getAttribute('data-src'));
        }
    }
    var element2 = document.createElement("script");
    element2.src = '/static/jquery-2.1.3.min.js';
    document.body.appendChild(element2);
    defer(homepageJS);
}

// onload, get jquery and switch image attributes
if (window.addEventListener)
    window.addEventListener("load", downloadJqueryAtOnload, false);
else if (window.attachEvent)
    window.attachEvent("onload", downloadJqueryAtOnload);
else window.onload = downloadJqueryAtOnload;
