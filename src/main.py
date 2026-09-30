from data_loader import load_data
from analyzer import analyze_data
from visualizer import create_visualizations

def main():
    data = load_data("data/dataset.csv")

    analyze_data(data)

    create_visualizations(data)

if __name__ == "__main__":
    main()