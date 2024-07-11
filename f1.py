import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# Load the data
results = pd.read_csv(r"D:\Karthik\Python Programs\F1\results.csv")
races = pd.read_csv(r"D:\Karthik\Python Programs\F1\races.csv")
drivers = pd.read_csv(r"D:\Karthik\Python Programs\F1\drivers.csv")
constructors = pd.read_csv(r"D:\Karthik\Python Programs\F1\constructors.csv")

# Merge datasets
f1 = pd.merge(results, races[['raceId', 'year', 'name', 'round']], on='raceId', how='left')
f1 = pd.merge(f1, drivers[['driverId', 'driverRef', 'nationality']], on='driverId', how='left')
f1 = pd.merge(f1, constructors[['constructorId', 'name', 'nationality']], on='constructorId', how='left')

# Drop columns which are not required
columns_to_drop = ['number', 'position', 'positionText', 'laps', 'fastestLap', 'statusId', 'resultId', 'raceId', 'driverId', 'constructorId']
f1.drop(columns=columns_to_drop, axis=1, inplace=True)

# Rename columns
f1.rename(columns={
    'rank': 'fastestLapRank',
    'name_x': 'gp_name',
    'nationality_x': 'driver_nationality',
    'name_y': 'constructor_name',
    'nationality_y': 'constructor_nationality',
    'driverRef': 'driver'
}, inplace=True)

# Re-arrange columns
columns_order = ['year', 'gp_name', 'round', 'driver', 'constructor_name', 'grid', 'positionOrder', 'points', 'time', 'milliseconds', 'fastestLapRank', 'fastestLapTime', 'fastestLapSpeed', 'driver_nationality', 'constructor_nationality']
f1 = f1[columns_order]

# Drop data from the 2023 season
f1 = f1[f1['year'] != 2023]

# Sort values in descending order of year
f1 = f1.sort_values(by=['year', 'round', 'positionOrder'], ascending=[False, True, True])

# Replace missing values
missing_value_cols = ['time', 'milliseconds', 'fastestLapRank', 'fastestLapTime', 'fastestLapSpeed']
for col in missing_value_cols:
    f1[col].replace('\\N', np.nan, inplace=True)

# Change data types
f1['fastestLapSpeed'] = f1['fastestLapSpeed'].astype(float)
f1['fastestLapRank'] = f1['fastestLapRank'].astype(float)
f1['milliseconds'] = f1['milliseconds'].astype(float)

# Reset index
f1.reset_index(drop=True, inplace=True)

# User-defined functions
def All_GP_Winners():
    """Visualize all GP winners."""
    driver_winner = f1.loc[f1['positionOrder'] == 1].groupby('driver')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
    sns.barplot(data=driver_winner, y='driver', x='positionOrder', color='gold', alpha=1)
    plt.title('GP Winners in F1 as of 2022')
    plt.ylabel('Driver Name')
    plt.xlabel('Number of GP wins')
    plt.show()

def Top_n_Winners(n):
    """Visualize top n GP winners."""
    driver_winner = f1.loc[f1['positionOrder'] == 1].groupby('driver')['positionOrder'].count().sort_values(ascending=False).to_frame().reset_index()
    top_n = driver_winner.head(n)
    sns.barplot(data=top_n, y='driver', x='positionOrder', color='Red', linewidth=0.8, edgecolor='black')
    plt.title(f'Top {n} GP winners')
    plt.xlabel('Number of Wins')
    plt.ylabel('Driver Name')
    plt.show()

def Speed_History():
    """Visualize speed history on different tracks from 2004 onwards."""
    f1_speed = f1[f1['year'] >= 2004]
    f1_group_speed = f1_speed.groupby(['gp_name', 'year'])['fastestLapSpeed'].mean().to_frame().reset_index()
    g = sns.FacetGrid(data=f1_group_speed, col='gp_name', col_wrap=5)
    g.map(plt.scatter, 'year', 'fastestLapSpeed', color='blue', alpha=0.5, linewidth=0.5, edgecolor='black', s=75)
    g.set_titles('{col_name}')
    g.set_xlabels('Year')
    g.set_ylabels('Average fastest speed (km/h)')
    plt.subplots_adjust(top=0.92)
    g.fig.suptitle('Average Speed among all teams during the fastest lap at individual GPs')
    plt.show()

def Requested_Race():
    """Display results of a specific race."""
    try:
        Y = int(input('Enter Year: '))
        GP = input('Enter Grand Prix location: ') + " Grand Prix"
        f1_req = f1[(f1['year'] == Y) & (f1['gp_name'] == GP)].reset_index()
        print('\n', f1_req)
    except ValueError:
        print("Invalid input. Please enter valid year and GP location.")

def Year_Winners():
    """List all winners of a particular year."""
    try:
        Y = int(input('Enter Year: '))
        f1_req = f1[(f1['year'] == Y) & (f1['positionOrder'] == 1)].reset_index()
        print('\n', f1_req)
    except ValueError:
        print("Invalid input. Please enter a valid year.")

def Driver_Wins():
    """List the last 20 wins of a driver."""
    D = input('Enter driver: ')
    f1_req = f1[(f1['driver'] == D) & (f1['positionOrder'] == 1)].head(20).reset_index()
    print('\n', f1_req)

# Main Interface
def main():
    while True:
        print('\nChoose from the list below what you want to do: ')
        print('1. Results of a specific race')
        print('2. Visualization of all Grand Prix winners ever')
        print("3. Top 'n' Grand Prix winners")
        print('4. Visualization of speed on different tracks over the years')
        print('5. List all winners of a particular year')
        print('6. List the last 20 wins of a driver')
        print('7. Quit')
        
        try:
            choice = int(input('Enter your choice: '))
            if choice == 1:
                Requested_Race()
            elif choice == 2:
                All_GP_Winners()
            elif choice == 3:
                x = int(input('Enter the number of top drivers you want to see: '))
                Top_n_Winners(x)
            elif choice == 4:
                Speed_History()
            elif choice == 5:
                Year_Winners()
            elif choice == 6:
                Driver_Wins()
            elif choice == 7:
                break
            else:
                print('You can only enter numbers from 1 to 7')
        except ValueError:
            print('Invalid input. Please enter a number from 1 to 7.')

if __name__ == "__main__":
    main()
