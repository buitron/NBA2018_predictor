from flask import Flask, render_template, jsonify
from team_info import team_info

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/team_info/<team_abbrev>', methods=['POST'])
if request.method == 'POST':
	team_name = request.form['team_name']
	# team_abbrev = team_name.val()

def team_stats(team_abbrev):

    team_stats_dict = team_info(team_abbrev)

    return jsonify(team_stats_dict[0])

if __name__ == '__main__':
    app.run(debug=True)