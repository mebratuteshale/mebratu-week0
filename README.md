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
 * Python Installation (windows):
  - Download the latest Python 3.12.4 installer from [Python.org](https://www.python.org/downloads/) by navigating to the downloads section.
  - Make sure to mark Add Python to PATH otherwise you will have to do it explicitly.
  - Verify Python installation by running `python --version`
 * Python Installation (Linux):
  -  Check if your device is pre-installed with Python or not `python --version` or `python3 --version`
  -  To install the latest Python on most Linux systems
     ```
      $ sudo add-apt-repository ppa:deadsnakes/ppa
      $ sudo apt-get update
      $ sudo apt-get install python3.13```
*  **Git Installation**: git was used for CI/CD operations
  - On windows: Just go to [gitforwindows.org](https://git-scm.com/download/win) and the download will start automatically
  - On Linux: on a Debian-based distribution, such as Ubuntu, try apt:
      ```$ sudo apt install git-all```
* Setup virtual Environment (optional): to avoid version conflict among different project requirements, create a virtual envrinment specific to this project.
  **Virtualenv** is a tool to set up your Python environments. Since Python 3.3, a subset of it has been integrated into the standard library under the venv module. You can install venv to your host Python by running this command in your terminal:
  ```pip install virtualenv```
   - To use venv in your project, in your terminal, create a new project folder, cd to the project folder in your terminal, and run the following command:
     ```python<version> -m venv <virtual-environment-name>```
   - Create virual environment
     ```
      mkdir 10acadamy-challenge
      cd 10acadamy-challenge
      python3.8 -m venv env```
     
   - Activate the Virtual Environment:```
     env/Scripts/activate.bat```   
     Linux systems:```
       source env/bin/activate```
     
* **Install all dependencies**
    + After activating the virual environment install project dependencies in the `requirements.txt`
      ```pip install -r requirements.txt```
* **Clone Project**: clone the project in to your local machine ```
  git clone https://github.com/mebratuteshale/mebratu-week0 ```
