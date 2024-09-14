# plot_utils.py

def apply_plot_settings(ax, x_label, y_label, plot_title, legend_title):
    ax.set_xlabel(x_label, fontsize=16, labelpad=15)
    ax.set_ylabel(y_label, fontsize=16, labelpad=15)
    ax.set_title(plot_title, fontsize=18, pad=20)
    handles, labels = ax.get_legend_handles_labels()
    by_label = dict(zip(labels, handles))
    ax.legend(by_label.values(), by_label.keys(), title=legend_title)
