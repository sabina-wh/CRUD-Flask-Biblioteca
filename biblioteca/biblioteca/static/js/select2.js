$(document).ready(function() {
    if ($.fn.select2) {
        $('.js-example-basic-multiple').select2();
    } else {
        console.error("Select2 no está cargado.");
    }
});