"""
Functions to initialize and manipulate StOut canvas
"""

import numpy as np
from color import color
from stOutPlotter import print_chart


def make_canvas(width: int,
                height: int,
                display_grid: bool = False,
                secondary_color: tuple = (125, 125, 125)) -> np.typing.NDArray:
    """
    Create a function for initializing a 2D array based on given dimensions width and height.
    :param width:
    :param height:
    :param display_grid: (boolean)
    :param secondary_color: Grid color. Only applies if display grid is True
    :return: Canvas (NDArray)
    """
    canvas = np.empty((height, width), dtype="<U30")

    canvas[0][0] = canvas[0][-1] = canvas[-1][0] = canvas[-1][-1] = "+"
    canvas[0][1:-1] = canvas[-1][1:-1] = "-"
    canvas[1:-1, 0] = canvas[1:-1, -1] = "|"

    grid_points = color(".", rgb=secondary_color) if display_grid else " "

    canvas[1:-1, 1:-1] = grid_points

    return canvas


if __name__ == "__main__":

    print_chart(make_canvas(width=10, height=4))
    print()
    print_chart(make_canvas(10, 5, display_grid=True))

