## NBA Champion Forecaster

<p align="center">
    <img src="https://media.giphy.com/media/6HXQPVYGQwJEs/giphy.gif" alt="Slam DUNK (via GIPHY)">
</p>


# Objective

Predict the NBA Championship Team for 2018 using a fine tuned Deep Learning Algorithm, and project it to the user on an easily digestable UI web application.


# Background

[NBA Stats info and years the data is collected]


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

Used various


## Step 4 - Application Build


# Sample Web-app

<img src="images/webpage_1.png" alt="webpage image 1">
<img src="images/webpage_2.png" alt="webpage image 2">
<img src="images/webpage_3.png" alt="webpage image 3">
<img src="images/webpage_4.png" alt="webpage image 4">
<img src="images/webpage_5.png" alt="webpage image 5">
