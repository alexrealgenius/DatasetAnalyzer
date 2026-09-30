import joblib

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score


def train_models(data):
    X = data[
        [
            "age",
            "monthly_spending",
            "months_as_customer",
            "support_tickets",
            "used_mobile_app",
        ]
    ]

    Y = data["churned"]

    # Keep the test data completely separate
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    models = {
        "Decision Tree": DecisionTreeClassifier(random_state=42),

        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000))
        ]),

        "K-Nearest Neighbors": Pipeline([
            ("scaler", StandardScaler()),
            ("model", KNeighborsClassifier())
        ])
    }

    print("\n===== MODEL COMPARISON =====")

    best_model = None
    best_model_name = None
    best_cv_score = 0

    for name, model in models.items():

        # Cross-validation only on training data
        cv_scores = cross_val_score(
            model,
            X_train,
            Y_train,
            cv=5,
            scoring="accuracy"
        )

        cv_mean = cv_scores.mean()

        print(f"\n{name}")
        print(f"CV Accuracy: {cv_mean:.3f}")
        print(f"CV Std: {cv_scores.std():.3f}")

        # Keep track of the highest CV score
        if cv_mean > best_cv_score:
            best_cv_score = cv_mean
            best_model = model
            best_model_name = name

    print("\n===== SELECTED MODEL =====")
    print("Model:", best_model_name)
    print(f"CV Accuracy: {best_cv_score:.3f}")

    # Train selected model
    best_model.fit(X_train, Y_train)

    # Final evaluation on untouched test data
    predictions = best_model.predict(X_test)

    test_accuracy = accuracy_score(Y_test, predictions)

    print(f"Test Accuracy: {test_accuracy:.3f}")

    # Save the trained model
    joblib.dump(best_model, "models/churn_model.joblib")

    print("Model saved to models/churn_model.joblib")