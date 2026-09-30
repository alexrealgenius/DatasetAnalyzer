import joblib
import pandas as pd


def predict_customer():
    # Load the trained model
    model = joblib.load("models/churn_model.joblib")

    print("\n===== CUSTOMER CHURN PREDICTION =====")

    age = int(input("Age: "))
    monthly_spending = float(input("Monthly spending: "))
    months_as_customer = int(input("Months as customer: "))
    support_tickets = int(input("Support tickets: "))
    used_mobile_app = int(input("Uses mobile app? (1 = yes, 0 = no): "))

    customer = pd.DataFrame([{
        "age": age,
        "monthly_spending": monthly_spending,
        "months_as_customer": months_as_customer,
        "support_tickets": support_tickets,
        "used_mobile_app": used_mobile_app
    }])

    # Make the prediction
    prediction = model.predict(customer)[0]

    # Get probability of each class
    probabilities = model.predict_proba(customer)[0]

    # Probability of churned = 1
    churn_probability = probabilities[1]

    print("\n===== PREDICTION =====")

    if prediction == 1:
        print("Predicted churn: YES")
    else:
        print("Predicted churn: NO")

    print(f"Churn probability: {churn_probability:.1%}")


if __name__ == "__main__":
    predict_customer()