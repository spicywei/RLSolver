# comparison methods for maxcut: random walk, greedy, epsilon greedy, simulated annealing
import copy
import time
import networkx as nx
import numpy as np
from typing import List, Union
import random
from utils import read_txt_as_networkx_graph
from utils import obj_maxcut
from utils import write_result
from utils import plot_fig


def random_walk(init_solution: Union[List[int], np.array], num_steps: int, graph: nx.Graph) -> (int, Union[List[int], np.array], List[int]):
    print('random_walk')
    start_time = time.time()
    curr_solution = copy.deepcopy(init_solution)
    init_score = obj_maxcut(init_solution, graph)
    num_nodes = len(curr_solution)
    scores = []
    for i in range(num_steps):
        # select a node randomly
        node = random.randint(0, num_nodes - 1)
        curr_solution[node] = (curr_solution[node] + 1) % 2
        # calc the obj
        score = obj_maxcut(curr_solution, graph)
        scores.append(score)
    print("score, init_score of random_walk", score, init_score)
    print("scores: ", scores)
    print("solution: ", curr_solution)
    running_duration = time.time() - start_time
    print('running_duration: ', running_duration)
    return score, curr_solution, scores


if __name__ == '__main__':
    # read data
    # graph1 = read_as_networkx_graph('data/gset_14.txt')
    graph = read_txt_as_networkx_graph('data/syn/syn_50_176.txt')

    # run alg
    # init_solution = [1, 0, 1, 0, 1]
    init_solution = list(np.random.randint(0, 2, graph.number_of_nodes()))
    rw_score, rw_solution, rw_scores = random_walk(init_solution=init_solution, num_steps=1000, graph=graph)

    # write result
    write_result(rw_solution)
    obj = obj_maxcut(rw_solution, graph)
    print('obj: ', obj)
    alg_name = 'RW'

    # plot fig
    plot_fig(rw_scores, alg_name)


