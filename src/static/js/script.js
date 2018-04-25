var previousClass;

jQuery(function ($) {
    $('button').click(function () {
        console.log($(this).val())

        $('#team').removeClass(previousClass).addClass($(this).val())
        previousClass = $(this).val()
    })
});