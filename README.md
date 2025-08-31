# 🏎️ F1 Podium Predictor

_Repo: [ipolishc22/f1-podium-predictor](https://github.com/ipolishc22/f1-podium-predictor)_

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)]()

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [How It Works](#how-it-works)
- [Results](#results)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Data Sources](#data-sources)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)
- [Future Roadmap](#future-roadmap)

---

## 🏁 Overview

F1 Podium Predictor is a machine learning pipeline that forecasts the top 3 finishers of a Formula 1 race using race weekend data (FP2, Qualifying).  
It trains multiple classification models, compares their performance, and currently achieves a top-3 prediction accuracy of ~78%.  
This is the first step toward a larger race strategy simulation platform.

---

## ✨ Key Features

- Automated data collection with **FastF1 API**
- Feature engineering and session data cleaning
- Trains and compares multiple models:
  - Random Forest
  - Gradient Boosting Classifier
  - Logistic Regression
  - Logistic Regression (Without Qualifying Position)
- Will export best-performing model for race prediction
- Future: integration with dashboard + strategy simulation engine

---

## 🛠 How It Works

The project is organized into Jupyter notebooks and utility scripts that cover the full workflow — from data collection and model training to real-time race prediction and continuous model updates.

---

### 1. **Data Collection** – `notebooks/data_collection.ipynb`

- Uses the **FastF1 API** to fetch Free Practice 2 and Qualifying session data.
- Performs feature engineering and compiles data into a structured format.
- Saves the output to `data/master_dataset_2025.csv`.

---

### 2. **Modeling** – `notebooks/modeling.ipynb`

- Trains and compares multiple classification models:
  - Random Forest
  - Gradient Boosting
  - Logistic Regression (with and without Qualifying Position)
- Evaluates model performance using classification reports and F1 scores.

---

### 3. **Race Predictions**

- `notebooks/predict_r13_r14_belgian_hungarian.ipynb`
- `notebooks/predict_r15_dutch.ipynb`

- Each prediction notebook uses session data available **before** the race.
- Loads the appropriate model and scaler (e.g., `logreg_scaled_quali_pre_r15_netherlands.pkl`).
- Applies the model to the pre-race data to predict each driver's probability of finishing on the podium.
- Outputs a sorted table with podium probabilities and highlights the predicted Top 3 finishers.

---

### 4. **Model Updating** – `notebooks/update_model_for_race.ipynb`

- After a Grand Prix is completed, this notebook:
  - Adds the official race results to the training dataset.
  - Retrains the model on the updated dataset (optionally).
  - Outputs a new `.pkl` model and scaler for use in the next prediction.

---

### 5. **Reusable Pipeline Functions** – `utils/pipeline.py`

- Centralizes helper functions used across all notebooks:
  - Scaling and preprocessing
  - Probability prediction
  - Sorting and formatting output
- Promotes modular, reusable code and consistent results.

> ⚠️ Note: This is an early version of the project meant as a **portfolio showcase**. While the notebooks are runnable with the included `requirements.txt`, the code is still under development and may require additional setup (e.g., FastF1 API configuration and race data updates).

---

## 📊 Results

| Model                          | Precision (Podium) | Recall (Podium) | F1-Score | Accuracy |
| ------------------------------ | ------------------ | --------------- | -------- | -------- |
| Random Forest                  | 1.00               | 0.43            | 0.60     | 0.91     |
| Gradient Boosting              | 1.00               | 0.43            | 0.60     | 0.91     |
| Logistic Regression (Quali)    | 0.54               | 1.00            | 0.70     | 0.87     |
| Logistic Regression (No Quali) | 0.22               | 0.71            | 0.33     | 0.57     |

Best performing model: Logistic Regression (with Qualifying Position) → 78% podium accuracy across the 2025 season.

---

## 📁 Project Structure

```
├── data/
│   ├── master_dataset_2025.csv                    # Full dataset used for training
│   ├── r13_belgium_2025.csv                       # Race-specific input data for predictions (Round 13)
│   ├── r14_hungary_2025.csv                       # Race-specific input data for predictions (Round 14)
│   ├── r15_netherlands_2025.csv                   # Race-specific input data for predictions (Round 15)
│
├── models/
│   ├── logreg_scaled_quali_pre_r13_belgium.pkl    # Logistic Regression model before Belgium GP
│   ├── logreg_scaled_quali_pre_r14_hungary.pkl    # Logistic Regression model before Hungary GP
│   ├── logreg_scaled_quali_pre_r15_netherlands.pkl# Logistic Regression model before Netherlands GP
│   ├── scaler.pkl                                 # Original scaler used for predicting Belgian and Hungarian GPs
│   ├── scaler_pre_r15_netherlands.pkl             # Scaler used for Netherlands GP
│
├── notebooks/
│   ├── data_collection.ipynb                      # Data loading and preprocessing notebook
│   ├── modeling.ipynb                             # Model training, evaluation, and saving
│   ├── predict_r13_r14_belgian_hungarian.ipynb    # Prediction notebook for Belgium & Hungary
│   ├── predict_r15_dutch.ipynb                    # Prediction notebook for Netherlands GP
│   ├── update_model_for_race.ipynb                # Retrains model with new race data
│
├── utils/
│   ├── pipeline.py                                # File containing all the custom helper functions
│
├── requirements.txt                               # Python dependencies
├── .gitignore                                     # Git ignore rules
├── LICENSE                                        # Project license
├── README.md                                      # Project overview and instructions

```

---

## 💻 Tech Stack

- Python 3.10+
- pandas, NumPy
- scikit-learn
- matplotlib, seaborn
- FastF1
- Jupyter Notebook

---

## 📦 Data Sources

- [FastF1 API](https://theoehrly.github.io/Fast-F1/) – timing, weather, and session data from Formula 1
- 2025 Formula 1 season (race weekend data)

---

## 🤝 Contributing

Contributions are welcome!  
To contribute:

```bash
1. Fork the repository
2. Create a new branch (`git checkout -b feature-xyz`)
3. Commit your changes
4. Push to your fork
5. Open a Pull Request
```

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 📬 Contact

**Illia Polishchuk**

- [LinkedIn](https://www.linkedin.com/in/illia-polishchuk-4065802a0)
- [GitHub](https://github.com/ipolishc22)
- Email: illia.polishchuk22@gmail.com

---

## 🛣️ Future Roadmap

- [ ] Expand dataset to include 2022–2024 seasons
- [ ] Explore scenario simulation for race strategies (e.g., different tire compounds, safety cars)
- [ ] Develop interactive dashboard for race scenario input
- [ ] Incorporate pit stop strategy and weather simulation

---

```

```
