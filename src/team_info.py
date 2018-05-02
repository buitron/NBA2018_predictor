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
	queryExpression = session.query(Team_info.team_abbrev
							,Team_info.team
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
                            ,Team_info.team_fact
	).filter(Team_info.team_abbrev == team).all()

	Team_info_dict = [{"Team": each[1],
	"Conference": each[2],
	"Division": each[3],
	"Star Player": each[4],
	"Head Coach": each[5],
	"Playoff Seed": each[6],
	"Regular Season Wins": each[7],
	"Regular Season Losses": each[8],
	"Win Percentage": float('{:.2f}'.format(each[9] * 100)),
	"Points Per Game": each[10],
	"Field Goal Percentage": each[11],
	"Three Point Percentage": each[12],
	"Free Throw Percentage": each[13],
	"Rebounds Per Game": each[14],
	"Assists Per Game": each[15],
	"Steals Per Game": each[16],
	"Blocks Per Game": each[17],
	"Team Fact": each[18]
	} for each in queryExpression]

	return Team_info_dict[0]