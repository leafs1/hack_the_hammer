from Algorithms import *
from Graph import *
from Tools import *


def draw_square_grid_example():
    g = SquareGrid(14, 29)
    g.walls = DIAGRAM1_WALLS  # long list, [(21, 0), (21, 2), ...]
    draw_grid(g)

def breadth_first_search_simple_graph_test():
    graph = SimpleGraph()
    graph.edges = {
        'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'B': ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'C': ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']}

    breadth_first_search(graph, 'C')


def breadth_first_search_simple_graph_example():
    graph = SimpleGraph()
    graph.edges = {
        'A': ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'B': ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'C': ['A', 'B', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'D': ['A', 'B', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'],
        'E': ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    }
    breadth_first_search(graph, 'A')


def breadth_first_search_square_grid_example():
    g = SquareGrid(30, 15)
    g.walls = DIAGRAM1_WALLS
    parents = breadth_first_search(g, (8, 7), (17, 2))
    draw_grid(g, width=2, point_to=parents, start=(8, 7), goal=(17, 2))


def dijkstra_search_example():
    came_from, cost_so_far = dijkstra_search(diagram4, (1, 4), (7, 8))
    draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
    print()
    draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))
    print()
    draw_grid(diagram4, width=3, path=reconstruct_path(came_from, start=(1, 4), goal=(7, 8)))


def a_star_search_example():
    came_from, cost_so_far = a_star_search(diagram4, (1, 4), (7, 8))
    draw_grid(diagram4, width=3, point_to=came_from, start=(1, 4), goal=(7, 8))
    print()
    draw_grid(diagram4, width=3, number=cost_so_far, start=(1, 4), goal=(7, 8))


if __name__ == '__main__':
    draw_square_grid_example()
    #breadth_first_search_simple_graph_test()
#    breadth_first_search_simple_graph_example()
#    breadth_first_search_square_grid_example()
    #print('Dijkstra')
    #dijkstra_search_example()
    #print('A Star')
    #a_star_search_example()
