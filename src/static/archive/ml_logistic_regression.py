
import pandas as pd


# In[175]:


df = pd.read_csv('data/ML/comp_nba_stats_rs.csv')
df_ = df.drop(['TEAM','GP','W','L'],axis=1)
# In[256]:
counter = 0

# iterate through each season
# for year in range(1997,2018):
#     counter += 1
#     temp_df = df_.loc[df_['SEASON'] == year]
    
#     season_df = temp_df['SEASON']
#     champion_df = temp_df['CHAMPION'].reset_index(drop=True)
    
#     # pull feature data
#     normalize_df = temp_df.drop(columns=['SEASON','CHAMPION'])
    
#     # normalize using sklearn's normalize() function, axis=0 to normalize across columns
#     normalization_df = pd.DataFrame(normalize(normalize_df, axis=0))
    
#     # combine features and outcomes ['CHAMPION']
#     final_df = pd.concat([normalization_df,champion_df],axis=1)
    
#     if counter == 1:
#         normalized_df = final_df
#     else:
#         normalized_df = pd.concat([normalized_df,final_df])

# features = normalized_df.drop(columns=['CHAMPION']).reset_index(drop=True)
# champions = normalized_df['CHAMPION'].reset_index(drop=True)

# overall_normalized_features = pd.DataFrame(normalize(features,axis=0))

# ultimate_df = pd.concat([overall_normalized_features,champions],axis=1)

# Split your features and outcomes
X = df_.drop(['CHAMPION','SEASON'],axis=1)
y = df_['CHAMPION']


# In[266]:


# import and then train_test_split, stratify=y to make sure there is even distribution of outcomes
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=20, stratify=y)


# In[267]:


# import and initiate model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(max_iter=1000)


# In[268]:


# fit training data
classifier.fit(X_train,y_train)


# In[275]:


# print scores
print('train score:',classifier.score(X_train,y_train))
print('test score:',classifier.score(X_test,y_test))


# In[271]:


# make predictions
predictions = classifier.predict(X_test)
predictions_list = list(predictions)

pd.DataFrame({"Prediction": predictions, "Actual": y_test}).to_csv('predictions.csv')


# In[273]:


# import 2018 stats
df_2018 = pd.read_csv('data/ML/2018_nba_stats_rs.csv')

X_2018 = df_2018.drop(['TEAM','GP','W','L'],axis=1)


# In[274]:


# output probabilities
classifier.predict_proba(X_2018)




# In[29]:


probabilities = []

for row in classifier.predict_proba(X_2018):
    probabilities.append(row[1])


# In[30]:


probabilities


# In[31]:


teams = df_2018['TEAM']


# In[32]:


results = pd.DataFrame({'TEAM':teams,'PROBABILITY':probabilities})


# In[33]:


results.sort_values('PROBABILITY',ascending=False)

