import datetime
import requests


now = datetime.datetime.now()
today = now.strftime("%Y%m%d")
url = f"http://data.nba.net/10s/prod/v1/{today}/scoreboard.json"


req = requests.get(url)
if req.status_code == 200:
    data = req.json()

    for game in data['games']:
        game_duration = "{}hrs, {}min".format(game['gameDuration']['hours'], game['gameDuration']['minutes'])
        game_clock = game['clock']

        playoffs = game['playoffs']
        game_num = playoffs['gameNumInSeries']
        series_sum = playoffs['seriesSummaryText']

        hometeam = game['hTeam']
        hometeam_name = hometeam['triCode']
        hometeam_score = hometeam['score']

        awayteam = game['vTeam']
        awayteam_name = awayteam['triCode']
        awayteam_score = awayteam['score']


        # print variables to console for testing
        print("-" * 40)
        if game_clock != '':
            print("game clock:", game_clock)
        else:
            print("game duration:", game_duration)

        print("game number:", game_num)
        print("series leader:", series_sum)
        print("hometeam abbreviation:", hometeam_name + ", hometeam score: ", hometeam_score)
        print("awayteam abbreviation:", awayteam_name + ", awayteam score: ", awayteam_score)
else:
    # save N/A to variables and print a 'sorry message'
    print('pinging is not allowed, status_code: ', req.status_code)

