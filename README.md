# SpringBoot and Python Integration Project

This project demonstrates the integration between a SpringBoot application and a Python Flask application. It is structured to showcase how both technologies can work together to handle data processing, model training, and prediction tasks.

## Project Structure

The project is organized into several key directories:

- **SpringBoot_project**: Contains the SpringBoot application.
  - **src**: Includes the main controller and the Device entity.
  - **pom.xml**: Maven project file with project configuration and dependencies.
- **python_project**: Contains the Python Flask application.
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
