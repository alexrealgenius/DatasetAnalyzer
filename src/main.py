from data_loader import load_data

def main():
    data = load_data("data/dataset.csv")

    print(data)

if __name__ == "__main__":
    main()