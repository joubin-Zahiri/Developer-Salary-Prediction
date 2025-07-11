# Developer Salary Prediction (Stack Overflow 2024 Survey)

## Project Overview

This project builds a machine learning model to predict developers’ annual compensation in the United States, using data from the 2024 Stack Overflow Developer Survey. It applies XGBoost regression along with data preprocessing and basic feature engineering to understand how factors such as experience, education, developer role, company size, and remote work status influence salary.

The R Markdown file used for this analysis is named `Final_code.Rmd`.

### Key Project Steps

- Load and filter the raw survey dataset
- Retain only U.S.-based responses with valid salary data
- Encode categorical variables as factors
- Engineer a squared experience term (`years_code_pro_sq`) to capture nonlinear effects
- Split the data into training and testing sets (80/20)
- Train an XGBoost regression model with tuned hyperparameters
- Evaluate model performance using R² and RMSE

Note: While feature importance was computed during modeling, no visualizations of feature importance were included in this version.

The main goal of this project was to develop a Shiny app that allows users to input key features and receive a predicted salary based on the trained model.

---

## Dataset Description

This project uses the public dataset from the 2024 Stack Overflow Annual Developer Survey, which gathered responses from over 65,000 developers worldwide in May 2024.

For this project, the dataset was filtered to include:
- Only respondents from the United States
- Only responses with non-missing salary values

After cleaning and filtering, the final dataset contained over 4,400 responses.

Key variables used in the model:
- `years_code_pro` — Years of professional coding experience
- `dev_type_label` — Developer role
- `ed_level_label` — Education level
- `org_size_label` — Company size
- `remote_work_label` — Work arrangement
- `years_code_pro_sq` — Experience squared (engineered feature)

---

## Modeling Approach

### Why XGBoost?

After testing various regression models, XGBoost was selected due to its:
- Ability to handle categorical and numeric variables (after appropriate preprocessing)
- Capacity to model nonlinear relationships
- Strong performance with imbalanced and noisy survey data

### Model Configuration

- Algorithm: XGBoost Regressor
- Train/Test Split: 80/20
- Engineered Feature: `years_code_pro_sq` (experience squared)

### Performance Metrics

- R²: 0.319 (explains approximately 31.9% of the variance in salaries)
- RMSE: ~$57,385

The relatively modest R² is expected given the nature of the survey data, which contains many categorical variables and other unobserved factors that influence compensation. Despite this, the model identifies important patterns and provides a meaningful basis for interactive prediction.

---

## Shiny App Deployment

This model is deployed in a live Shiny application. Users can enter their information (role, education, experience, company size, work setup) to estimate their expected salary based on the trained model.

Use the app here:  
**[Launch Salary Predictor](https://huggingface.co/spaces/joooobin/salary-predictor-shiny)**

---

## Data Source and Metadata

This dataset was curated as part of the #TidyTuesday project. The data includes:
- 65,000+ developer responses
- Cleaned single-response questions
- Integer-encoded variables with label mappings via a crosswalk file

More information and raw data files are available on the TidyTuesday GitHub repository:  
https://github.com/rfordatascience/tidytuesday/tree/master/data/2024/2024-09-03

Key files:
- `stackoverflow_survey_single_response.csv`: Main dataset used
- `qname_levels_single_response_crosswalk.csv`: Categorical value labels
- `stackoverflow_survey_questions.csv`: Full list of survey questions
