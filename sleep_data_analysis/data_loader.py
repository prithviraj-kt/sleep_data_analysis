import pandas as pd  # Library for handling data

class DataLoader:
    def __init__(self, file_path="Health_Sleep_Statistics.csv"):
        self.file_path = file_path  # Set the file path
        self.df = None  # Initialize dataframe
        self.load_data()  # Load data when the object is created

    # Load dataset from CSV file
    def load_data(self):
        self.df = pd.read_csv(self.file_path)

    # Display basic info about the dataset
    def display_info(self):
        print(self.df.head())  # First few rows of the data
        print(self.df.size)  # Total number of elements
        print(self.df.shape)  # Shape of the dataframe
        print(self.df.info())  # Info about the dataframe
        print(self.df.describe())  # Summary statistics
        print(self.df.isna().sum())  # Missing values
        print(self.df.duplicated().sum())  # Duplicated rows
        print(self.df.columns)  # Column names
