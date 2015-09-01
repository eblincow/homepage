// show and hide page elements
function showAbout() {
    $('li.selected').removeClass('selected');
    $('li.aboutlink').addClass('selected');
    $('.content').hide();
    $('#about').show();
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


function homepageJS() {
    // bind click handlers for links
    // to show and hide html
    $(document).ready(function () {

        $(".aboutlink").click(function (e) {
            e.preventDefault();
            showAbout();
        });
        $(".contactlink").click(function (e) {
            e.preventDefault();
            showContact();
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
