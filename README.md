# 🏎️ F1 Podium Predictor

_Repo: [ipolishc22/f1-strategy-simulator](https://github.com/ipolishc22/f1-strategy-simulator)_

[![MIT License](https://img.shields.io/badge/License-MIT-blue.svg)]()
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-green.svg)]()
[![Model Accuracy](https://img.shields.io/badge/accuracy-TBD-yellow.svg)]()

---

## 🚀 Project Description

**F1 Podium Predictor** is a machine learning pipeline that forecasts the top 3 finishers of a Formula 1 race using race weekend data (Free Practice, Qualifying). It is designed as the first module in a broader F1 race strategy simulation platform.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Installation](#installation)
- [Usage](#usage)
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

This project trains multiple classification models using 2025 Formula 1 race data. It takes cleaned and feature-engineered data from FP3 and Qualifying sessions and compares the performance of different machine learning models in predicting podium outcomes. The long-term goal is to simulate user-defined race scenarios and strategic decisions.

---

## ✨ Key Features

- Automated data collection with **FastF1 API**
- Feature engineering and session data cleaning
- Trains and compares multiple models:
  - Logistic Regression
  - Random Forest
  - Gradient Boosting Classifier
  - (Fourth model TBD)
- Will export best-performing model for race prediction
- Future: integration with dashboard + strategy simulation engine

---

## 🛠 Installation

```bash
git clone https://github.com/ipolishc22/f1-strategy-simulator.git
cd f1-strategy-simulator
pip install -r requirements.txt
```

---

## ⚙️ Usage

1. Run the data pipeline:

   ```bash
   python pipeline.py
   ```

2. Explore modeling and results in Jupyter:

   ```bash
   jupyter notebook notebooks/modeling.ipynb
   ```

3. (Coming Soon) Use a saved model with a script:
   ```bash
   python predict_race.py --race "Spa 2025"
   ```

---

## 📊 Results

Results will be added soon. Metrics such as model accuracy, confusion matrix, and prediction examples will appear here.

---

## 📁 Project Structure

```
.
├── data/                    # Cleaned and master datasets
├── notebooks/               # Data collection and modeling notebooks
├── utils/                   # (internal tools and pipeline logic)
├── pipeline.py              # Main data processing script
├── requirements.txt         # Python dependencies
└── README.md
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

**Will Franko**

- GitHub: [@ipolishc22](https://github.com/ipolishc22)
- LinkedIn: [Your LinkedIn URL here]
- Email: [Your email, optional]

---

## 🛣️ Future Roadmap

- [ ] Expand dataset to include 2021–2024 seasons
- [ ] Add Monte Carlo simulation of race outcomes
- [ ] Develop interactive dashboard for race scenario input
- [ ] Incorporate pit stop strategy and weather simulation

---
