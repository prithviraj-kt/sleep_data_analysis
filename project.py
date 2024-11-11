# Import the main classes from the package
from sleep_data_analysis.data_loader import DataLoader
from sleep_data_analysis.data_analysis import DataAnalysis
from sleep_data_analysis.sleep_duration_analysis import SleepDurationAnalysis
from sleep_data_analysis.physical_activity_analysis import PhysicalActivityAnalysis
from sleep_data_analysis.dietary_habits_analysis import DietaryHabitsAnalysis
from sleep_data_analysis.sleep_disorder_analysis import SleepDisorderAnalysis
# from health_sleep_analysis.medication_analysis import MedicationAnalysis
from sleep_data_analysis.final_analysis import FinalAnalysis

def load_data():
    # Step 1: Load Data
    data_loader = DataLoader()  # Automatically loads the built-in CSV file
    print("Dataset Information:")
    data_loader.display_info()
    return data_loader.df

def analyze_age_vs_sleep_quality(df):
    # Step 2: Basic Data Analysis - Age vs Sleep Quality
    print("\nAnalyzing Age vs Sleep Quality...")
    analysis = DataAnalysis(df)
    analysis.plot_age_vs_sleep_quality()
    print("Correlation coefficient between Age and Sleep Quality:", analysis.correlation())

def analyze_sleep_duration(df):
    # Step 3: Sleep Duration Analysis
    print("\nAnalyzing Sleep Duration...")
    sleep_analysis = SleepDurationAnalysis(df)
    sleep_analysis.process_sleep_times()
    sleep_analysis.plot_sleep_time_vs_quality()
    #print("R-squared value for Sleep Duration vs Sleep Quality:", sleep_analysis.linear_regression_on_sleep_duration())

def analyze_physical_activity(df):
    # Step 4: Physical Activity Analysis
    print("\nAnalyzing Physical Activity...")
    physical_activity_analysis = PhysicalActivityAnalysis(df)
    physical_activity_analysis.plot_physical_activity_vs_sleep_quality()

def analyze_dietary_habits(df):
    # Step 5: Dietary Habits Analysis
    print("\nAnalyzing Dietary Habits...")
    dietary_analysis = DietaryHabitsAnalysis(df)
    dietary_analysis.plot_dietary_habits_vs_sleep_quality()

def analyze_sleep_disorders(df):
    # Step 6: Sleep Disorder Analysis
    print("\nAnalyzing Sleep Disorders...")
    sleep_disorder_analysis = SleepDisorderAnalysis(df)
    sleep_disorder_analysis.plot_sleep_disorder_vs_sleep_quality()

def final_comprehensive_analysis(df):
    # Step 7: Final Comprehensive Analysis
    print("\nConducting Final Comprehensive Analysis...")
    final_analysis = FinalAnalysis(df)
    final_analysis.correlation_matrix()

def main():
    df = load_data()
    analyze_age_vs_sleep_quality(df)
    analyze_sleep_duration(df)
    analyze_physical_activity(df)
    analyze_dietary_habits(df)
    analyze_sleep_disorders(df)
    final_comprehensive_analysis(df)

if __name__ == "__main__":
    main()