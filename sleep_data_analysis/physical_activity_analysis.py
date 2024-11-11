import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class PhysicalActivityAnalysis:
    def __init__(self, df):
        self.df = df

    def plot_physical_activity_vs_sleep_quality(self):
        """Enhanced plot of Physical Activity Level vs Sleep Quality with values on top of each bar."""
        plt.figure(figsize=(12, 8))
        sns.set(style="whitegrid")
        ax = sns.barplot(
            x='Physical Activity Level', y='Sleep Quality', data=self.df,
            palette='viridis'
        )
        
        # Adding value labels on top of bars
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        fontsize=12, color='black', 
                        xytext=(0, 5), textcoords='offset points')

        plt.title("Physical Activity Level vs Sleep Quality", fontsize=20, fontweight='bold', color='#34495e')
        plt.xlabel("Physical Activity Level", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()

    def calories_burned_vs_sleep_quality(self):
        """Enhanced plot of Calories Burned vs Sleep Quality with regression line."""
        plt.figure(figsize=(12, 8))
        
        # Scatter plot with color gradient
        sns.scatterplot(
            x='Calories Burned', y='Sleep Quality', data=self.df,
            hue='Sleep Quality', palette='coolwarm', size='Sleep Quality', sizes=(50, 200), alpha=0.8
        )
        
        # Add regression line
        X = self.df[['Calories Burned']]
        Y = self.df['Sleep Quality']
        model = LinearRegression()
        model.fit(X, Y)
        plt.plot(X, model.predict(X), color='red', linewidth=2, label='Best Fit Line')
        
        # Enhancing aesthetics
        plt.legend(title='Sleep Quality', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.xlabel("Calories Burned", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.title("Calories Burned vs Sleep Quality", fontsize=18, fontweight='bold', color='#2c3e50')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()