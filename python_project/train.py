from sklearn.model_selection import GridSearchCV
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

# Load train data
data = pd.read_excel('../data/train.xlsx')


# Separate features and target variable
X = data.drop('price_range', axis=1)
y = data['price_range']

# Replace them with the "median" value rather than the "mean" to avoid outliers
# Scan for missing values and replace them
for column in data.columns:
    if data[column].dtype == 'object':
        # Calculate the mode and replace missing values
        mode_value = data[column].mode()[0]
        data[column].fillna(mode_value, inplace=True)
    else:  # Numerical columns
        # Calculate the median and replace missing values
        median_value = data[column].median()
        data[column].fillna(median_value, inplace=True)

# Split the data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(
    X, y, test_size=0.2, random_state=42)


# Choose a random forest classifier
model = RandomForestClassifier(random_state=42)
# Train the model using the training set
model.fit(X_train.values, y_train.values)

# Model Evaluation
# Make predictions on the validation set
y_pred = model.predict(X_val.values)

# Calculate accuracy
accuracy = accuracy_score(y_val, y_pred)
print(f'Accuracy: {accuracy}')

# Print classification report
print(classification_report(y_val, y_pred))

# Print confusion matrix
print(confusion_matrix(y_val, y_pred))

# Model Optimization
# Tune the model's hyperparameters using techniques such as grid search or random search

# Define the parameter grid
param_grid = {
    'n_estimators': [50, 100, 150],
    'max_depth': [None, 10, 20],
    'min_samples_split': [2, 4, 6]
}

# Perform grid search
grid_search = GridSearchCV(model, param_grid, cv=3)
grid_search.fit(X_train, y_train)

# Use the best parameters found during optimization to retrain the model.
best_model = grid_search.best_estimator_
best_model.fit(X_train, y_train)

# Model Deployment as RESTful API
# Save the trained model using pickle or joblib so that it can be loaded later for prediction.
joblib.dump(best_model, 'model.joblib')
