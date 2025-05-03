
# 🧪 Student Exam Pass Prediction Using Logistic Regression

## 🎯 Objective
The objective of this project is to build a machine learning model that predicts whether a student will pass or fail an exam based on the number of hours they studied. This is a binary classification problem, and we use **Logistic Regression** to solve it.

## 🧠 Why Logistic Regression?
Logistic Regression is suitable for binary classification problems where the output is categorical (e.g., pass or fail). It models the probability that a given input belongs to a particular category.

## 🧾 Dataset Description
We use a **synthetic dataset** for simplicity. It contains two columns:
- **Hours_Studied** (Independent variable): The number of hours a student studied.
- **Passed** (Dependent variable): The target class — `1` if the student passed the exam, `0` otherwise.

### Sample Data
```
Hours_Studied | Passed
--------------|--------
1             | 0
5             | 1
10            | 1
```

## 🔧 Project Steps

### 1️⃣ Import Libraries
We use the following Python libraries:
- `pandas` for data handling
- `scikit-learn` for modeling
- `matplotlib` and `seaborn` for visualization

### 2️⃣ Create the Dataset
We define a simple DataFrame with sample data representing hours studied and the corresponding pass/fail result.

### 3️⃣ Prepare Features and Labels
We separate the dataset into:
- `X`: the input features (Hours_Studied)
- `y`: the output label (Passed)

### 4️⃣ Split the Data
We split the dataset into training and testing sets using `train_test_split` to evaluate our model properly.

### 5️⃣ Train the Model
We train a `LogisticRegression` model on the training data.

### 6️⃣ Make Predictions
We use the trained model to make predictions on the test set.

### 7️⃣ Evaluate the Model
We evaluate the performance using:
- **Accuracy Score**: Measures the proportion of correct predictions.
- **Confusion Matrix**: Shows the counts of true positives, true negatives, false positives, and false negatives.

### 8️⃣ Visualize the Results
We plot:
- The original data points (hours studied vs. pass/fail)
- The logistic regression curve showing the probability of passing as hours studied increases

## 📈 Output Example

- **Accuracy**: `1.0` (or 100%) — because the synthetic data is very simple
- **Confusion Matrix**:
  ```
  [[1 0]
   [0 2]]
  ```

- **Plot**: A sigmoid curve representing the probability of passing vs. hours studied

## 💡 What You Learn
- How to build a classification model using logistic regression
- How to evaluate classification results using accuracy and confusion matrix
- How to visualize a logistic curve in 2D space
- Understanding the probability output of a classifier

## 🚀 Possible Improvements
- Add more features (e.g., attendance, sleep hours)
- Use a larger real-world dataset from Kaggle or UCI
- Try other classifiers like SVM or Decision Trees for comparison
