# F1 Data Analysis

This is a data analysis project for Formula 1 (F1) racing data. The project involves importing, cleaning, and analyzing F1 race data to gain insights and visualize key aspects of the sport. The project is implemented in Python using the Pandas, Matplotlib, and Seaborn libraries.

## Getting Started

To run this project locally, you will need to follow the steps below.

### Prerequisites

Before running the code, ensure you have the necessary Python packages installed. You can install them using `pip`:

```bash
pip install numpy pandas matplotlib seaborn
```

### Code

You can find the entire code in the [F1.py](f1.py) file.

### Dataset

The project uses the following datasets:
- `results.csv`: Contains F1 race results.
- `races.csv`: Contains information about F1 races.
- `drivers.csv`: Contains information about F1 drivers.
- `constructors.csv`: Contains information about F1 constructors.

Make sure to download the datasets and place them in the same directory as the Jupyter Notebook.

## Data Cleaning and Transformation

The code performs the following data cleaning and transformation steps:

1. Load the data from the CSV files.
2. Merge the datasets to create a single, comprehensive dataset.
3. Drop unnecessary columns.
4. Rename columns for clarity.
5. Remove data for the incomplete 2023 season.
6. Sort the data by year, round, and position order.
7. Replace missing values.
8. Change data types.
9. Reset the DataFrame index.

## Data Analysis and Visualization

The code provides several user-defined functions for data analysis and visualization:

1. `All_GP_Winners`: Visualizes all Grand Prix winners ever.
2. `Top_n_Winners`: Visualizes the top 'n' Grand Prix winners.
3. `Speed_History`: Visualizes the average speed on different tracks over the years.
4. `Requested_Race`: Lists race results for a specific year and Grand Prix location.
5. `Year_Winners`: Lists all winners of a particular year.
6. `Driver_Wins`: Lists the last 20 wins of a driver.

## Usage

1. Run the Jupyter Notebook to analyze and visualize the F1 data.
2. Choose from the options presented in the main interface to perform specific analyses.
