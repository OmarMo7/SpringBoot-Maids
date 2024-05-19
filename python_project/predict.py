import pandas as pd
import numpy as np
import joblib


model = joblib.load('model.joblib')
test_data = pd.read_excel('../data/test.xlsx')

test_data = test_data.drop("id", axis=1)
random_samples = test_data.sample(n=10, random_state=42)

predictions = model.predict(random_samples)

# Convert predictions to a DataFrame
predictions_df = pd.DataFrame(predictions, columns=['Predicted'])

# Reset index on random_samples to align with predictions DataFrame
random_samples.reset_index(drop=True, inplace=True)

# Concatenate the original data with predictions for display
result_df = pd.concat([random_samples, predictions_df], axis=1)
print(result_df)