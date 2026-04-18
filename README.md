# 🧠 Social Media & Mental Health Analyzer

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21E?style=for-the-badge&logo=huggingface&logoColor=black)

</div>

---

> **Can your scrolling habits predict your mental health?**  
> This project answers that — with real data, machine learning, and a live AI assistant.

---

## 📌 What This Project Does

Most mental health tools are either too clinical or too generic.  
This project bridges the gap — it takes your **daily social media habits** and tells you **how they're affecting your mental health**, backed by data and ML.

- 📊 Analyzes patterns between social media use, sleep, stress, and depression
- 🤖 Predicts your **depression risk level** (Low / Medium / High)
- 🗄️ Stores and queries data using **SQL**
- 💬 Includes a **live AI chatbot** (Nova — powered by LLaMA 3.1) for mental wellness conversations
- 🌐 Fully deployed as an interactive **Streamlit web app**

---

## 🗂️ Project Structure

```
Mental_Health_Social_Media/
│
├── data/
│   ├── raw/                        # Original datasets
│   ├── cleaned/                    # Cleaned & merged CSVs
│   └── database/mental_health.db   # SQLite database
│
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_engineering.ipynb
│   └── 04_model_training.ipynb
│
├── models/
│   ├── best_model.pkl              # Logistic Regression (LR)
│   └── scaler.pkl
│
├── outputs/plots/                  # Saved EDA charts
│
├── app/
│   └── streamlit_app.py            # Main Streamlit app
│
├── requirements.txt
└── README.md
```

---

## 📂 Datasets Used

| Dataset | Source | Records | Key Features |
|---|---|---|---|
| Social Media Impact on Life | Kaggle | ~1700 | Platform, usage hours, academic impact, mental health score |
| Teen Mental Health Dataset | Kaggle | ~1200 | Stress, anxiety, addiction level, depression label |
| **Merged Dataset** | Combined | ~1231 | All features + engineered risk score & addiction index |

---

## 🔬 ML Pipeline

```
Raw Data → Cleaning → EDA → Feature Engineering → Merged Dataset
                                                        ↓
                                           Train/Test Split (80/20)
                                                        ↓
                                    Logistic Regression | Random Forest
                                                        ↓
                                         Best Model: Logistic Regression
                                         Accuracy: 96.7% | Recall: 100%
```

### Why Logistic Regression over Random Forest?
Random Forest hit 100% accuracy — a red flag for **overfitting** on a small, imbalanced dataset (8 positive cases vs 239 negative).  
LR with `class_weight='balanced'` gave honest, generalizable results. ✅

---

## ⚙️ Feature Engineering

| Feature | Formula |
|---|---|
| `risk_score` | `stress×0.3 + anxiety×0.3 + addiction×0.2 + usage×0.1 + (10−sleep)×0.1` |
| `addiction_index` | `usage×0.5 + screen_time×0.3 + addiction×0.2` |
| `poor_sleep` | `1 if sleep < 6 hrs else 0` |
| `high_usage` | `1 if daily hours > 5 else 0` |

---

## 📈 Key Findings

- 📱 Depressed users spend **~2 hrs more/day** on social media
- 😴 Depressed users sleep **4.76 hrs** vs **6.49 hrs** for healthy users
- 😓 High stress + high anxiety = strongest predictors of depression
- 🔁 Social media addiction and poor sleep form a **self-reinforcing cycle**

---

## 🖥️ App Pages

| Page | Description |
|---|---|
| 🏠 Home | Project overview + portfolio link |
| 🤖 Prediction | Enter 5 habits → get risk level + suggestions |
| 📈 Insights | KPIs, dataset tables, scatter plot, key findings |
| 💬 Chat | Nova AI chatbot for mental wellness conversations |

---

## 🚀 Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/kanhasujit/Social-Media-Mental-Health-Analyzer.git
cd mental-health-analyzer

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the notebooks in order (01 → 04)

# 4. Launch the app
cd app
streamlit run streamlit_app.py
```

---

## 📦 Requirements

```
pandas
numpy
scikit-learn
matplotlib
seaborn
plotly
streamlit
sqlalchemy
jupyter
```

---

## 💡 What Makes This Unique (2026)

- ✅ **End-to-end pipeline** — raw data → cleaned → EDA → ML → SQL → deployed app
- ✅ **Integrated AI chatbot** (Nova) for real conversations about mental wellness
- ✅ **Engineered features** that go beyond raw columns (risk score, addiction index)
- ✅ **Honest ML** — chose accuracy over overfitting, documented the why
- ✅ **Real-world impact** — not just a model, but a tool people can actually use

---

## 👨‍💻 Built By

**Sujit Kumar Behera** — Data Scientist & AI Engineer

🌐 [Portfolio / Connect with me](https://sujit-port-folio.netlify.app/)

---

<div align="center">
<i>Built with 🧠 and a lot of curiosity about what scrolling does to us.</i>
</div>