
# Student Placement Prediction Web App

## Overview
This is a Flask-based web application that predicts whether a student is likely to be placed in a job based on input features such as age, gender, academic stream, internship experience, hostel status, CGPA, and backlog history. The application uses a Decision Tree Classifier trained on a dataset's features to make predictions.

![image](https://github.com/user-attachments/assets/6eafd86a-2e85-472a-95af-8cc69706939c)


## Features
- **Input Form**: Allows users to enter student details, including age, gender, stream, internship count, hostel status, CGPA, and backlogs, through a web interface.
- **Prediction**: Predicts placement status (e.g., "Placed" or "Not Placed") using a trained Decision Tree Classifier.
- **Web Interface**: Built with Flask and rendered using an HTML template (`placement.html`).
- **Dataset**: Uses a local dataset (`studentPlacement.csv`) for training the model.


## Requirements
To run this project, you need the following Python packages:
- Flask
- NumPy
- Pandas
- Scikit-learn

You can install the dependencies using:
```bash
pip install flask pandas numpy scikit-learn
```

## Project Structure
- **app.py**: The main Flask application that contains the logic for loading the dataset, training the model, and handling web requests.
- **templates/placement.html**: The HTML template used for the web interface (not included in this file but required for rendering).
- **studentPlacement.csv**: The dataset file containing student placement data (must be present in the project directory).
- **README.md**: This file, providing an overview and instructions for the project.

## How It Works
1. The application loads the student placement dataset from a local CSV file (`studentPlacement.csv`).
2. A Decision Tree Classifier is trained on the dataset's features (age, gender, stream, internship, hostel, CGPA, backlog) to predict placement status.
3. Users access the web interface at the root URL (`/`), where they can input student details.
4. Upon form submission, the app processes the input, makes a prediction, and displays the predicted placement status on the same page.

## Usage
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/lovnishverma/placement-prediction.git
   cd placement-prediction
   ```

2. **Prepare the Dataset**:
   Ensure the `studentPlacement.csv` file is placed in the project directory.

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Web App**:
   Open a browser and navigate to `http://127.0.0.1:5000`.

6. **Input Student Details**:
   Enter the required details (age, gender, stream, internship, hostel, CGPA, backlog) in the form, then submit to see the predicted placement status.

## Notes
- Ensure the `placement.html` template is present in the `templates` folder, as it is required for rendering the web interface.
- The dataset (`studentPlacement.csv`) must be available in the project directory, as the app reads it locally.
- The `eval` function is used to parse some form inputs, which is not recommended for production due to security risks. Consider using safer alternatives like `float` or `int` for parsing in a production environment.
- The dataset's structure is assumed to have features in the first columns and the target variable (placement status) in the last column, with the second-to-last column excluded (as per the code).

## License
This project is licensed under the MIT License.
