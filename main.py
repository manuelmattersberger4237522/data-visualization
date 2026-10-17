import matplotlib.pyplot as plt
import pandas as pd


def get_transformed_dataset():    
    return None

def create_visualizations(dataset):
    fig = plt.figure()

    ax1 = fig.add_subplot(131, frameon=False)

    plt.show()

def main():
    dataset = get_transformed_dataset()
    create_visualizations(dataset)


if __name__ == "__main__":
    main()