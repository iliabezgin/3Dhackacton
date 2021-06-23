from main_model import *
from dynamics import *

import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd
import pymc3 as pm


def generate_heatmap(data, labels_dict, file_title, plot_title):
    """
    method to generate heatmap with name file title of the given data
    """
    ax = sn.heatmap(data,
                    linewidths=0.3,
                    )
    figure = ax.get_figure()

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
        ax.set_ylabel(labels_dict["y"])
    if plot_title:
        ax.set_title(plot_title)

    figure.savefig(file_title + ".png")


def generate_history_plot(data, labels_dict, file_title, plot_title):
    ax = sns.histplot(data)

    if labels_dict:
        ax.set_xlabel(labels_dict["x"])
    if plot_title:
        ax.set_title(plot_title)

    plt.legend()
    plt.savefig(file_title + "png")


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


def simulation_energy_over_time(E, T_ns, T_ns_threshold):
    """
    method to create function of energy as a function of time
    """
    no_start = (T_ns > T_ns_threshold)
    # (x, y, labels_dict, file_title, plot_title)
    generate_2D_plot(T_ns[no_start], E[no_start],
                     {'x': r'time [$ns$]',
                      'y': r'E [$kcal/mol/A^2$]'},
                     "energy_graph",
                     "Energy(time) graph")


def end_to_end_distances_over_time(E, T_ns, T_ns_threshold):
    """
    method to create plot of distances of end to end as
    a function of time
    """
    no_start = (T_ns > T_ns_threshold)
    # (x, y, labels_dict, file_title, plot_title)
    generate_2D_plot(T_ns[no_start], E[no_start],
                     {'x': r'time [$ns$]',
                      'y': r'end-to-end distance [$A$]'},
                     "distances_graph",
                     "end to end Distances(time) graph")


def distribution_of_energy_over_time(E, T_ns, T_ns_threshold):
    """
    method to create plot of distribution of energy over time
    """
    no_start = (T_ns > T_ns_threshold)
    generate_history_plot(E[no_start],
                          {"x": r'energy [$kcal^{-1}mol^{-1}A^2$]'},
                          "dist_of_E",
                          "distribution of Energy history plot")


def distribution_of_dist_over_time(D):
    D_concat = np.concatenate(D[0:])
    generate_history_plot(D_concat,
                          {"x": r'N''-C'' distance [A]'},
                          "dist_of_D",
                          "distribution of Distances history plot")
