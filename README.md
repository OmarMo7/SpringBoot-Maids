# SpringBoot and Python Integration Project

This project demonstrates the integration between a SpringBoot application and a Python Flask application. It is structured to showcase how both technologies can work together to handle data processing, model training, and prediction tasks.

## Project Structure

The project is organized into several key directories:

- **SpringBoot_project**: Contains the SpringBoot application.
  - **src**: Includes the main controller and the Device entity.
  - **pom.xml**: Maven project file with project configuration and dependencies.
- **python_project**: Contains the Python Flask application.
  - **EDA_analysis**: Contains some exploratory data analysis performed on the data.
  - **train.py**: Handles data loading, preprocessing, model training, optimization, and model exportation.
  - **predict.py**: Performs testing with the model on random samples from the test data.
  - **app.py**: Contains Flask endpoints for model predictions based on the request body's data.
- **data**: Directory for storing datasets used in the project.
- **venv**: Python virtual environment for managing dependencies.

## Dependencies

### Python Dependencies

Ensure you have the following Python packages installed:

- Flask
- Joblib
- scikit-learn
- seaborn
- pandas
- matplotlib

You can install these packages using pip:

```bash
pip install Flask Joblib scikit-learn seaborn pandas matplotlib
```

## Database
- sqlite3

## Testing endpoints

1. **URL**: http://localhost:5000/devices **method**=GET **description**: Getting all devices in the databases
2. **URL**: http://localhost:5000/devices/1 **method**=GET **description**: Getting a specific device
3. **URL**: http://localhost:5000/devices/ **method**=POST **description**: Add a new device
4. **URL**: http://localhost:5000/predict/ **method**=POST **description**: Predict the price of the device given its features

**NOTE:**

- For the 3rd endpoint, request body should look something like this JSON format:

```JSON
{
    "battery_power": 1002,
    "blue": 1,
    "clock_speed": 2.9,
    "dual_sim": 1,
    "fc": 0,
    "four_g": 0,
    "int_memory": 9,
    "m_dep": 0.1,
    "mobile_wt": 182,
    "n_cores": 5,
    "pc": 1,
    "px_height": 248,
    "px_width": 874,
    "ram": 3946,
    "sc_h": 5,
    "sc_w": 2,
    "talk_time": 2,
    "three_g": 7,
    "touch_screen": 0,
    "wifi": 0,
    "price_range": 0
}
```

- For the 4th endpoint, request body will be the same except for the last feature, as this is the feature that is going to be predicted:

```JSON
{
    "battery_power": 1002,
    "blue": 1,
    "clock_speed": 2.9,
    "dual_sim": 1,
    "fc": 0,
    "four_g": 0,
    "int_memory": 9,
    "m_dep": 0.1,
    "mobile_wt": 182,
    "n_cores": 5,
    "pc": 1,
    "px_height": 248,
    "px_width": 874,
    "ram": 3946,
    "sc_h": 5,
    "sc_w": 2,
    "talk_time": 2,
    "three_g": 7,
    "touch_screen": 0,
    "wifi": 0
}
```
