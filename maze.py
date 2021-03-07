# This file basically sends the solution to the animation that we will see
# on running our __main__.py file.

from configuration import return_path, offsets, move_possible # We import all necessary function definition from
                                                              # the configuration that we designed
from myQueue import Queue                                     # We will import our Queue class to be used for BFS

# Let us define the mechanism for breadth first search that will yield the return path
def bfs(maze, start, goal):
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}
    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return return_path(predecessors, start, goal)
        for direction in ["up", "right", "down", "left", "up-left", "up-right", "down-left", "down-right"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if move_possible(maze, neighbor) and neighbor not in predecessors:
                queue.enqueue(neighbor)
                predecessors[neighbor] = current_cell

# The above function was responsible for storing the return path when a solution was found.
# As demanded in our project description was that we need to show the exploration path.
# It is better to define a separate function which will be called only when such a requirement is asked.
# Why?
# It is always a good practice not to collect garbage collection as it gets cumbersome with time
# to handle memory if it is running on a smaller machine or a microcontroller board.

def explored_path(maze, start, goal):
    coordinates = list()
    queue = Queue()
    queue.enqueue(start)
    predecessors = {start: None}
    while not queue.is_empty():
        current_cell = queue.dequeue()
        if current_cell == goal:
            return coordinates
        for direction in ["up", "right", "down", "left", "up-left", "up-right", "down-left", "down-right"]:
            row_offset, col_offset = offsets[direction]
            neighbor = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if move_possible(maze, neighbor) and neighbor not in predecessors:
                queue.enqueue(neighbor)
                coordinates.append(neighbor)
                predecessors[neighbor] = current_cell

# If you run this file alone, you will get the list of coordinates that our player
# will follow when he starts at origin and intends to reach at (252, 299)
if __name__ == '__main__':
    maze = [['']*400]*300

    solution = bfs(maze, (0, 0), (252, 299))
    print(solution)
