import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class SleepDisorderAnalysis:
    def __init__(self, df):
        self.df = df
    # Analyse sleep disorder vs sleep quality 
    def plot_sleep_disorder_vs_sleep_quality(self):
        """Enhanced plot of Sleep Disorders vs Sleep Quality."""
        plt.figure(figsize=(12, 8))
        sns.set(style="whitegrid")
        sns.boxplot(
            x='Sleep Disorders', y='Sleep Quality', data=self.df,
            palette='rocket'
        )
        plt.title("Distribution of Sleep Quality by Sleep Disorders", fontsize=20, fontweight='bold', color='#34495e')
        plt.xlabel("Sleep Disorders", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()