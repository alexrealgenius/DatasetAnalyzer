from data_loader import load_data
from analyzer import analyze_data
from visualizer import create_visualizations
from trainer import train_models

def main():
    data = load_data("data/dataset.csv")
    analyze_data(data)

    create_visualizations(data)

    train_models(data)

if __name__ == "__main__":
    main()