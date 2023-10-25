# Import all packages and set plots to be used
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline
#Loading the data
results = pd.read_csv(r"D:\Karthik\Python Programs\F1\results.csv")
races = pd.read_csv(r"D:\Karthik\Python Programs\F1\races.csv")
drivers = pd.read_csv(r"D:\Karthik\Python Programs\F1\drivers.csv")
constructors = pd.read_csv(r"D:\Karthik\Python Programs\F1\constructors.csv")
#Merge Datasets
f1 = pd.merge(results,
races[['raceId','year','name','round']],on='raceId',how='left')
f1=pd.merge(f1,drivers[['driverId','driverRef','nationality']],on='driverId',
how='left')
f1=pd.merge(f1,constructors[['constructorId','name','nationality']],
on='constructorId',how='left')
#Drop columns which are not required
f1.drop(['number', 'position', 'positionText', 'laps', 'fastestLap',
'statusId','resultId', 'raceId', 'driverId', 'constructorId'], axis=1, inplace=True)
#Rename columns
f1.rename(columns={'rank':'fastestLapRank', 'name_x':'gp_name',
'nationality_x':'driver_nationality', 'name_y':'constructor_name',
'nationality_y':'constructor_nationality', 'driverRef':'driver'},
inplace=True)
#Re-Arrange Columns
f1 = f1[['year', 'gp_name', 'round','driver', 'constructor_name', 'grid',
'positionOrder', 'points', 'time','milliseconds', 'fastestLapRank',
'fastestLapTime', 'fastestLapSpeed', 'driver_nationality',
'constructor_nationality']]
#Since the 2023 season is not yet complete, we will drop the 2023 season data.
f1 = f1[f1['year']!=2023]
#Sort Values in descending order of year
f1 = f1.sort_values(by=['year','round','positionOrder'],
ascending=[False,True,True])
#Replacing /N in columns since those readings are not there if driver did not finish a race
#Also replacing /N in since no time records when the driver is lapped
f1.time.replace('\\N', np.nan, inplace=True)
f1.milliseconds.replace('\\N', np.nan, inplace=True)
f1.fastestLapRank.replace('\\N', np.nan, inplace=True)
f1.fastestLapTime.replace('\\N', np.nan, inplace=True)
f1.fastestLapSpeed.replace('\\N', np.nan, inplace=True)
#Changing Datatypes
f1.fastestLapSpeed = f1.fastestLapSpeed.astype(float)
f1.fastestLapRank = f1.fastestLapRank.astype(float)
f1.milliseconds = f1.milliseconds.astype(float)
#Reset Indices
f1.reset_index(drop=True, inplace=True)
#User-defined functions to perform operations
def All_GP_Winners ():
 driver_winner =f1.loc[f1['positionOrder']==1].groupby('driver')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
 sns.barplot(data=driver_winner, y='driver', x='positionOrder', color='gold',
alpha=1)
 plt.title('GP Winners in F1 as of 2022')
 plt.ylabel('Driver Name')
 plt.xlabel('Number of GP wins')
 plt.yticks([])

def Top_n_Winners(n):
 #Create new Data Frame for top 10 GP winnners
 driver_winner =f1.loc[f1['positionOrder']==1].groupby('driver')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
 top10 = driver_winner.head(n)
 sns.barplot(data=top10, y='driver', x='positionOrder', color='Red',
linewidth=0.8,edgecolor='black')
 plt.title(f'Top {n} GP winners')
 plt.xlabel('Number of Wins')
 plt.ylabel('Driver Name')
def Speed_History():
 #Visualisation of Speed on different tracks from 2004 onwards
 f1_speed = f1[f1['year']>=2004]
 f1_group_speed=f1_speed.groupby(['gp_name','year'])['fastestLapSpeed'].mean().to_frame().reset_index()
 #Creating a facetgrid
 g = sns.FacetGrid(data=f1_group_speed, col='gp_name', col_wrap=5)
 g.map(plt.scatter,'year', 'fastestLapSpeed', color='blue', alpha=0.5,linewidth=0.5, edgecolor='black', s=75)
 g.set_titles('{col_name}')
 g.set_xlabels('{Year}')
 g.set_ylabels('Average fastest speed(kmh)')
 plt.subplots_adjust(top=0.92)
 g.fig.suptitle('Average Speed amongst all teams during the fastest lap at individual GPs');

def Requested_Race():
 Y=int(input('Enter Year: '))
 GP=input('Enter Grand Prix location: ')
 GP+=" Grand Prix"
 f1_req = f1[(f1['year'] == Y) & (f1['gp_name'] == GP)].reset_index()
 print('\n', f1_req)
def Year_Winners():
 Y=int(input('Enter Year: '))
 f1_req = f1[(f1['year'] == Y) & (f1['positionOrder'] == 1)].reset_index()
 print('\n',f1_req)
def Driver_Wins():
 D=input('Enter driver: ')
 f1_req = f1[(f1['driver'] == D) & (f1['positionOrder'] == 1)].copy()
 print(df_empty.head(20))
#Main Interfac
flag = True
while(flag):
 print('\nChoose from the list below what you want to do: ')
 print('1. Results of a specific race')
 print('2. Visualisation of all Grand Prix winners ever')
 print("3. Top 'n' Grand Prix winnners")
 print('4. Visualisation of speed on different tracks over the years')
 print('5. List all winnners of a particular year')
 print('6. List the last 20 wins of a driver')
 print('7. Quit')
 choice = int(input('Enter your choice: '))
 if(choice==1):
     Requested_Race()
     flag=False
 elif(choice==2):
     All_GP_Winners()
     flag=False
 elif(choice==3):
     x=int(input('Enter the number of top drivers you want to see: '))
     Top_n_Winners(x)
     flag=False
 elif(choice==4):
     Speed_History()
     flag=False
 elif(choice==5):
     Year_Winners()
     flag=False
 elif(choice==6):
     Driver_Wins()
     flag=False
 elif(choice==7):
     flag=False
 else:
     print('You can only enter numbers from 1 to 5')