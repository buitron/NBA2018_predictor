var previousClass;

jQuery(function ($) {
    $('.btn').click(function () {
        console.log($(this).val())

        $('#team').removeClass(previousClass).addClass($(this).val())
        previousClass = $(this).val()

    	$.getJSON($SCRIPT_ROOT + '/team_info', {
        	team_name: $(this).val()
        }, function(data) {

        	// place to change Team Information



        	console.log(data)
        })
    })
});