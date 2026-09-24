# Mobile Phone Analytics

# Project Overview

**Mobile Phone Analytics** is a data analytics and machine learning project that analyzes mobile phone prices, specifications, performance, and ratings.

The project follows an end-to-end analytics workflow, starting with data cleaning and feature engineering, followed by exploratory data analysis, visualization, predictive modeling, and interactive dashboard development.

The final project includes a **Streamlit dashboard** that allows users to explore mobile phone data and a **Random Forest Regression model** for mobile phone price prediction.

---

## 1. Problem Statement

The mobile phone market contains a wide variety of devices with different brands, prices, specifications, performance levels, and ratings.

Analyzing this data can help identify patterns between mobile phone prices and their specifications.

### Objectives

The main objectives of this project are:

* Analyze mobile phone prices across different brands.
* Understand the relationship between specifications and prices.
* Analyze user and expert ratings.
* Identify highly rated and high-specification phones.
* Explore different mobile phone price categories.
* Develop a machine learning model to predict mobile phone prices.
* Create an interactive dashboard for data exploration.

---

## 2. Data Source

The project uses a mobile phone dataset containing information about different mobile phone models.

### Dataset Information

| Attribute           | Description                 |
| ------------------- | --------------------------- |
| Phone Name          | Name of the mobile phone    |
| Brand               | Mobile phone brand          |
| Release Date        | Phone release information   |
| Specification Score | Overall specification score |
| Processor           | Processor used in the phone |
| RAM & Storage       | RAM and storage information |
| Rear Camera         | Rear camera specifications  |
| Front Camera        | Front camera specifications |
| Battery             | Battery capacity            |
| Display             | Display specifications      |
| AnTuTu Score        | Performance score           |
| Awards              | Awards received             |
| User Rating         | Rating given by users       |
| Expert Rating       | Rating given by experts     |
| Price               | Mobile phone price          |
| Store               | Store information           |

The original dataset was cleaned and transformed before being used for analysis and machine learning.

---

## 3. Methodology

The project follows these major stages:

### 3.1 Data Collection

The raw mobile phone dataset was imported into Python using Pandas.

### 3.2 Data Cleaning

The dataset was prepared for analysis by:

* Handling missing values
* Cleaning price values
* Converting data into appropriate data types
* Cleaning release-date information
* Removing unnecessary or duplicate data where required

### 3.3 Feature Engineering

New analytical features were created from the original dataset.

These include:

* Brand
* Price in INR
* RAM in GB
* Storage in GB
* Battery capacity in mAh
* Display size in inches
* AnTuTu score
* Rear camera in MP
* Front camera in MP
* User rating
* Expert rating
* Price category

### 3.4 Exploratory Data Analysis

The cleaned dataset was explored using statistical analysis and visualizations.

The analysis includes:

* Number of phones by brand
* Average price by brand
* Price category distribution
* RAM vs Price
* Storage vs Price
* Battery vs Price
* AnTuTu Score vs Price
* Display Size vs Price
* Rear Camera vs Price
* User Rating vs Price
* Expert Rating vs Price
* User Rating Distribution
* Expert Rating Distribution
* Top phones by ratings
* Top phones by specification score

### 3.5 Predictive Modeling

A **Random Forest Regression** model was developed to predict mobile phone prices.

The model uses the following features:

* Brand
* Processor
* Specification Score
* RAM
* Storage
* Battery
* Display Size
* AnTuTu Score
* Rear Camera
* Front Camera
* User Rating
* Expert Rating

Categorical features were processed using **One-Hot Encoding**, while numerical features were handled using appropriate preprocessing techniques.

### 3.6 Model Evaluation

The model is evaluated using:

* **MAE – Mean Absolute Error**
* **RMSE – Root Mean Squared Error**
* **R² Score**

These metrics are used to evaluate the performance of the price prediction model.

### 3.7 Interactive Dashboard

A **Streamlit dashboard** was developed to make the analysis interactive.

The dashboard includes:

