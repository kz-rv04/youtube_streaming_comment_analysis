from matplotlib import pyplot as plt

def plot_timeseries(x, y, xlabel='time(sec)', ylabel='freq'):
    fig, ax = plt.subplots(figsize=(16,10), dpi=60)
    ax.plot(freq.index, freq.values)
    ax.set_xlabel(xlabel, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=24)
    ax.tick_params(labelsize=20)
    plt.show()
    
def bar_timeseries(x, y, label=[], width=1, xlabel='time(sec)', ylabel='freq'):
    fig, ax = plt.subplots(figsize=(16,10), dpi=60)
    if label:
        ax.bar(x, y, width=width, color=label)
    else:
        ax.bar(x, y, width=width)
    ax.set_xlabel(xlabel, fontsize=24)
    ax.set_ylabel(ylabel, fontsize=24)
    ax.tick_params(labelsize=20)
    plt.show()