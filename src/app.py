from flask import Flask, render_template, jsonify, request, redirect
from team_info import team_info

app = Flask(__name__)


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/team_info')
def team_stats():
	team_name = request.args.get('team_name', type=str)
	team_stats_dict = team_info(team_name)

	return jsonify(team_stats_dict)


# @app.route('/prediction_stats')
# def future():
# 	team_name = request.args.get('team_name', type=str)
#	future_stats_dict = finals(team_name)

#	return jsonify(future_stats_dict)


if __name__ == '__main__':
    app.run(debug=True)