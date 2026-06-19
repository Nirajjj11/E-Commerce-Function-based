import joblib
import os
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, "stock_model.pkl")

model = joblib.load(MODEL_PATH)

FESTIVAL_MONTHS = [10, 11, 12]


def predict_stock(sales_last_30_days, current_stock):
      current_month = datetime.now().month

      festival_flag = 1 if current_month in FESTIVAL_MONTHS else 0

      prediction = model.predict([[
            sales_last_30_days,
            current_stock,
            current_month,
            festival_flag
      ]])

      return round(prediction[0], 2)