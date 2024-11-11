# Importing DataLoader to handle loading and processing of datasets
from .data_loader import DataLoader

# Importing DataAnalysis class for general analysis and correlation of data
from .data_analysis import DataAnalysis

# Importing SleepDurationAnalysis for analyzing sleep duration patterns and plotting graphs related to sleep duration
from .sleep_duration_analysis import SleepDurationAnalysis

# Importing PhysicalActivityAnalysis to analyze the relationship between physical activity levels and sleep quality
from .physical_activity_analysis import PhysicalActivityAnalysis

# Importing DietaryHabitsAnalysis to evaluate the impact of dietary habits on sleep quality
from .dietary_habits_analysis import DietaryHabitsAnalysis

# Importing SleepDisorderAnalysis to analyze sleep disorders and their correlation with sleep quality
from .sleep_disorder_analysis import SleepDisorderAnalysis

# Importing FinalAnalysis to bring together all analyses and generate a comprehensive final conclusion
from .final_analysis import FinalAnalysis