
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


# In[118]:


# import and initiate model
from sklearn.preprocessing import StandardScaler

X_scaler = StandardScaler().fit(X_train)


# In[119]:


X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# In[120]:


from keras.utils import to_categorical

y_train_categorical = to_categorical(y_train)
y_test_categorical = to_categorical(y_test)


# In[131]:


from keras.models import Sequential

model = Sequential()


# In[150]:


from keras.layers import Dense

number_inputs = 23
number_hidden_nodes = 100

model.add(Dense(units=number_hidden_nodes,
               activation='relu',input_dim=number_inputs))


# In[151]:


number_classes = 2
model.add(Dense(units=number_classes, activation='softmax'))


# In[152]:


model.summary()


# In[153]:


model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])


# In[154]:


model.fit(X_train_scaled,
          y_train_categorical,
          epochs=1000,
          shuffle=True,
          verbose=2
)


# In[146]:


model_loss, model_accuracy = model.evaluate(
    X_test_scaled, y_test_categorical, verbose=2)
print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")


# In[147]:


df_2018 = pd.read_csv('data/ML/2018_nba_stats_rs.csv')

X_2018 = df_2018.drop(['TEAM','GP','W','L'],axis=1)


# In[148]:


model.predict_classes(X_2018)


# In[149]:


model.predict(X_2018)

