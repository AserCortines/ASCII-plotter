"""
Functions to initialize and manipulate StOut canvas
"""

import numpy as np
from numpy.typing import NDArray
from typing import Tuple
from color import color
from stOutPlotter import print_chart


def make_canvas(width: int,
                height: int,
                display_grid: bool = False,
                secondary_color: tuple = (125, 125, 125)) -> NDArray:
    """
    Creates a Canvas (2D array) based on given dimensions width and height.
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


def draw_in_canvas(canvas: NDArray,
                   *values: Tuple[int],
                   primary_color: Tuple[int] = (0, 0, 255),
                   display_grid: bool = False) -> NDArray:

    """
    Draw data in canvas
    :param canvas:
    :param values:
    :param primary_color:
    :param display_grid:
    :return: Canvas (NDArray) with plotted data
    """

    height, width = canvas.shape
    dot = color("*", primary_color) if display_grid else color(".", primary_color)

    for val in values:
        x, y = val
        canvas[height - y - 1, x] = dot

    return canvas


if __name__ == "__main__":

    print_chart(make_canvas(width=10, height=4))
    print()
    test_canvas = make_canvas(10, 5, display_grid=True)
    print_chart(test_canvas)

    print()
    print_chart(draw_in_canvas(test_canvas, (5, 2), (6, 3), display_grid=True))




