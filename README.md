# Developer Salary Prediction (Stack Overflow 2024 Survey)

## What This Project Does

This project builds a machine learning model to predict developers’ annual compensation using responses from the 2024 Stack Overflow Developer Survey.  
It combines **data cleaning**, **feature engineering**, and **CatBoost regression** to explore how factors such as experience, education, role, company size, and work arrangement relate to salary.

Specifically, the project:

- Loads and preprocesses survey data.
- Cleans and encodes categorical variables.
- Engineers new features (e.g., years of experience squared, interaction variables).
- Splits data into training and test sets.
- Trains a CatBoost regression model.
- Evaluates prediction performance (R², RMSE).
- Visualizes feature importance.

This approach demonstrates how to apply a tree-based model to real-world survey data.

---

## Dataset Description

This project uses the public dataset from the 2024 Stack Overflow Developer Survey, which collected responses from over 65,000 developers worldwide ([survey.stackoverflow.co](https://survey.stackoverflow.co)).  
For this analysis, the data was filtered to focus on **U.S. respondents with valid salary data**.

The dataset includes encoded features representing developer roles, education, years of experience, company size, and remote work status.  
Additional **engineered features** were created to improve predictive power, such as experience squared and interaction terms.

---

## Modeling Approach

I tested several regression algorithms and selected **CatBoost**, which is well-suited to handling categorical variables and capturing nonlinear relationships.

**Key modeling details:**

- **Algorithm:** CatBoost Regressor
- **Hyperparameters:**
  - `iterations = 2000`
  - `learning_rate = 0.005`
  - `depth = 10`
  - `early_stopping_rounds = 200`
- **Train/test split:** 80/20

After tuning and feature engineering, the model achieved:

- **R² = 0.319** (explains ~31.9% of salary variance)
- **RMSE ≈ $57,385**

This performance demonstrates the model captures meaningful relationships but also reflects the complexity and variability of compensation data.

---

## Key Features Used

The final model included these predictors:

- `years_code_pro_sq` – Years of professional experience squared
- `dev_type_grouped` – Developer role (grouped, rare roles as "Other")
- `org_size_label` – Company size (e.g., "10–19 employees")
- `ed_level_label` – Education level (e.g., Bachelor’s, Master’s)
- `remote_work_label` – Remote, Hybrid, or In-person
- `seniority_bucket` – Derived seniority (Junior, Mid, Senior)
- `seniority_remote` – Interaction: seniority × remote status
- `seniority_orgsize` – Interaction: seniority × company size

Feature importance analysis indicated that experience, developer type, and seniority interactions were the most influential factors in predicting salary.

---

## Instructions to Run

1. **Install Libraries**

   In R:
   ```r
   install.packages(c("catboost", "ggplot2", "dplyr"))
   ```

2. **Load Data**

   Use the provided `survey_us_salary_filtered.csv`.

3. **Run Model**

   - Preprocess data (factor encoding, feature engineering)
   - Split into training and testing sets
   - Train CatBoost with tuned parameters
   - Evaluate performance using R² and RMSE

4. **Interpret Results**

   - Review feature importance plots
   - Analyze prediction accuracy and error patterns

---

## Code Files

- `ProjectcheckpointC12.Rmd` – Final modeling and feature engineering notebook
- `survey_us_salary_filtered.csv` – Cleaned dataset used for modeling

---

## Notes

This project demonstrates an applied approach to salary prediction using real-world survey data and machine learning.  
It can be extended by incorporating additional features (e.g., geographic location, technology stack) or experimenting with different model architectures.