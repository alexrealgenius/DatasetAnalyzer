import matplotlib.pyplot as plt


def create_visualizations(data):
    churn_counts = data["churned"].value_counts().sort_index()

    labels = ["Stayed", "Churned"]
    values = [
        churn_counts.get(0, 0),
        churn_counts.get(1, 0)
    ]

    total = sum(values)

    fig, ax = plt.subplots(figsize=(8, 5))

    bars = ax.bar(labels, values)

    ax.set_title("Customer Churn")
    ax.set_xlabel("Customer Status")
    ax.set_ylabel("Number of Customers")

    # Create labels for each bar
    bar_labels = [
        f"{value} ({value / total * 100:.1f}%)"
        for value in values
    ]

    ax.bar_label(bars, labels=bar_labels, padding=5)

    ax.set_ylim(0, max(values) * 1.15)

    plt.tight_layout()
    plt.show()