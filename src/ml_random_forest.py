import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier


df = pd.read_csv('static/data/ML/comp_nba_stats_rs.csv')
df_ = df.drop(['TEAM', 'GP', 'MIN'],axis=1)

# Split your features and outcomes
X = df_.drop(['CHAMPION','SEASON'],axis=1)
y = df_['CHAMPION']

# import and then train_test_split, stratify=y to make sure there is even distribution of outcomes

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

rf = RandomForestClassifier(n_estimators=1000)
rf = rf.fit(X_train,y_train)


results = {'model_mean_accuracy': rf.score(X_test,y_test)}
results['feature_importance'] = sorted(zip(rf.feature_importances_,X.columns),reverse=True)

complete_2018 = pd.read_csv('static/data/regular_season/2018_nba_stats_rs.csv')

X_2018 = pd.read_csv('static/data/regular_season/2018_nba_stats_rs.csv')
X_2018.drop(['TEAM', 'GP', 'MIN'], axis=1, inplace=True)

results['team_prediction'] = sorted(zip(complete_2018['TEAM'].tolist(), rf.predict(X_2018).tolist(), [perc[1] for perc in rf.predict_proba(X_2018).tolist()]))

# results['prediction'] = rf.predict(X_2018).tolist()
# results['prediction_probability'] = [perc[1] for perc in rf.predict_proba(X_2018).tolist()]

print(results)

