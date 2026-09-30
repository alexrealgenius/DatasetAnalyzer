def analyze_data(data):
    print("\n=====DATASET OVERVIEW=====")

    print("\nNumber of rows:", len(data))
    print("\nNumber of columns:", len(data.columns))

    print("\nColumns:")
    for column in data.columns:
        print("-", column)

    print("\nMissing values:")
    print(data.isnull().sum())

    print("\nBasic Statistics:")
    print(data.describe())

    print ("\nChurn distribution:")
    print(data["churned"].value_counts())