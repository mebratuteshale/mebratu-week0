
import seaborn as sns
import matplotlib.pyplot as plt

def remove_outliers(df, column, threshold,lessThan):
    sns.boxplot(df[column])
    plt.title(f'Original Box Plot of {column}')
    plt.show()
    if lessThan:
        data_after_outlier_removed = df[df[column] <= threshold]
    else:        
        data_after_outlier_removed = df[df[column] >= threshold]
        
    sns.boxplot(data_after_outlier_removed[column])
    plt.title(f'Box Plot without Outliers of {column}')
    plt.show()
    return data_after_outlier_removed