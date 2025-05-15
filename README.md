# 💼 Salary Prediction Web App

This is a simple Flask-based web application that predicts a person's salary based on years of experience. The prediction is powered by a machine learning model trained using Python and scikit-learn.

---

## 🚀 Demo

The app allows users to input years of experience and returns a predicted salary using a trained linear regression model.

---

## 📁 Project Structure
├── [app.py](https://github.com/BandaJithendra/Salary_Prediction_Web_APP/blob/main/app.py) # Main Flask application<br/>
├── [app.ipynb](https://github.com/BandaJithendra/Salary_Prediction_Web_APP/blob/main/app.ipynb) # Machine learning model Training<br/>
├── [model.pkl](https://github.com/BandaJithendra/Salary_Prediction_Web_APP/blob/main/model.pkl) # Trained machine learning model (Linear Regression)<br/>
├── templates/<br/>
│ ├── [index.html](https://github.com/BandaJithendra/Salary_Prediction_Web_APP/blob/main/templates/index.html) # Input form UI<br/>
│ └── [login.html](https://github.com/BandaJithendra/Salary_Prediction_Web_APP/blob/main/templates/login.html) # Output display<br/>
└── requirements.txt # List of Python dependencies<br/>


---

## 🧠 Machine Learning Model

- **Algorithm**: Linear Regression
- **Input Feature**: Years of Experience
- **Target Output**: Salary

The model was trained on a dataset containing `YearsExperience` and `Salary`, and serialized using `pickle`.

---

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML/Jinja2
- Scikit-learn
- Pickle

---

## 🔧 Setup Instructions

```bash
# 1. Clone the Repository
git clone https://github.com/yourusername/salary-prediction-app.git
cd salary-prediction-app

# 2. Create a Virtual Environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install Dependencies
pip install -r requirements.txt

# 4. Run the Application
python app.py