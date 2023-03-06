#IMPORTING LIBRARIES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#loading the dataset
df=pd.read_csv("spotify.csv")
#data preprocessing
print(df)
print(df.info())
print(df.describe())
print(df.duplicated().sum())
print(df.columns)
#print unique values of all the column
print(df["uri"].unique())
print(df["artist_names"].unique())
print(df['track_name'].unique())
print(df['peak_rank'].unique())
print(df['weeks_on_chart'].unique())
print(df['energy'].unique())
print(df['key'].unique())
print(df['loudness'].unique())
print(df['mode'].unique())
print(df['speechiness'].unique())
print("Data Insights")
print("Name of the songs whose mode value is 1")
print(df.loc[df['mode']==1])
print("The song with maximum energy and the details")
max_energy_index = df['energy'].idxmax()
max_energy_track_name = df.loc[max_energy_index, 'track_name']
max_energy_artist_name=df.loc[max_energy_index,'artist_names']
max_energy_duration=df.loc[max_energy_index,'duration_ms']
print(max_energy_artist_name)
print(max_energy_track_name)
print(max_energy_duration)
print("The song with maximum weeks on chart and the details")
max_weeks_index=df['weeks_on_chart'].idxmax()
max_weeks_track_name=df.loc[max_weeks_index,'track_name']
max_weeks_artist_name=df.loc[max_weeks_index,'artist_names']
max_weeks_duration=df.loc[max_weeks_index,'duration_ms']
print(max_weeks_track_name)
print(max_weeks_artist_name)
print(max_weeks_duration)
print("The song with maximum dance ability and the details ")
max_dance_index=df['danceability'].idxmax()
max_dance_track_name=df.loc[max_dance_index,'track_name']
max_dance_duration=df.loc[max_dance_index,'duration_ms']
max_dance_artist_names=df.loc[max_dance_index,'artist_names']
print(max_dance_track_name)
print(max_dance_duration)
print(max_dance_artist_names)
corr_matrix=df.corr()
print(corr_matrix)
#dropping all the null values
print(df.dropna())
#To ensure that there is no null values
print(df.isnull())
#proceed to plotting
x_new=df['artist_names']
y_new=df['peak_rank']
plt.plot(y_new)
plt.show()
#Heatmap of the dataset
sns.heatmap(data=corr_matrix,annot=True,fmt=".1f")
plt.show()
