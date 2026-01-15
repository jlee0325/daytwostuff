# %%
import pandas as pd


# %%
df = pd.read_csv("digi.csv")   # assumes digi.csv is in the same folder as your workspace root
df.head()


## What is your terminal display "path"? (type/paste as text into the .py file) 
## /workspaces/daytwostuff

## Should you include the environment in your repo or not?  
## No, you should not include the environment in your repo. Instead, you can use a requirements.txt or environment.yml file to specify dependencies.

## Now what is your terminal display "path"? Is it different? 
##(.venv) @jlee0325 ➜ /workspaces/daytwostuff (main)

##
# %%

## Find the extension in the extension menu. What do you notice about the extension menu? 
## I notice that there are various extensions available for different programming languages and tools, including Python, JavaScript, and Docker.

## Review the capabilities, what are three useful elements of Data Wrangler
## 1. Data Cleaning: Data Wrangler provides tools for cleaning and transforming data, such as removing duplicates, handling missing values, and standardizing formats.
## 2. Data Visualization: Data Wrangler allows users to create visualizations of their data, making it easier to identify patterns and insights.
## 3. Integration with Jupyter Notebooks: Data Wrangler can be integrated with Jupyter Notebooks, allowing users to seamlessly incorporate data wrangling tasks into their data analysis workflows.
# %%

## Plotly Version: 6.5.1
## Why do we use a requirements.txt file?
## A requirements.txt file is used to specify the dependencies and their versions needed for a Python project. It allows for easy installation of the required packages using pip, ensuring that the project can be set up consistently across different environments.

# %%
##Recipe
## Create/open the repo in VS Code
## Create a virtual environment
## Activate the virtual environment
## Install necessary packages
## Create a requirements.txt file
## Deactivate the virtual environment
## Push the changes to GitHub
