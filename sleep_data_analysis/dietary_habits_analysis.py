import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class DietaryHabitsAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_dietary_habits_vs_sleep_quality(self):
        """Enhanced bar graph with individual points for Dietary Habits vs Sleep Quality."""
        plt.figure(figsize=(14, 8))
        sns.set(style="whitegrid")

        self.df['Dietary Habits'] = self.df['Dietary Habits'].astype('category')
        mean_sleep_quality = self.df.groupby('Dietary Habits')['Sleep Quality'].mean()
        bar_colors = sns.color_palette("mako", len(mean_sleep_quality))
        bars = plt.bar(mean_sleep_quality.index, mean_sleep_quality, color=bar_colors, width=0.6)

        for i, dietary_habit in enumerate(mean_sleep_quality.index):
            individual_points = self.df[self.df['Dietary Habits'] == dietary_habit]['Sleep Quality']
            plt.scatter([dietary_habit] * len(individual_points), individual_points, color='black', alpha=0.6, s=30, zorder=3)

        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.05, f'{yval:.2f}', ha='center', va='bottom', fontsize=12, color='black')

        # Aesthetic improvements
        plt.title("Dietary Habits vs Sleep Quality", fontsize=20, fontweight='bold', color='#34495e')
        plt.xlabel("Dietary Habits", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.tight_layout()

        plt.show()