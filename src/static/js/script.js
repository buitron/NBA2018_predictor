var previousClass;

jQuery(function ($) {
    $('.btn').click(function () {

        $('#team').removeClass(previousClass).addClass($(this).val());
        previousClass = $(this).val();

    	$.getJSON($SCRIPT_ROOT + '/team_info', {
        	team_name: $(this).val()
        }, function(data) {

            $('.lead').hide();
            $('#team_name').text(data.Team);

            $('#team_table').removeAttr('hidden');
            $('#playoff_seed').text(data['Playoff Seed']);
            $('#conference').text(data.Conference);
            $('#division').text(data.Division);
            $('#head_coach').text(data['Head Coach']);
            $('#star_player').text(data['Star Player']);
            $('#rs_season_wins').text(data['Regular Season Wins']);
            $('#rs_season_losses').text(data['Regular Season Losses']);
            $('#win_percentage').text(data['Win Percentage']);
            $('#points_per_game').text(data['Points Per Game']);
            $('#field_goal_percentage').text(data['Field Goal Percentage']);
            $('#free_throw_percentage').text(data['Free Throw Percentage']);
            $('#three_point_percentage').text(data['Three Point Percentage']);
            $('#assists_per_game').text(data['Assists Per Game']);
            $('#blocks_per_game').text(data['Blocks Per Game']);
            $('#rebounds_per_game').text(data['Rebounds Per Game']);
            $('#steals_per_game').text(data['Steals Per Game']);

            $('#team_fact').text(data['Team Fact']);


        })

        $.getJSON($SCRIPT_ROOT + '/prediction_stats', {
        }, function(data) {

            $('#team_predict').removeAttr('hidden');

            var counter = 0;
            data['team_prediction'].forEach(function(element) {
                counter ++;
                if (element[3] == previousClass) {
                    $('#champion').text(element[1]);
                    $('#predict_perc').text(element[0]);
                    $('#ranked').text(counter);

                }
            })
        })
    })
});