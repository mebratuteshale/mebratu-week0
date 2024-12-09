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

