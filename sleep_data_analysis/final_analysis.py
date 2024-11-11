import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

class FinalAnalysis:
    def __init__(self, df):
        self.df = df
    # Display correltion matrix
    def correlation_matrix(self):
        """Enhanced correlation matrix heatmap of numeric columns."""
        plt.figure(figsize=(10, 8))
        corr = self.df.select_dtypes(include=['number']).corr()
        sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5, square=True, cbar_kws={"shrink": .8})
        plt.title("Correlation Matrix", fontsize=20, fontweight='bold', color='#34495e')
        plt.show()