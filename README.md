#Air Quality Analysis in Major North American Cities with the Rise of Electric Vehicles (EVs)
#Overview
This project analyzes the impact of electric vehicle (EV) adoption on air quality in major North American cities between 2016 and 2021. By studying pollutants such as PM2.5, NO2, and CO, this research aims to understand the relationship between sustainable transportation and urban air quality improvement. Using regression models, we explore trends and provide insights into how EV adoption correlates with reduced air pollution.

#Key Features
Air Quality Trends: Detailed analysis of pollutant levels (PM2.5, NO2, CO) across multiple cities.
EV Adoption Impact: Correlation between EV adoption rates and pollutant reduction.
Statistical Analysis: Regression models to quantify relationships and identify significant factors.
Data Pipeline: Robust ETL (Extract, Transform, Load) pipeline to prepare datasets for analysis.
#Data Sources
Air Quality Data: U.S. Environmental Protection Agency (EPA) - Daily pollutant measurements, including metadata about monitoring stations.
Electric Vehicle Adoption Data: U.S. Department of Energy (DOE) - Annual EV registration trends by city and state.
#Methodology
Data Collection: Gathered data from EPA and DOE spanning 2016–2021.
#Data Processing:
Standardized column names and cleaned missing values.
Aggregated daily pollutant data into yearly averages.
Unified geographic identifiers for consistent analysis.
#Analysis:
Exploratory Data Analysis (EDA) to observe pollutant trends.
Simple and multiple regression models to assess correlations.
#Visualization: Charts and plots to illustrate key findings.
#Results
#Key Insights:
NO2 emerged as the most significant contributor to PM2.5 levels.
EV adoption showed a negative correlation with PM2.5 but was not statistically significant.
Declines in pollutant levels align with increased EV usage but require further investigation.
#Limitations:
Small dataset and potential multicollinearity among variables.
Need for broader factors and expanded data for deeper insights.
#Technologies Used
Programming Languages: Python
Libraries and Tools: Pandas, NumPy, Matplotlib, Seaborn, SQLite
Database: SQLite for efficient data querying and analysis.
#Future Work
Expand datasets to include more cities and years for increased statistical power.
Refine regression models to incorporate additional variables and reduce collinearity.
Investigate the long-term impact of EVs on other pollutants and urban mobility metrics.

# Methods of Advanced Data Engineering Template Project

This template project provides some structure for your open data project in the MADE module at FAU.
This repository contains (a) a data science project that is developed by the student over the course of the semester, and (b) the exercises that are submitted over the course of the semester.

To get started, please follow these steps:
1. Create your own fork of this repository. Feel free to rename the repository right after creation, before you let the teaching instructors know your repository URL. **Do not rename the repository during the semester**.

## Project Work
Your data engineering project will run alongside lectures during the semester. We will ask you to regularly submit project work as milestones, so you can reasonably pace your work. All project work submissions **must** be placed in the `project` folder.

### Exporting a Jupyter Notebook
Jupyter Notebooks can be exported using `nbconvert` (`pip install nbconvert`). For example, to export the example notebook to HTML: `jupyter nbconvert --to html examples/final-report-example.ipynb --embed-images --output final-report.html`


## Exercises
During the semester you will need to complete exercises using [Jayvee](https://github.com/jvalue/jayvee). You **must** place your submission in the `exercises` folder in your repository and name them according to their number from one to five: `exercise<number from 1-5>.jv`.

In regular intervals, exercises will be given as homework to complete during the semester. Details and deadlines will be discussed in the lecture, also see the [course schedule](https://made.uni1.de/).

### Exercise Feedback
We provide automated exercise feedback using a GitHub action (that is defined in `.github/workflows/exercise-feedback.yml`). 

To view your exercise feedback, navigate to Actions → Exercise Feedback in your repository.

The exercise feedback is executed whenever you make a change in files in the `exercise` folder and push your local changes to the repository on GitHub. To see the feedback, open the latest GitHub Action run, open the `exercise-feedback` job and `Exercise Feedback` step. You should see command line output that contains output like this:

```sh
Found exercises/exercise1.jv, executing model...
Found output file airports.sqlite, grading...
Grading Exercise 1
	Overall points 17 of 17
	---
	By category:
		Shape: 4 of 4
		Types: 13 of 13
```
