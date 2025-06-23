# Developer Salary Prediction (Stack Overflow 2024 Survey)

## Dataset Description

I use the public dataset from the 2024 Stack Overflow Developer Survey, which collected responses from over 65,000 developers worldwide ([survey.stackoverflow.co](https://survey.stackoverflow.co)). For this project, the data was filtered to focus on **U.S. respondents with valid salary data**.

The dataset includes cleaned and encoded features representing developer roles, education level, years of experience, company size, and remote work status. For example, raw survey entries like `DevType`, `EdLevel`, `YearsCodePro`, and `OrgSize` were transformed into structured categories like `dev_type_grouped`, `ed_level_label`, `years_code_pro`, `org_size_label`, etc. The target variable is **annual compensation** (`ConvertedCompYearly`), standardized to USD.

---

## Modeling Approach

I tested multiple regression algorithms, including:

- Linear Regression  
- Random Forest  
- XGBoost  
- LightGBM  
- **CatBoost** (best performance)

CatBoost was selected as the final model due to its ability to handle categorical variables and nonlinear relationships effectively. After tuning, the model achieved:

- **R² = 0.339** (explains ~33.9% of salary variance)
- **RMSE ≈ 55,359 USD**

This result indicates the model captures some important salary drivers, though unexplained variability remains — expected given the complexity of compensation.

---

## Key Features Used

The most important predictors of salary were:

- `years_code_pro` – Years of professional coding experience  
- `dev_type_grouped` – Developer role (grouped)  
- `org_size_label` – Organization size (e.g., "10–19 employees")  
- `ed_level_label` – Education level (e.g., Master’s, Bachelor’s)  
- `remote_work_label` – Remote, Hybrid, or In-person  
- `seniority_bucket` – Derived seniority (Junior, Mid, Senior)

These features were selected for their known relationship to pay. Experience and role were especially influential, while remote status had relatively low impact.

---

## Feature Importance Visualization

The CatBoost model’s feature importance plot showed:

- **Top factors**: `dev_type_grouped`, `years_code_pro`, `seniority_bucket`  
- **Moderate factors**: `org_size_label`, `ed_level_label`  
- **Lowest impact**: `remote_work_label`

This aligns with common salary patterns in tech — what you do and how long you’ve done it matters most.

---

## Instructions to Run

1. **Setup**  
   Install required libraries (in R or Python). In R:  
   - `tidyverse`, `catboost`, `ggplot2`, etc.

2. **Load Data**  
   Download the 2024 Stack Overflow survey (CSV).  
   Filter to U.S. responses with valid salary data.  
   Encode relevant fields and create `seniority_bucket`.  
   Remove or handle missing values.

3. **Train Model**  
   Split into train/test sets (e.g., 80/20).  
   Use CatBoost with tuned hyperparameters  
   (e.g., iterations = 1000, learning_rate = 0.03, depth = 6).  
   Specify categorical columns (CatBoost handles them natively).  
   Fit model on training set.

4. **Evaluate**  
   On test set, compute:  
   - R² (Coefficient of determination)  
   - RMSE (Root Mean Squared Error)  
   Feature importances can be extracted with `model.get_feature_importance()`.

5. **Visualize & Interpret** (Optional)  
   Create bar plots of feature importance or use SHAP values for deeper insight.  
   Discuss patterns — e.g., how experience or company size affects predictions.

---

This project provides a hands-on, interpretable example of salary prediction using real-world data and machine learning. It can be extended or modified to explore new features, try different models, or fine-tune the approach for better accuracy.
