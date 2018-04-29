import datetime
import requests
import time


def now_playing():
    now = datetime.datetime.now()
    today = now.strftime("%Y%m%d")
    url = f"http://data.nba.net/10s/prod/v1/{today}/scoreboard.json"

    while True:
        req = requests.get(url)
        if req.status_code == 200:
            data = req.json()

            live_game = []
            for game in data['games']:
                game_duration = "{}hrs, {}min".format(game['gameDuration']['hours'], game['gameDuration']['minutes'])
                game_clock = game['clock']
                game_date = game['startDateEastern']
                game_time = game['startTimeEastern']

                playoffs = game['playoffs']
                game_num = playoffs['gameNumInSeries']
                series_sum = playoffs['seriesSummaryText']

                hometeam = game['hTeam']
                hometeam_name = hometeam['triCode']
                hometeam_score = hometeam['score']

                awayteam = game['vTeam']
                awayteam_name = awayteam['triCode']
                awayteam_score = awayteam['score']

                live = {}

                if game_clock != '':
                    live["game_clock"] = game_clock
                
                if game_duration != 'hrs, min':
                    live["game_duration"] = game_duration
                else:
                    live["game_date"] = game_date
                    live["game_time"] = game_time

                live["game_number"] = game_num
                live["series_leader"] = series_sum
                live["hometeam_abbrev"] = hometeam_name
                live["hometeam_score"] = hometeam_score
                live["awayteam_abbrev"] = awayteam_name
                live["awayteam_score"] = awayteam_score

                live_game.append(live)

        else:
            # save N/A to variables and print a 'sorry message'
            print('pinging is not allowed, status_code: ', req.status_code)
            live_game[0] = "Sorry hommie, live stream is temporarily down."

        return live_game
    time.sleep(60 * 5)


