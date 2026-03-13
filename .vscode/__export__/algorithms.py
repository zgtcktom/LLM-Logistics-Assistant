#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nbimport

import os, sys, time, json, re
from tqdm import tqdm

import numpy as np
import matplotlib.pyplot as plt

import pandas as pd


# In[2]:


def nearest_neighbor_vrp(distance_matrix, demands, vehicle_capacity, depot=0):
    distance_matrix = np.array(distance_matrix)
    demands = np.array(demands)

    n = len(distance_matrix)
    if len(demands) != n:
        raise ValueError("demands length must match number of nodes")

    unvisited = set(range(n))
    unvisited.remove(depot)  # depot is not a customer
    routes = []
    total_distance = 0.0

    while unvisited:
        # Start a new route from depot
        route = [depot]
        current_load = 0
        current_pos = depot
        route_distance = 0.0

        while True:
            # Find the closest feasible customer
            best_next = None
            best_dist = float("inf")

            for customer in unvisited:
                if demands[customer] + current_load > vehicle_capacity:
                    continue
                dist = distance_matrix[current_pos][customer]
                if dist < best_dist:
                    best_dist = dist
                    best_next = customer

            # No more customers can be added → close route
            if best_next is None:
                break

            # Add to route
            route.append(best_next)
            route_distance += best_dist
            current_load += demands[best_next]
            current_pos = best_next
            unvisited.remove(best_next)

        # Return to depot
        route.append(depot)
        route_distance += distance_matrix[current_pos][depot]
        total_distance += route_distance

        routes.append(route)

    return routes, total_distance


nearest_neighbor_vrp.__name__


# In[ ]:




