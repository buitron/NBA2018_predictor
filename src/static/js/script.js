jQuery(function ($) {
    $('button').click(function () {
        console.log($('#filterDay input:radio:checked').val())
        console.log($('#filterDay label.active input').val())
    })
});