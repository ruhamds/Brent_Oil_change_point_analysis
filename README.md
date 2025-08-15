# 🛢️ Brent Oil Change Point Detection using Bayesian Modeling

This project applies **Bayesian Change Point Detection** on Brent crude oil price data to detect structural breaks and significant shifts. We identify change points using PyMC3, quantify economic impact, and present insights through an interactive dashboard built with **FastAPI** and **React**.

---

## 📁 Project Structure

Brent_Oil_change_point_analysis/
│
├── App/ # Backend + Frontend app
│ ├── backend/ # FastAPI backend
│ │ ├── main.py # FastAPI entry point
│ │ ├── changepoint_results.json # JSON output from Bayesian model
│ │ └── ... # Other backend files
│ │
│ └── frontend/ # React dashboard frontend
│ ├── public/
│ ├── src/
│ │ ├── components/
│ │ │ └── ChangePointChart.js
│ │ ├── App.js
│ │ ├── api.js
│ │ └── index.js
│ ├── package.json
│ └── ...
│
├── Notebooks/ # Jupyter notebooks
│ ├── EDA.ipynb # Task 1: Data Analysis & Preprocessing
│ └── Bayesian_change_point_model.ipynb # Task 2: Modeling
│
├── data/ # Data files
│ └── processed_brent_data.csv # Cleaned log returns dataset
│
├── requirements.txt # Python dependencies
├── requirements-pymc3.txt # PyMC3-specific environment
├── .gitignore
├── README.md
└── changepoint_results.json # Final result for dashboard

---

## ✅ Task 1: Data Preprocessing and EDA

We started with daily Brent crude oil prices and computed **log returns**, cleaned the dataset, and visualized time series properties including:

- Price trends
- Volatility (30-day rolling std)
- Log return distributions

🔍 *Output:* `processed_brent_data.csv`

---

## ✅ Task 2: Bayesian Change Point Detection (PyMC3)

We applied **Bayesian inference** using PyMC3 to detect structural breaks in log returns:

- Implemented a **single change point model**
- Extended to **multiple change point model** (2 tau parameters)
- Verified **model convergence** using trace plots and diagnostics (R-hat, ESS)
- Compared models using **WAIC**
- Quantified economic impact:
  - Mean return shift before/after
  - Approx. price impact per barrel/day

📦 *Output:* `changepoint_results.json`

---

## ✅ Task 3: Interactive Dashboard

We built a modern dashboard with:

- **FastAPI backend** serving change point data
- **React + Recharts frontend** visualizing:
  - Log returns and detected change point
  - Posterior distributions
  - Regime shifts and statistics

To run locally:

### 🔧 Backend (FastAPI)

```bash
cd App/backend
uvicorn main:app --reload

Frontend (React)
Edit
cd App/frontend
npm install
npm start

 Installation
1. Clone the repo
git clone https://github.com/your-username/Brent_Oil_change_point_analysis.git
cd Brent_Oil_change_point_analysis

Setup Python environment (PyMC)
conda create -n pymc_env python=3.9
conda activate pymc_env
pip install -r requirements-pymc3.txt

 Key Technologies
Python, Jupyter, PyMC3, ArviZ

FastAPI (backend API)

React, Recharts (dashboard)

Bayesian inference, time series modeling

References
PyMC3 documentation

ArviZ diagnostics

Energy Information Administration (EIA)

OPEC Newsroom

📬 License
MIT License — free to use and adapt.