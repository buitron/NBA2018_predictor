import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect
from sqlalchemy import func

engine = create_engine("sqlite:///static/data/team_info/team_info.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Team_info = Base.classes.team_info
session = Session(engine)

def team_info(team):
	team = team.replace("_", " ")
	queryExpression = session.query(Team_info.team
                            ,Team_info.conference
                            ,Team_info.division
                            ,Team_info.star_player
                            ,Team_info.head_coach
                            ,Team_info.playoff_seed
                            ,Team_info.regular_season_wins
                            ,Team_info.regular_season_losses
                            ,Team_info.win_percentage
                            ,Team_info.points_per_game
                            ,Team_info.field_goal_percentage
                            ,Team_info.three_point_percentage
                            ,Team_info.free_throw_percentage
                            ,Team_info.rebounds_per_game
                            ,Team_info.assists_per_game
                            ,Team_info.steals_per_game
                            ,Team_info.blocks_per_game
	).filter(Team_info.team == team).all()

	Team_info_dict = [{"Team": each[0],
	"Conference": each[1],
	"Division": each[2],
	"Star Player": each[3],
	"Head Coach": each[4],
	"Playoff Seed": each[5],
	"Regular Season Wins": each[6],
	"Regular Season Losses": each[7],
	"Win Percentage": float('{:2f}'.format(each[8])),
	"Points Per Game": each[9],
	"Field Goal Percentage": each[10],
	"Three Point Percentage": each[11],
	"Free Throw Percentage": each[12],
	"Rebounds Per Game": each[13],
	"Assists Per Game": each[14],
	"Steals Per Game": each[15],
	"Blocks Per Game": each[16]
	} for each in queryExpression]

	return Team_info_dict