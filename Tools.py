from Graph import GridWithWeights


# utility functions for dealing with square grids
def from_id_width(id, *, width):
    return id % width, id // width


def draw_tile(graph, id, style, width):
    r = "."
    if 'number' in style and id in style['number']:
        r = "%d" % style['number'][id]
    if 'point_to' in style and style['point_to'].get(id, None) is not None:
        (x1, y1) = id
        (x2, y2) = style['point_to'][id]
        if x2 == x1 + 1:
            r = "\u2192"
        if x2 == x1 - 1:
            r = "\u2190"
        if y2 == y1 + 1:
            r = "\u2193"
        if y2 == y1 - 1:
            r = "\u2191"
    if 'start' in style and id == style['start']:
        r = "A"
    if 'goal' in style and id == style['goal']:
        r = "Z"
    if 'path' in style and id in style['path']:
        r = "@"
    if id in graph.walls:
        r = "#" * width
    return r


def draw_grid(graph, width=2, **style):
    for y in range(graph.height):
        for x in range(graph.width):
            print("%%-%ds" % width % draw_tile(graph, (x, y), style, width), end="")
        print()


# data from main article
DIAGRAM1_WALLS = [from_id_width(id, width=14) for id in
                  [14, 15, 16, 17, 28, 29, 30, 31, 42, 43, 44, 45, 70, 71, 72, 73, 84, 85, 86, 87, 98, 99, 100, 101,
                   126, 127, 128, 129, 140, 141, 142, 143, 154, 155, 156, 157, 182, 183, 184, 185, 196, 197, 198, 199,
                   210, 211, 212, 213, 238, 239, 240, 241, 252, 253, 254, 255, 266, 267, 268, 269, 294, 295, 296, 297,
                   308, 309, 310, 311, 322, 323, 324, 325, 350, 351, 352, 353, 364, 365, 366, 367, 378, 379, 380, 381,

                   19, 20, 21, 22, 33, 34, 35, 36, 47, 48, 49, 50, 75, 76, 77, 78, 89, 90, 91, 92, 103, 104, 105, 106,
                   131, 132, 133, 134, 145, 146, 147, 148, 159, 160, 161, 162, 187, 188, 189, 190, 201, 202, 203, 204,
                   215, 216, 217, 218, 243, 244, 245, 246, 257, 258, 259, 260, 271, 272, 273, 274, 299, 300, 301, 302,
                   313, 314, 315, 316, 327, 328, 329, 330, 355, 356, 357, 358, 369, 370, 371, 372, 383, 384, 385, 386,

                   24, 25, 26, 27, 38, 39, 40, 41, 52, 53, 54, 55, 80, 81, 82, 83, 94, 95, 96, 97, 108, 109, 110, 111,
                   136, 137, 138, 139, 150, 151, 152, 153, 164, 165, 166, 167, 192, 193, 194, 195, 206, 207, 208, 209,
                   220, 221, 222, 223, 248, 249, 250, 251, 262, 263, 264, 265, 276, 277, 278, 279, 304, 305, 306, 307,
                   318, 319, 320, 321, 332, 333, 334, 335, 360, 361, 362, 363, 374, 375, 376, 377, 388, 389, 390, 391]]

diagram4 = GridWithWeights(10, 10)
diagram4.walls = [(1, 7), (1, 8), (2, 7), (2, 8), (3, 7), (3, 8)]
diagram4.weights = {loc: 5 for loc in [(3, 4), (3, 5), (4, 1), (4, 2),
                                       (4, 3), (4, 4), (4, 5), (4, 6),
                                       (4, 7), (4, 8), (5, 1), (5, 2),
                                       (5, 3), (5, 4), (5, 5), (5, 6),
                                       (5, 7), (5, 8), (6, 2), (6, 3),
                                       (6, 4), (6, 5), (6, 6), (6, 7),
                                       (7, 3), (7, 4), (7, 5)]}
