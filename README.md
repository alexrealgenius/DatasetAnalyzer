# AI Dataset Analyzer

A Python-based machine learning project that analyzes customer data, compares classification models, and predicts customer churn from new customer information.

## Overview

The AI Dataset Analyzer is an end-to-end machine learning project built with Python.

The project currently:

* Loads customer data from a CSV file
* Analyzes dataset structure and statistics
* Checks for missing values
* Creates data visualizations
* Splits data into training and testing sets
* Trains multiple machine learning models
* Uses 5-fold cross-validation to compare models
* Selects a model based on cross-validation accuracy
* Saves the trained model using Joblib
* Uses the saved model to make predictions on new customers
* Provides a churn probability for predictions

## Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* scikit-learn
* Joblib
* Git / GitHub

## Project Structure

```text
DatasetAnalyzer/
│
├── data/
│   └── dataset.csv
│
├── models/
│   └── churn_model.joblib
│
├── src/
│   ├── main.py
│   ├── data_loader.py
│   ├── analyzer.py
│   ├── visualizer.py
│   ├── trainer.py
│   ├── predict.py
│   └── generate_dataset.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset

The current dataset contains 1,000 synthetically generated customer records.

Each customer contains:

| Feature              | Description                                            |
| -------------------- | ------------------------------------------------------ |
| `age`                | Customer age                                           |
| `monthly_spending`   | Customer's monthly spending                            |
| `months_as_customer` | Number of months the customer has used the service     |
| `support_tickets`    | Number of support tickets submitted                    |
| `used_mobile_app`    | `1` if the customer uses the mobile app, otherwise `0` |
| `churned`            | `1` if the customer churned, otherwise `0`             |

The dataset is generated locally with `generate_dataset.py` for development and experimentation.

Because the dataset is synthetic, model performance should not be interpreted as real-world customer churn performance.

## Machine Learning Models

The project currently compares three classification models:

### Decision Tree

A tree-based model that learns decision rules from the training data.

### Logistic Regression

A classification model that estimates the relationship between the input features and the probability of the two possible outcomes.

### K-Nearest Neighbors

A model that predicts a customer based on similar examples in the training data.

## Model Evaluation

The models are evaluated using:

* 80/20 train-test split
* 5-fold cross-validation
* Accuracy
* Cross-validation standard deviation

The test dataset is kept separate from the cross-validation training process so that it can be used for a final evaluation.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd DatasetAnalyzer
```

### 2. Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn joblib
```

### 3. Generate the dataset

```bash
python src/generate_dataset.py
```

This creates:

```text
data/dataset.csv
```

### 4. Run the analyzer

```bash
python src/main.py
```

This will:

1. Load the dataset
2. Display dataset statistics
3. Check for missing values
4. Generate a visualization
5. Train and compare machine learning models
6. Select a model
7. Save the trained model

The trained model is saved to:

```text
models/churn_model.joblib
```

### 5. Make a prediction

After the model has been trained, run:

```bash
python src/predict.py
```

The program will ask for information about a customer, such as:

```text
Age: 25
Monthly spending: 50
Months as customer: 6
Support tickets: 5
Uses mobile app? (1 = yes, 0 = no): 0
```

The saved model will then produce a churn prediction and estimated churn probability.

## Example Workflow

```text
Generate Dataset
       ↓
Load CSV
       ↓
Analyze Dataset
       ↓
Visualize Data
       ↓
Split Training/Test Data
       ↓
Train Multiple Models
       ↓
5-Fold Cross-Validation
       ↓
Compare Models
       ↓
Select Model
       ↓
Save Model
       ↓
Predict New Customer
```


## Purpose

This project was created as a personal project to develop practical skills in:

* Python programming
* Data analysis
* Machine learning
* Model evaluation
* Software engineering
* Git and GitHub workflows

<br>
<h1><b>Author</b></h1>

[Alexander Troshin](https://github.com/alexrealgenius)

[![GitHub](https://img.shields.io/badge/GitHub-alexrealgenius-181717?style=for-the-badge&logo=github)](https://github.com/alexrealgenius)
