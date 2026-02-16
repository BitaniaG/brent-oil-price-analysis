import matplotlib.pyplot as plt

def plot_change_point(df, change_date):
    plt.figure(figsize=(12,6))
    plt.plot(df["Date"], df["Price"], label="Brent Price")
    plt.axvline(change_date, color="red", linestyle="--", label="Change Point")
    plt.legend()
    plt.title("Brent Oil Structural Break Detection")
    plt.tight_layout()
    plt.savefig("reports/change_point.png")
