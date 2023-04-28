# This interpretation of Dijkstra's Algorithm is originally from: https://algodaily.com/lessons/an-illustrated-guide-to-dijkstras-algorithm/python 

# Source and destination to determine the route
source = "Whitewood Park"
destination = "Antelope Hills Elementary School"

def dijkstra():
  # Declaring variables and lists
  unvisited = graph
  shortest_distances = {}
  route = []
  path_nodes = {}

  # For loop to iterate through the unvisited nodes while searching for best path
  for nodes in unvisited:
      shortest_distances[nodes] = math.inf
  shortest_distances[source] = 0

  # While the node is unvisited, each should be checked and the node with the shortest distance should be chosen
  while unvisited:
      min_node = None
      for current_node in unvisited:
          if min_node is None:
              min_node = current_node
          elif shortest_distances[min_node] \
              > shortest_distances[current_node]:
              min_node = current_node
      for (node, value) in unvisited[min_node].items():
          if value + shortest_distances[min_node] \
              < shortest_distances[node]:
              shortest_distances[node] = value \
                  + shortest_distances[min_node]
              path_nodes[node] = min_node
      unvisited.pop(min_node)
  node = destination

  # Continue searching unless destination is reached or if the path is unreachable.
  while node != source:
      try:
          route.insert(0, node)
          node = path_nodes[node]
      except Exception:
          print('Path not reachable')
          break
  route.insert(0, source)

  # Display the path with the shortest distance calculation
  if shortest_distances[destination] != math.inf:
      print('The shortest distance is ' + str(shortest_distances[destination]) + ' miles.')
      print('The path is :' + str(route))

dijkstra()