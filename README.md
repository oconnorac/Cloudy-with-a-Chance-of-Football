# Cloudy with a Chance of Football

Griffin, Ermina, Yaphet, and Aidan's capstone project for the Certificate of Data Science at the Georgetown University School of Continuing Studies (Cohort 23, Spring - Summer 2021).

![Image](fixtures/images/fantasy_football_image.png)

## Description

Fantasy football allows fans to act as team managers by drafting, trading for, acquiring, and playing real football players in on fantasy football platforms, scoring points using a scoring system based on real life performance of their players. Fantasy football platforms (such as [ESPN](https://www.espn.com/fantasy/football/) or [Yahoo!](https://football.fantasysports.yahoo.com/)) apply their own analytics to project player performance weekly during the NFL season in preparation for the upcoming week. It is not uncommon for players to score well above or far below their platform-projected fantasy score, leaving fantasy managers wondering which players to draft, trade for, acquire, and play.

We want to know what influences a player's *actual* fantasy score so that we can make data-driven decisions when building a team or weekly starting lineup during the NFL season. To do so, we're using 2019 and 2020 NFL season data and ESPN fantasy football projection data for this project.

## Data Sourcing

Fantasydata.com
Nflsavant.com
Pro-football-reference.com

## Data Architecture

Talk about the structure of the data

## Machine Learning

We intend to use a classification model with a 80/20 train/test split to determine whether or not a player will perform above or below the projected fantasy points. Critical to this model is engineering binary features to complement the numeric features we have found, and fine-tuning parameters to make the model account for complexities in the selected features, but flexible enough to take in 2021 fantasy projections and help fantasy managers to decide who to draft, start, trade for, and pick up off of the waiver wire.

Our intent is to deploy our trained model to a web application that requests basic user input and takes certain features into account to provide a prediction (which could be taken as a recommendation) about a player’s performance in the coming week.

## Limitations and Areas for Future Study

Write a little bit about our limitations in conduting this project and areas where this research can be added to

## Conclusion
 
 Write a project conclusion
 
## Acknowledgements
 
Thanks to kaggle user Chris Murphy for the use of his data [https://www.kaggle.com/mur418/espn-2019-stats-and-2020-nfl-fantasy-projections]

## References

Provide reference material
