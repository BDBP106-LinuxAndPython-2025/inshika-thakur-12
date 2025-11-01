#!/usr/bin/python3

"""(2) Read the file ODI-Batting Cricket Analytics.json in pandas using
pandas.read_json(<filename>) syntax. Then do the following:"""

"""a.) Display the column names"""
import pandas as pd
file=pd.read_json('ODI-Batting_Cricket_Analytics(1).json')
print(f'a.) The column names as given in the files are: ',list(file.columns))
print(f"=============================================================================================================")

"""b.) Sort the dataframe by their ScoreRate and print the top 5 players 
with the highestScoreRate"""

TopPlayers=file.sort_values(by='ScoreRate', ascending=False).head(5)
print(f'c.) The top 5 players eith the highest score rate are: ')
print(TopPlayers[['Player', 'ScoreRate']])
print(f'========================================================================================')

"""c.)Print all the players who have got the min runs"""

MinRuns=file['Runs'].min()
PlayersWithMinRuns=file[file['Runs']==MinRuns]
print(PlayersWithMinRuns[['Player', 'Runs']])
print(f'====================================================================================')

"""d.)How many players have got the min runs?"""

MinRuns=file['Runs'].min()
NumberOfPlayers=(file['Runs']==MinRuns).sum()
print(f"{NumberOfPlayers} players have {MinRuns} runs")
print(f'====================================================================================')

"""e.)Print all the players from India who have runs above average"""

AverageRuns=file['Runs'].mean()
PlayersAboveAverageRuns=file[(file['Runs']>AverageRuns) & (file['Country']=='India')]
print(PlayersAboveAverageRuns[['Player', 'Runs']])
print(f'======================================================================================')