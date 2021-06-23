from main_model import *
from dynamics import *

import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd


def generate_heatmap(data, file_title):
    """
    method to generate heatmap with name file title of the given data
    """
    ax = sn.heatmap(data,
                    linewidths=0.3,
                    )
    figure = ax.get_figure()
    ax.legend()

    figure.savefig(file_title + ".png")


def generate_2D_scatter_plot(x, y, labels_dict, file_title, plot_title):
    """
    method to generate 2D scatter plot
    """
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.scatter(x, y)

    if labels_dict:
        plt.xlabel(labels_dict["x"])
        plt.ylabel(labels_dict["y"])
    if plot_title:
        plt.title(plot_title)

    plt.legend()

    plt.savefig(file_title + "png")


def generate_3D_scatter_plot(x, y, z, labels_dict, file_title, plot_title):
    """
    method to generate 3D scatter plot
    """
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.scatter(x, y, z,
               marker=".")

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
        ax.set_ylabel(labels_dict["y"])
        ax.set_zlabel(labels_dict["z"])
    if plot_title:
        ax.set_title(plot_title)

    plt.legend()
    plt.savefig(file_title + "png")


def generate_2D_plot(x, y, labels_dict, file_title, plot_title):
    """
    generate simple 2d plot
    """
    plt.plot(x, y)

    if labels_dict:
        plt.xlabel(labels_dict["x"])
        plt.ylabel(labels_dict["y"])
    if plot_title:
        plt.title(plot_title)

    plt.legend()
    plt.savefig(file_title + "png")


def e_n_d_as_function_of_time(E, D, T_ns, T_ns_threshold):
    """
    method to create function of energy and distances as a function of time
    """
    no_start = (T_ns > T_ns_threshold)
    # (x, y, labels_dict, file_title, plot_title)
    generate_2D_plot(T_ns[no_start], E[no_start],
                     {'x': r'time [$ns$]',
                      'y': r'E [$kcal/mol/A^2$]'},
                     "energy_graph",
                     "Energy(time) graph")
    generate_2D_plot(T_ns[no_start], D[no_start],
                     {'x': r'time [$ns$]',
                      'y': r'end-to-end distance [$A$]'},
                     "energy_graph",
                     "Energy(time) graph")
