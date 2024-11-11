import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class SleepDurationAnalysis:
    @staticmethod
    def sleep_duration_hours_helper_function(str_time):
        """Helper function to convert time in 'HH:MM' format to hours."""
        h, m = map(int, str_time.split(':'))
        return h + m / 60

    def __init__(self, df):
        self.df = df

    def process_sleep_times(self):
        """Convert 'Bedtime' and 'Wake-up Time' columns to hours."""
        self.df['Bedtime'] = self.df['Bedtime'].apply(self.sleep_duration_hours_helper_function)
        self.df['Wake-up Time'] = self.df['Wake-up Time'].apply(self.sleep_duration_hours_helper_function)
        self.df['Sleep Duration Hours'] = (self.df['Wake-up Time'] - self.df['Bedtime']) % 24

    def plot_sleep_time_vs_quality(self):
        """Enhanced plot of Bedtime, Wake-up Time, and Sleep Duration vs Sleep Quality with regression line on the scatter plot."""
        
        # Bedtime vs Sleep Quality
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Bedtime', y='Sleep Quality', data=self.df, palette='Blues_d')
        plt.xlabel("Bedtime", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.title("Bedtime vs Sleep Quality", fontsize=18, fontweight='bold', color='#2c3e50')
        
        # Adding value labels on top of bars
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        fontsize=12, color='black', 
                        xytext=(0, 5), textcoords='offset points')
        
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()

        # Wake-up Time vs Sleep Quality
        plt.figure(figsize=(12, 6))
        ax = sns.barplot(x='Wake-up Time', y='Sleep Quality', data=self.df, palette='Purples_d')
        plt.xlabel("Wake-up Time", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.title("Wake-up Time vs Sleep Quality", fontsize=18, fontweight='bold', color='#2c3e50')
        
        # Adding value labels on top of bars
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}', 
                        (p.get_x() + p.get_width() / 2., p.get_height()), 
                        ha='center', va='center', 
                        fontsize=12, color='black', 
                        xytext=(0, 5), textcoords='offset points')
        
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()

        # Sleep Duration Hours vs Sleep Quality with regression line
        plt.figure(figsize=(12, 6))
        sns.scatterplot(
            x='Sleep Duration Hours', y='Sleep Quality', data=self.df,
            hue='Sleep Quality', palette='coolwarm', size='Sleep Quality', sizes=(50, 200), alpha=0.8
        )
        
        # Regression line
        X = self.df[['Sleep Duration Hours']]
        Y = self.df['Sleep Quality']
        model = LinearRegression()
        model.fit(X, Y)
        plt.plot(X, model.predict(X), color='red', linewidth=2, label='Best Fit Line')

        # Enhancing aesthetics
        plt.legend(title='Sleep Quality', loc='upper left', bbox_to_anchor=(1, 1), fontsize=12)
        plt.xlabel("Sleep Duration Hours", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.title("Sleep Duration Hours vs Sleep Quality", fontsize=18, fontweight='bold', color='#2c3e50')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()
