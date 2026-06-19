import joblib
import random
from sklearn.ensemble import RandomForestRegressor

X = []
y = []

for i in range(300):
      sales_last_30_days = random.randint(20, 500)
      current_stock = random.randint(10, 300)
      month = random.randint(1, 12)
      festival_flag = random.randint(0, 1)

      X.append([
            sales_last_30_days,
            current_stock,
            month,
            festival_flag
      ])

      predicted = (sales_last_30_days / 30 * 7) + (festival_flag * 20)

      y.append(predicted)

model = RandomForestRegressor(n_estimators=100,random_state=42)

model.fit(X, y)

joblib.dump(model, "ml/stock_model.pkl")

print("Stock model trained successfully")