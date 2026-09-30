import matplotlib.pyplot as plt

def create_visualizations(data):
    # Churn count
    data["churned"].value_counts().plot(kind="bar")

    plt.title("Customer Churn")
    plt.xlabel("Churned (0 = Stayed, 1 = Left)")
    plt.ylabel("Number of Customers")

    plt.tight_layout()
    plt.show()