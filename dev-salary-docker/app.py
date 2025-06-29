from fastapi import FastAPI
from pydantic import BaseModel
import catboost
import pandas as pd

# Initialize FastAPI app
app = FastAPI()

# Load your CatBoost model
model = catboost.CatBoostRegressor()
model.load_model("developer_salary_model.cbm")

# Define expected input schema
class SalaryInput(BaseModel):
    years_code_pro_sq: float
    dev_type_grouped: str
    org_size_label: str
    ed_level_label: str
    remote_work_label: str
    seniority_bucket: str
    seniority_remote: str
    seniority_orgsize: str

@app.post("/predict")
def predict_salary(input: SalaryInput):
    # Convert input to DataFrame
    df_input = pd.DataFrame([input.dict()])

    # Make prediction
    pred = model.predict(df_input)

    return {"predicted_salary": pred[0]}
