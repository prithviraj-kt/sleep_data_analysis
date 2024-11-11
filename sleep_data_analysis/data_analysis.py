import matplotlib.pyplot as plt  # Used for creating graphs
import seaborn as sns  # Makes graphs look nicer
from sklearn.linear_model import LinearRegression  # For making predictions

class DataAnalysis:
    def __init__(self, df):
        self.df = df  # Store the data

    # Find correlation between Age and Sleep Quality
    def correlation(self):
        age_vs_sleep_quality_corr = self.df[['Age', 'Sleep Quality']].corr()
        return age_vs_sleep_quality_corr.iloc[0, 1]

    # Plot a graph of Age vs Sleep Quality with a regression line
    def plot_age_vs_sleep_quality(self):
        plt.figure(figsize=(12, 8))
        sns.set(style="whitegrid")
        sns.regplot(
            x='Age', y='Sleep Quality', data=self.df,
            scatter_kws={'s': 100, 'alpha': 0.6, 'color': '#3498db'},
            line_kws={'color': '#e74c3c', 'linewidth': 2}
        )
        plt.title("Age vs Sleep Quality", fontsize=20, fontweight='bold', color='#2c3e50')
        plt.xlabel("Age", fontsize=15)
        plt.ylabel("Sleep Quality", fontsize=15)
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        sns.despine()
        plt.show()

    # Fit and return a linear regression model
    def linear_regression(self, X, Y):
        model = LinearRegression()
        model.fit(X, Y)
        return model

    # Plot actual vs predicted data using linear regression
    def plot_linear_regression(self, X, Y, model):
        plt.figure(figsize=(12, 6))
        sns.scatterplot(x='Age', y='Sleep Quality', data=self.df, label='Actual Data')
        plt.plot(X, model.predict(X), color='green', label='Predicted Data')
        plt.title("Age vs Sleep Quality")
        plt.xlabel("Age")
        plt.ylabel("Sleep Quality")
        plt.legend()
        plt.show()
