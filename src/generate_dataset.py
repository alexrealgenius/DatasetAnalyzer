import pandas as pd
import numpy as np


def generate_dataset():

    number_of_customers = 1000

    age = np.random.randint(18, 70, number_of_customers)

    monthly_spending = np.round(
        np.random.uniform(30, 200, number_of_customers),
        2
    )

    months_as_customer = np.random.randint(
        1, 73, number_of_customers
    )

    support_tickets = np.random.randint(
        0, 10, number_of_customers
    )

    used_mobile_app = np.random.randint(
        0, 2, number_of_customers
    )

    # Create a probability of churning.
    # More support tickets increases churn probability.
    # Not using the mobile app increases churn probability.
    churn_score = (
        support_tickets * 0.08
        + (1 - used_mobile_app) * 0.20
        - months_as_customer * 0.003
    )

    churn_probability = np.clip(
        0.15 + churn_score,
        0.05,
        0.90
    )

    churned = np.random.binomial(
        1,
        churn_probability
    )

    data = pd.DataFrame({
        "age": age,
        "monthly_spending": monthly_spending,
        "months_as_customer": months_as_customer,
        "support_tickets": support_tickets,
        "used_mobile_app": used_mobile_app,
        "churned": churned
    })

    data.to_csv("data/dataset.csv", index=False)



if __name__ == "__main__":
    generate_dataset()