* Brand filters
* Price category filters
* Key statistics
* Market analysis
* Specification analysis
* Rating analysis
* Top phone analysis
* Detailed phone data
* Price prediction

The PPT specifically identifies Python tools such as **Streamlit** as suitable for dashboard projects and emphasizes filters, multiple chart types, interactivity, and a clear narrative. 

---

## 4. Key Findings

The project analyzes several important relationships within the mobile phone dataset.

### Market Analysis

The project examines:

* Number of phones available for each brand
* Average price of phones by brand
* Distribution of phones across different price categories

### Specification Analysis

The project investigates how different specifications are related to mobile phone prices, including:

* RAM
* Storage
* Battery capacity
* Display size
* AnTuTu performance score
* Rear camera

### Rating Analysis

The project compares:

* User ratings
* Expert ratings
* Rating distributions
* Highly rated mobile phones

### Top Phones

The dashboard identifies phones with high:

* User ratings
* Expert ratings
* Specification scores

The specific numerical findings should be taken from the final dashboard outputs rather than being assumed in the README.

---

## 5. Results

### Dataset

The final cleaned and transformed dataset contains:

**4,000 records and 27 columns.**

### Dashboard

An interactive **Streamlit dashboard** was developed to analyze:

* Mobile phone prices
* Brands
* Specifications
* Performance
* Ratings
* Price categories

### Machine Learning

A **Random Forest Regression model** was developed to predict mobile phone prices.

### Model Performance

The final model evaluation results should be added here:

| Evaluation Metric |               Result |
| ----------------- | -------------------: |
| MAE               | **Add actual value** |
| RMSE              | **Add actual value** |
| R² Score          | **Add actual value** |

> The actual model results should be taken directly from your Colab output. Do not enter estimated values.

---

## 6. Tools and Technologies

| Technology   | Purpose                             |
| ------------ | ----------------------------------- |
| Python       | Programming and analysis            |
| Pandas       | Data cleaning and manipulation      |
| NumPy        | Numerical operations                |
| Plotly       | Interactive visualizations          |
| Scikit-learn | Machine learning                    |
| Joblib       | Model saving and loading            |
| Streamlit    | Interactive dashboard               |
| Google Colab | Data analysis and model development |
| GitHub       | Project version control             |

The PPT recommends documenting the methodology, maintaining a clean project structure, and using version control such as GitHub. 

---

## 7. Future Scope

The project can be further enhanced by:

* Testing additional machine learning algorithms
* Performing hyperparameter tuning
* Improving prediction performance
* Adding more dashboard filters
* Adding additional visualizations
* Including more mobile phone datasets
* Deploying the Streamlit dashboard online
* Adding more advanced predictive analytics

---
## 8. Conclusion

The **Mobile Phone Analytics** project demonstrates a complete data analytics workflow from raw data to an interactive analytical solution.

The project covers:

**Data Collection → Data Cleaning → Feature Engineering → EDA → Visualization → Machine Learning → Model Evaluation → Interactive Dashboard**

The analysis provides insights into mobile phone prices, specifications, performance, brands, and ratings.

The Streamlit dashboard provides an interactive platform for exploring the dataset, while the Random Forest Regression model provides a machine learning approach for estimating mobile phone prices.

---

## 9. References

1. **Business and Data Analytics – Session 13: Real-World Case Studies & Projects.** Course presentation used as the guideline for project structure, data cleaning, EDA, predictive modeling, dashboard development, documentation, and project presentation. 

2. **Mobile Phone Dataset.** Source dataset used for the Mobile Phone Analytics project, containing mobile phone specifications, ratings, prices, and related information.

3. **Python Documentation.** Python programming language used for data analysis and project development.

4. **Pandas Documentation.** Used for data loading, cleaning, transformation, and analysis.

5. **Plotly Documentation.** Used for creating interactive data visualizations.

6. **Scikit-learn Documentation.** Used for data preprocessing, Random Forest Regression, and model evaluation.

7. **Streamlit Documentation.** Used for developing the interactive Mobile Phone Analytics dashboard.

8. **Joblib Documentation.** Used for saving and loading the trained machine learning model.
