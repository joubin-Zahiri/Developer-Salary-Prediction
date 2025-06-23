# Developer Salary Prediction (Stack Overflow 2024 Survey)

## Dataset Description

I use the public dataset from the 2024 Stack Overflow Developer Survey, which collected responses from over 65,000 developers worldwide ([survey.stackoverflow.co](https://survey.stackoverflow.co)). For this project, the data was filtered to focus on **U.S. respondents with valid salary data**.

The dataset includes cleaned and encoded features representing developer roles, education level, years of experience, company size, and remote work status. For example, raw survey entries like `DevType`, `EdLevel`, `YearsCodePro`, and `OrgSize` were transformed into structured categories like `dev_type_grouped`, `ed_level_label`, `years_code_pro`, and `org_size_label`. The target variable is **annual compensation** (`ConvertedCompYearly`), standardized to USD.

---

## Modeling Approach

I tested several regression algorithms:

- Linear Regression  
- Random Forest  
- XGBoost  
- LightGBM  
- **CatBoost** (best performance)

CatBoost was selected as the final model because it handles categorical features and nonlinear relationships effectively. After tuning, the model achieved:

- **R² = 0.339** (explaining ~33.9% of salary variance)  
- **RMSE ≈ 55,359 USD**

---

## Key Features Used

The most important predictors of salary were:

- `years_code_pro`: Years of professional coding experience  
- `dev_type_grouped`: Developer role  
- `org_size_label`: Company size  
- `ed_level_label`: Education level  
- `remote_work_label`: Remote, hybrid, or in-person  
- `seniority_bucket`: Derived from experience years

---

## Feature Importance Insights

Top influencing features based on the CatBoost model:

- **Highest**: `dev_type_grouped`, `years_code_pro`, `seniority_bucket`  
- **Moderate**: `org_size_label`, `ed_level_label`  
- **Lowest**: `remote_work_label`

This reflects common salary patterns—experience and role matter most.

---

## Instructions to Run

1. **Install Libraries**  
   In R: `catboost`, `ggplot2`, `dplyr`, etc.

2. **Load Data**  
   Use `survey_us_salary_filtered.csv` included in this repository.

3. **Run Model**  
   - Split into train/test (80/20)  
   - Use CatBoost with parameters like:
     - `iterations = 1000`
     - `learning_rate = 0.03`
     - `depth = 6`
   - Evaluate using R² and RMSE

4. **Visualize Results**  
   Plot feature importances or use SHAP values for interpretation.

---

## Code Files

- `ProjectcheckpointC5.Rmd`: Draft version submitted during Checkpoint C. Not the final model.
- `survey_us_salary_filtered.csv`: Cleaned dataset used for modeling.

---

## Note

This project demonstrates a practical approach to salary prediction using real-world data. The `.Rmd` file included reflects work-in-progress. Final model may be in a separate file or used in live demos.
