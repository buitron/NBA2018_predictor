## NBA Champion Forecaster

<p align="center">
    <img src="https://media.giphy.com/media/6HXQPVYGQwJEs/giphy.gif" alt="Slam DUNK (via GIPHY)">
</p>


# Objective

Predict the NBA Championship Team for 2018 using a fine tuned Machine Learning Algorithm, and project it to the user on an easily digestable UI web application.


# Background

We scraped 21 years worth of regular season NBA team stats data, starting at 1997, from stats.nba.com, which we used as test features in our ML model. We also appended a boolean label column to this dataset with the winning or losing team for that particular season. With this data we were able to produce most of the hard working functionalities of this application, the rest is mumbo jumbo (for those that like that kinda stuff, we ain't judging).


## Step 1 - Data Gathering and Cleaning

* Data was collected from <a href="https://stats.nba.com/">stats.nba.com</a>
* The endpoint http://data.nba.net/10s/prod/v1/{today}/scoreboard.json
* Engineered a SqlLite data file with playoff team stats and historical information


## Step 2 - ML Model Build

We tested various ML algorithms for best fit. Random Forests proved to be the best model for this type of classification problem. Below are our Jupyter Notebook coding blocks showing the how we produced our model and the metrics that show the strength in fit.

<p align="center">
    <img src="images/notebook_1.png" alt="jupyter notebook 1">
</p>
<p align="center">
    <img src="images/notebook_2.png" alt="jupyter notebook 2">
</p>
<p align="center">
    <img src="images/notebook_3.png" alt="jupyter notebook 3">
</p>


## Step 3 - Flask

The Python Flask Module allowed us to create multiple data API endpoints so that we could pull in both static and live data into our application. We also utilized a Flask + Jquery Javascript functionality that transformed our team labeled buttons into RESTful input POSTs. And then PRESTO, our app was born.


## Step 4 - Hosting

This application is being hosted on Heroku. To veiw the app and possibly place a bet before the 2018 NBA series is over (disclosure: we aren't liable for any of your loses, gamble at your own discretion) - [*CLICK HERE*](https://nba-champion.herokuapp.com/) !


# Sample Web-app

![webpage image 1](images/webpage_1.png)
![webpage image 2](images/webpage_2.png)
![webpage image 3](images/webpage_3.png)
![webpage image 4](images/webpage_4.png)
![webpage image 5](images/webpage_5.png)
