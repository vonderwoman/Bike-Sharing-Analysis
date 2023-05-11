# Bike-Sharing-Analysis

![image](https://user-images.githubusercontent.com/104657679/235465643-08187fa2-909d-4957-af8e-30303a204dc0.png)

[![Open In Jupyter Notebook](https://img.shields.io/badge/Open%20in-Jupyter%20Notebook-blue)](https://mybinder.org/v2/gh/username/repo/master?filepath=notebook.ipynb)     [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Anaconda-Server Badge](https://anaconda.org/anaconda/python/badges/version.svg)](https://anaconda.org/anaconda/python)

# Key Findings: Analysis of customer behaviors based on different time frames and weather conditions
## Table of Contents

- [Project Title](#project-title)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Background](#background)
- [Objectives](#objectives)
- [Dataset](#dataset)
- [Methods](#methods)
- [Tasks](#tasks)
- [Contributing](#contributing)
- [License](#license)

# Project Title: Bike Sharing Analysis
Are you interested in bike sharing systems and their role in traffic, environmental, and health issues? Then you've come to the right place!

# Installation Guide for Anaconda and Jupyter Notebook

This guide will walk you through the installation of Anaconda and Jupyter Notebook on your local machine.
Prerequisites

Before proceeding with the installation, make sure that your computer meets the following requirements:

   -Operating system: Windows, macOS, or Linux
   - Minimum 4GB RAM
   - At least 10GB free hard drive space

Steps

   -Download the latest version of Anaconda from the official website: https://www.anaconda.com/products/individual. Make sure to choose the version that matches your     operating system (Windows, macOS, or Linux).

   -Once the download is complete, double-click on the installer to launch it. Follow the installation wizard instructions to complete the installation process.

   -After installing Anaconda, open the Anaconda Navigator application.

   -Click on the "Launch" button below the "Jupyter Notebook" icon to open Jupyter Notebook.

   -In the Jupyter Notebook interface, you can create new notebooks, open existing ones, and run code cells.

That's it! You now have Anaconda and Jupyter Notebook installed on your machine. You can start using Jupyter Notebook to create and run Python notebooks for data analysis, machine learning, and more.


 # Background
Bike sharing systems have become increasingly popular around the world. They provide an automatic rental process that allows users to easily rent a bike from one location and return it to another. The characteristics of the data generated by these systems make them attractive for research. Unlike other transport services such as buses or subways, the duration of travel, departure, and arrival positions are explicitly recorded in these systems. This feature turns bike sharing systems into a virtual sensor network that can be used for sensing mobility in the city.

# Objectives 
The goal of this analysis is to identify patterns or trends that could help a business optimize its operations, marketing strategies, or other aspects of its performance. The analysis also introduces hypothesis testing and time series analysis, which are common statistical techniques used in business research. The application of these techniques could help a business make data-driven decisions and improve its overall performance

# Data Set
UCI Machine Learning Repository

# Methods

- Exploratory data analysis
- Bivariate analysis
- Hypothesis Testing
- Time Series
- ARIMA Model


# Associated Tasks
This dataset is useful for two main tasks: regression and event/anomaly detection. In the regression task, the goal is to predict the hourly or daily bike rental count based on the environmental and seasonal settings. Meanwhile, in the event and anomaly detection task, the count of rented bikes can be correlated to certain events in the town which can be easily traced via search engines. For instance, a search for "2012-10-30 Washington D.C." in Google may return related results to Hurricane Sandy. By identifying such events, the dataset can also be used to validate anomaly or event detection algorithms.

# Tech Stack
- Jupyter notebook
- Python(refer to the app.py)
- Streamlit interface for deployment

# Overview of the results

## Distribution of Rides
![Distribution of Rides](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/rides_distribution.png)


## Hypothesis testing on casual rides
![Hypothesis_testing_on_casual_rides](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/Hypothesis_testing_on_casual_rides_png.png)

## Hypothesis testing on Registered rides
![Hypothesis testing on Registered rides](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/Hypothesis_testing_on_registered_rides_png.png)

## Number of rides per day
![Number of rides per day](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/number%20of%20rides%20per%20day.png)

## Correlation Matrix
![Correlation matrix](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/corr_matt_png.png)

## Analyzing Seasonal Impact on Rides
![Analyzing Seasonal Impact on Rides](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/Aanalyzing%20Seasonal%20Impact%20on%20Rides.png)
## Analysis of the distributions of the requests over separate hours and days of the week.
![Analysis of the distributions of the requests over separate hours and days of the week.](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/Analysis%20of%20the%20distributions%20of%20the%20requests%20over%20separate%20hours%20and%20days%20of%20the%20week..png)

## Analysis_the distribution of rides on a weekday
![Analysis_the distribution of rides on a weekday basis_png](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/the%20distribution%20of%20rides%20on%20a%20weekday%20basis_png.png)

# Lesson Learned from Bike Sharing Analysis
- Analyzed customers behaviors based on different time frames and weather conditions
# Limitation 
- The analysis focuses on a limited set of variables and does not account for other factors that may affect bike sharing usage, such as demographics, economic factors, or geographic factors.
- The analysis presented in the chapter is based on a single dataset, which limits the generalizability of the findings to other bike-sharing services or regions.
# Improvement to be made
- To increase the generalizability of the findings, the analysis could be replicated with data from other bike-sharing services or regions.
- To account for other potential factors that may affect bike sharing usage, additional variables could be included in the analysis, such as demographic data or geographic data.


# App deployed on Streamlit
![app deployed](https://github.com/vonderwoman/Bike-Sharing-Analysis/blob/main/Output/deployment.JPG)

🌟 Thank you for visiting my repository! If you find the content useful or interesting, I encourage you to give it a star ⭐️.

By starring the repository, you show your support and appreciation for the work put into creating and maintaining it. It also helps to boost its visibility, making it more accessible to others in the community.

Contributions are also highly welcome! Whether it's bug fixes, feature enhancements, or new ideas, your contributions can make a significant impact. Feel free to open issues, submit pull requests, or engage in discussions. Together, we can build an even better project!

Your involvement and feedback are invaluable in shaping the future of this repository. Let's collaborate and make a difference in the world of technology! ✨
# Lincence
MIT
