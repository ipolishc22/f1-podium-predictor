# 🏎️ F1 Podium Predictor

_Repo: [ipolishc22/f1-strategy-simulator](https://github.com/ipolishc22/f1-strategy-simulator)_

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)]()
[![Model Accuracy](https://img.shields.io/badge/accuracy-0.78-yellow.svg)]()

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

The project is organized into Jupyter notebooks and utility scripts that cover the full workflow:

1. **Data Collection** – `notebooks/data_collection.ipynb`

   - Uses the **FastF1 API** to fetch Free Practice 2 and Qualifying data.
   - Performs feature engineering and compiles everything into a master dataset (`data/master_f1_dataset_2025.csv`).

2. **Modeling** – `notebooks/modeling.ipynb`

   - Trains and compares multiple machine learning models (Random Forest, Gradient Boosting, Logistic Regression).
   - Evaluates performance using classification reports and confusion matrices.
   - Saves the best-performing model into the `models/` directory.

3. **Prediction** – `notebooks/next_race_predict.ipynb`
   - Loads the saved Logistic Regression model.
   - Applies it to the latest session data to generate podium predictions for upcoming races (e.g., Belgian GP).

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
f1-strategy-simulator/
├── data/
│   └── master_f1_dataset_2025.csv       # Master dataset used for training and prediction
│
├── models/
│   └── podium_predictor_logistic_regression.pkl  # Trained logistic regression model (serialized)
│
├── notebooks/
│   ├── data_collection.ipynb            # Collects and preprocesses race weekend data
│   ├── modeling.ipynb                   # Feature engineering and model training
│   └── next_race_predict.ipynb          # Loads trained model and generates podium predictions
│
├── utils/
│   └── pipeline.py                      # Python module for data fetching, cleaning, and dataset creation
│
├── .gitignore                           # Specifies untracked files (e.g., __pycache__, .DS_Store)
├── requirements.txt                     # Project dependencies
├── LICENSE                              # License information
└── README.md                            # Project documentation (you're reading it!)
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
- [ ] Add Monte Carlo simulation of race outcomes
- [ ] Develop interactive dashboard for race scenario input
- [ ] Incorporate pit stop strategy and weather simulation

---

```

```
