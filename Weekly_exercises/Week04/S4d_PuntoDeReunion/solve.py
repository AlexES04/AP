import os
import sys

actual_dir = os.path.dirname(os.path.abspath(__file__))
week04_dir = os.path.dirname(actual_dir)
sys.path.append(week04_dir)

from utils.simple_queue import Queue


def solve_punto_reunion(graph, positions):
  filtered_positions = list(set(positions))

  max_distances = {}
  allowed_nodes = {}

  for node in graph.nodes():
     max_distances[node] = 0
     allowed_nodes[node] = 0

  for position in filtered_positions:
    distances_from_start = bfs(graph, position)

    for reached_node, distance in distances_from_start.items():
      allowed_nodes[reached_node] += 1
      max_distances[reached_node] = max(max_distances[reached_node], distance)

  best_node = -1
  min_max_distance = float('inf')

  for node in graph.nodes():
    if allowed_nodes[node] == len(filtered_positions):
      if max_distances[node] < min_max_distance:
        min_max_distance = max_distances[node]
        best_node = node

      elif max_distances[node] == min_max_distance:
        if node < best_node:
          best_node = node

  if best_node == -1:
    return (-1, -1)
  return (best_node, min_max_distance)


def bfs(graph, first_node):
    queue = Queue()
    distances = {}

    queue.enqueue(first_node)
    distances[first_node] = 0

    while not queue.isEmpty():
      current = queue.dequeue()
      for neighbour in graph.neighbors(current):
        if neighbour not in distances:
          queue.enqueue(neighbour)
          distances[neighbour] = distances[current] + 1
    return distances
