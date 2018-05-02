import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

############## pulling abbreviations using splinter ###############

from bs4 import BeautifulSoup as bs
import requests

url = 'https://en.wikipedia.org/wiki/Wikipedia:WikiProject_National_Basketball_Association/National_Basketball_Association_team_abbreviations'

team_abr = {}
response = requests.get(url)
soup = bs(response.text, 'html.parser')
table = soup.find_all('tr')
counter = 0

for row in table:
    counter += 1
    
    if counter != 1:
        if row.a.text == 'Los Angeles Clippers':
            team_abr['LA Clippers'] = row.td.text
        else:
            team_abr[row.a.text] = row.td.text



############## random forest model with 2018 predictions and probabilities ###############

def finals():
	df = pd.read_csv('static/data/ML/comp_nba_stats_rs.csv')
	df_ = df.drop(['TEAM', 'GP', 'MIN'],axis=1)

	# Split your features and outcomes
	X = df_.drop(['CHAMPION','SEASON'],axis=1)
	y = df_['CHAMPION']

	# import and then train_test_split, stratify=y to make sure there is even distribution of outcomes

	X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

	rf = RandomForestClassifier(n_estimators=300)
	rf = rf.fit(X_train,y_train)


	results = {'model_mean_accuracy': float("{:.4f}".format(rf.score(X_test,y_test)))}
	results['feature_importance'] = sorted(zip([float("{:.4f}".format(feat)) for feat in rf.feature_importances_],X.columns), reverse=True)

	complete_2018 = pd.read_csv('static/data/regular_season/2018_nba_stats_rs.csv')

	X_2018 = pd.read_csv('static/data/regular_season/2018_nba_stats_rs.csv')
	X_2018.drop(['TEAM', 'GP', 'MIN'], axis=1, inplace=True)


	results['team_prediction'] = sorted(zip([float("{:.4f}".format(perc[1])) for perc in rf.predict_proba(X_2018).tolist()], rf.predict(X_2018).tolist(), complete_2018['TEAM'].tolist(),[team_abr[team] for team in complete_2018['TEAM'].tolist()]), reverse=True)

	return(results)
