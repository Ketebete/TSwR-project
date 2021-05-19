from machines_setup.master import *
from machines_setup.slave import *
import networkx as nx
import matplotlib.pyplot as plt


def draw_graph(current_master_state, current_slave_state, M_ok, S_ok):
    plt.ion()
    plt.figure('Tester', figsize=(12, 8))
    for node in a:
        if node == current_master_state and M_ok == 1:
            master_color.append('#adf7df')
        else:
            master_color.append('#C0C0C0')

    for node in b:
        if node == current_slave_state and S_ok == 1:
            slave_color.append('#adf7df')
        else:
            slave_color.append('#C0C0C0')

    nx.draw(b, **slave_settings)
    nx.draw(a, **master_settings)

    plt.show()
    master_color.clear()
    slave_color.clear()
    plt.pause(0.1)
    plt.clf()


b = nx.DiGraph()
a = nx.DiGraph()

a.add_edges_from(master_edges)
a.add_nodes_from(master_nodes)

b.add_edges_from(slave_edges)
b.add_nodes_from(slave_nodes)
