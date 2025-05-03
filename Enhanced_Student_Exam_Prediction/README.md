
# 🎓 Student Exam Pass Prediction using Logistic Regression

This machine learning project predicts whether a student will pass an exam based on key factors such as hours studied, sleep hours, and class attendance percentage.

## 🧠 Overview

We use **Logistic Regression** to build a classification model that predicts binary outcomes: **pass (1)** or **fail (0)**.

---

## 📁 Project Structure

```
.
├── Enhanced_Student_Exam_Prediction.ipynb
├── Enhanced_Student_Exam_Prediction_Documentation.md
└── README.md
```

---

## 📊 Features Used

- `Hours_Studied`
- `Sleep_Hours`
- `Attendance_Percentage`

Target:
- `Passed` (1 = pass, 0 = fail)

---

## 🚀 How It Works

1. **Data Preparation** – Manually create a synthetic dataset.
2. **Feature Scaling** – Normalize features using `StandardScaler`.
3. **Model Training** – Fit logistic regression on the training set.
4. **Evaluation** – Accuracy, confusion matrix, classification report.
5. **ROC Curve** – Visualize true/false positive trade-off.
6. **Cross-validation** – Use 5-fold cross-validation to validate the model.

---

## 📈 Sample Output

- **Accuracy**: 1.0  
- **ROC AUC**: 1.0  
- **Cross-validation Scores**: `[1. 1. 1. 1. 1.]`

---

## 📦 Libraries Used

- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

---

## 📌 Future Improvements

- Replace synthetic data with real-world data from [Kaggle](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)
- Try advanced models like SVM, Decision Trees
- Build a simple [Streamlit](https://streamlit.io/) app for real-time prediction

---

## 👨‍💻 Author

Made by **[Your Name]**  
Feel free to fork, star, or contribute!

