# Multi-Sport Performance Predictor

## Overview

Multi-Sport Performance Predictor is a machine learning based Streamlit application that predicts a fantasy-style performance score for players across three sports:

- Cricket
- Basketball
- Football

The application uses separate sport-specific Random Forest regression models because each sport has different performance metrics, datasets, and prediction logic.

---

## Features

- Sport selection from sidebar
- Dynamic input fields based on selected sport
- Separate ML model for each sport
- Predicted performance score
- Model R² score display
- Expected performance range
- Interactive Plotly performance comparison chart
- Input validation for unrealistic values
- Clean and responsive Streamlit UI

---

## Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- RandomForestRegressor
- Joblib
- Plotly

---

## Supported Sports and Inputs

### Cricket

The cricket model predicts batting performance.

Inputs:

- Balls faced
- Fours
- Sixes

Output:

- Predicted batting performance score

---

### Basketball

The basketball model predicts fantasy performance using historical player averages.

Inputs:

- Average points
- Average assists
- Average rebounds
- Average minutes played

Output:

- Predicted basketball performance score

Model R² score:


0.412

## Football

The football model predicts fantasy-style performance using attacking, creative, progressive, defensive, and discipline metrics.

### Inputs

- Minutes played
- Expected goals
- Expected assisted goals
- Shots on target
- Key passes
- Shot-creating actions
- Progressive carries
- Progressive passes
- Progressive receptions
- Tackles
- Interceptions
- Yellow cards
- Red cards

### Output

- Predicted football performance score

### Model R² Score


0.961

**Machine Learning Approach**

This is a regression-based project because the output is a numerical performance score.

The project uses RandomForestRegressor because sports data is usually non-linear, noisy, and dependent on interactions between multiple features.

Each sport has a separately trained model:

cricket_model.pkl
basketball_model.pkl
football_model.pkl

Although the same algorithm is used, each model is trained on different sport-specific datasets and features.

What is Fantasy Performance Score?

A fantasy performance score is a single numerical value that represents a player's overall contribution.

It combines important performance actions into one score.

Examples:

Cricket: balls, fours, sixes
Basketball: points, assists, rebounds, minutes
Football: xG, xAG, shots, key passes, tackles, interceptions, cards

This makes it easier to compare overall player impact across different sports.

**Model Evaluation**

The models are evaluated using regression metrics:

R² Score
Mean Absolute Error

R² score is used because the project predicts numerical values, not categories.

This project does not use classification accuracy because it is not a classification problem.

**Project Workflow**
Dataset Collection
        ↓
Data Cleaning
        ↓
Feature Engineering
        ↓
Fantasy Score Creation
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Model Saving
        ↓
Streamlit App Integration
        ↓
Prediction and Visualization

**Folder Structure**
multi_sport_predictor/
│
├── app.py
├── cricket_model.pkl
├── basketball_model.pkl
├── football_model.pkl
├── requirements.txt
└── README.md

**How to Run Locally**

1. Clone the Repository
```bash git clone <your-repository-link>

2. Move into the P
3. Install Dependencies
```bash pip install -r requirements.txt
4. Run the Streamlit App
```bash streamlit run app.py

**Requirements**
streamlit
pandas
numpy
scikit-learn
joblib
plotly
