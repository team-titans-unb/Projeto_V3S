import matplotlib.pyplot as plt

def plot_data(x, y, title='Data Plot', xlabel='X-axis', ylabel='Y-axis'):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid()
    plt.show()

def save_plot(x, y, filename='plot.png'):
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o')
    plt.savefig(filename)
    plt.close()