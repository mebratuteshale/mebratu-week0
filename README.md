# Week0 challenge by 10acadamy
### Overview
This repo created to complete the week0 challenges by **10acadamy** as an admission to the 12-week long **10 Academy: Data Engineer and Artificial Intelligence Mastery Challenge**. 
The challenge include setting-up git repo, and performing EDA analysis for three data sources collected from **Solar Radiation Measurement Data**.
Tasks inlcude: 
+ Development Environment setup
+ EDA Analysis
## Development Environment setup (Prerequest)
To setup the development environment follow the following steps:
* **Python Installation**
  + Python Installation (windows):
    - Download the latest Python 3.12.4 installer from [Python.org](https://www.python.org/downloads/) by navigating to the downloads section.
    - Make sure to mark Add Python to PATH otherwise you will have to do it explicitly.
  + Verify Python installation by running
     ```
      python --version
      ```
*  **Git Installation** (windows): git was used for **CI/CD** operations
    A windows installer from [gitforwindows.org](https://git-scm.com/download/win) is used to install git on windows.
* **Setup virtual Environment**: to avoid version conflict among different project requirements, create a virtual envrinment specific to this project.
  **Virtualenv** is a tool to set up your Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. You can install venv to your host Python by running this command in your terminal:
  ```pip install virtualenv```
   - The general usage of the **venv** library is: 
      ```
      python<version> -m venv <virtual-environment-name>
      ```
   - Create virual environment: A directory was created for all projects from 10acadamy.
      ```
      mkdir 10acadamy-challenge             // project directory
      cd 10acadamy-challenge               // change directory
      python3.8 -m venv .venv10acad       // create a virtual environment called .venv10acad
      ```     
   - Activate the Virtual Environment:
       ```
        .venv10acad\Scripts\activate
       ```
## Project Setup
* Create `git` repo:
  A public git repository [mebratu-week0](https://github.com/mebratuteshale/mebratu-week0) was created.  
* **Clone project**:
  ```
  git clone https://github.com/mebratuteshale/mebratu-week0
  ```
* **Install all dependencies**
    + After activating the virual environment install project dependencies in the `requirements.txt`
      ```pip install -r requirements.txt```
* Project (repo) Skeloton was created as shown
  
  ![Screenshot of project (repo) skeleton.](https://github.com/mebratuteshale/mebratu-week0/blob/main/screenshoots/project_skeleton.png)
## EDA Analysis
* Import `panda`, `numpy`, `pylab` and `seaborn`
* Read datasets one-by-one
  ```
  df_benin=pd.read_csv('../dataset/benin-malanville.csv')
  ```
* **Understand data**:
  + _Summary Statistics_: Calculate the `mean`, `median`, `standard deviation`, `max` and `min` for each the numeric columns to understand data distribution
  + _Data Quality Check_ is performed by removing negative values of the GHI, DNI, and DHI, remove outliers from the Temprature readings.
    ```
    # change the datatype of the `Timestamp` column from `Object` type to `datetime` 
    df_benin['Timestamp']=pd.to_datetime(df_benin['Timestamp'])
    ```
   **Remove outliers** from temprature data
   ```
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
    ```
  + _Time Series Analysis_: Bar charts and Line charts of GHI, DNI, DHI, and Tamb over time are created to observe patterns by month
     ![Time Series anlysis using linechart.](https://github.com/mebratuteshale/mebratu-week0/blob/main/screenshoots/linecharts.png)
     ![Time Series anlysis using Barchart .](https://github.com/mebratuteshale/mebratu-week0/blob/main/screenshoots/barcharts.png)
    
    

