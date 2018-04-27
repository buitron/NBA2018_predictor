
# coding: utf-8

# In[19]:


import pandas as pd


# In[21]:


df = pd.read_csv('data/ML/comp_nba_stats_rs.csv')
df_ = df.drop(['TEAM','GP','W','L'],axis=1)

# Split your features and outcomes
X = df_.drop(['CHAMPION','SEASON'],axis=1)
y = df_['CHAMPION']


# In[35]:


len(list(X.columns))


# In[117]:


# import and then train_test_split, stratify=y to make sure there is even distribution of outcomes
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20, stratify=y)


# In[156]:


from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=200)
rf = rf.fit(X_train,y_train)
rf.score(X_test,y_test)


# In[159]:

sorted(zip(rf.feature_importances_,X.columns),reverse=True)

# In[164]:

rf.predict_proba(X_2018)


# In[166]:

probabilities = []

for row in rf.predict_proba(X_2018):
    probabilities.append(row[1])

df_2018 = pd.read_csv('data/ML/2018_nba_stats_rs.csv')
X_2018 = df_2018.drop(['TEAM','GP','W','L'],axis=1)

# In[167]:


teams = df_2018['TEAM']


# In[169]:
results = pd.DataFrame({'TEAM':teams,'PROBABILITY':probabilities})
results.sort_values('PROBABILITY',ascending=False)

