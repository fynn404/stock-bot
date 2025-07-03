import matplotlib.pyplot as plt
from datetime import datetime
from fetch_data import get_fear_greed_data

def plot_fear_greed():
    data = get_fear_greed_data()
    historical = data["fear_and_greed_historical"]["data"]

    dates = [datetime.fromtimestamp(item["x"] / 1000) for item in historical]
    scores = [item["y"] for item in historical]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, scores, marker='o', linestyle='-')
    plt.title("Fear and Greed Index Over Time")
    plt.xlabel("Date")
    plt.ylabel("Score")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_fear_greed()
