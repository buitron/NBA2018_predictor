var previousClass;

jQuery(function ($) {
    $('.team_btn').click(function () {

        $('#team').removeClass(previousClass).addClass($(this).val());
        previousClass = $(this).val();

        location.href = "#about"

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

        // prediction section

        $.getJSON($SCRIPT_ROOT + '/prediction_stats', {
        }, function(data) {

            $('#team_predict').removeAttr('hidden');

            var counter = 0;
            data['team_prediction'].forEach(function(element) {
                counter ++;

                console.log(element)

                if (element[3] == previousClass) {
                    $('#champion').text(element[1]);
                    $('#predict_perc').text(element[0]);
                    $('#ranked').text(counter);

                    team_id = '#' + element[3];

                    document.getElementById(element[3]).style.fontSize = "11px";
                    document.getElementById(element[3]).style.fontWeight = "700";

                    // d3 percent circle

                    $('#circle').remove()
                    var circle = "circle"

                    var duration = 1500,
                        transition = 200,
                        percent = element[0] * 100,
                        width = window.innerWidth - 800,
                        height = window.innerHeight - 600;

                    var dataset = {
                                lower: calcPercent(0),
                                upper: calcPercent(percent)
                            },
                            radius = Math.min(width, height) / 2,
                            pie = d3.layout.pie().sort(null),
                            format = d3.format(".0%");

                    var arc = d3.svg.arc()
                            .innerRadius(radius * .8)
                            .outerRadius(radius);

                    var svg = d3.select("#perc_circle").append("svg")
                            .attr("id", circle)
                            .attr("width", width)
                            .attr("height", height)
                            .append("g")
                            .attr("transform", "translate(" + width / 5 + "," + height / 2 + ")");

                    var path = svg.selectAll("path")
                                    .data(pie(dataset.lower))
                                    .enter().append("path")
                                    .attr("class", function (d, i) {
                                        return "color" + i
                                    })
                                    .attr("d", arc)
                                    .each(function (d) {
                                        this._current = d;
                                    });

                    var text = svg.append("text")
                            .attr("text-anchor", "middle")
                            .attr("dy", ".3em");

                    var progress = 0;

                    var timeout = setTimeout(function () {
                        clearTimeout(timeout);
                        path = path.data(pie(dataset.upper));
                        path.transition().duration(duration).attrTween("d", function (a) {
                            var i = d3.interpolate(this._current, a);
                            var i2 = d3.interpolate(progress, percent)
                            this._current = i(0);
                            return function (t) {
                                text.text(format(i2(t) / 100));
                                return arc(i(t));
                            };
                        });
                    }, 200);

                    function calcPercent(percent) {
                        return [percent, 100 - percent];
                    };


                }
            })
        })
    })
});

$('#myModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

