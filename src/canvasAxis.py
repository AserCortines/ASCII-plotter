"""
Functions to create axis in canvas:
 - add_axis
 - add_title
"""

import numpy as np
from numpy.typing import NDArray
from typing import Optional, List
from src.stOutPlotter import print_chart
from src.stOutCanvas import make_canvas, draw_in_canvas
from src.utils import scale_points


def add_axis(canvas: NDArray, x: List[float], y: List[float], legend: Optional[str] = None) -> NDArray:
    """
    Add x and y axes to canvas.
    :param canvas:
    :param x:
    :param y:
    :param legend:
    :return: canvas with axis
    """

    height, width = canvas.shape

    x_axis = _make_x_axis(x_values=x, width=width, legend=legend)
    canvas = np.vstack((canvas, x_axis))
    # Must add one to take into account the x-axis
    y_axis = _make_y_axis(y_values=y, height=height+1)
    canvas = np.hstack((y_axis, canvas))

    return canvas


def add_title(canvas: NDArray, title: str) -> NDArray:
    """
    Add title to canvas
    :param canvas:
    :param title:
    :return:
    """

    _, width = canvas.shape
    title = f"{title[:width]:^{width}}"

    title_axis = np.array(list(title))
    return np.vstack((title_axis, canvas))


def _make_x_axis(x_values: List[float], width: int, legend: Optional[str] = None) -> NDArray:
    """
    Make x-axis and adds legend (Optional)
    :param x_values:
    :param width:
    :param legend:
    :return:
    """

    # Taking minimum and maximum value of x (as integer) and transforming it into str
    x_min, x_max = str(np.floor(min(x_values)).astype(int)), str(np.ceil(max(x_values)).astype(int))

    if legend:
        # centering legend
        legend = f"{legend[:width]: ^{width}}"
        x_axis = np.array(list(legend))
    else:
        x_axis = np.full(width, fill_value=" ", dtype="<U30")

    x_axis[:len(x_min)] = list(x_min)
    x_axis[-len(x_max):] = list(x_max)
    return x_axis


def _make_y_axis(y_values: List[float], height: int) -> NDArray:
    """
    make y-axis. The width of y-axis is set to 4
    :param y_values:
    :param height:
    :return:
    """

    # Taking minimum and maximum value of y (as integer) and transforming it into str
    y_min, y_max = str(np.floor(min(y_values)).astype(int)), str(np.ceil(max(y_values)).astype(int))

    y_min = f"{y_min:^4}"
    y_max = f"{y_max:^4}"

    # The width of y-axis is set to 4
    y_axis = np.full((height, 4), fill_value=" ", dtype="<U30")

    y_axis[0, :] = np.array(list(y_max))
    # The height must take into account the x-axis
    y_axis[height - 2, :] = np.array(list(y_min))

    return y_axis


if __name__ == "__main__":

    # Canvas Width and Height
    w, h = 100, 30

    # Values
    scale, n = 0.1, 100
    x_vals = [scale * i for i in range(n)]
    y_vals = [np.sin(scale * i) for i in range(n)]

    # Creating Canvas
    test_canvas = make_canvas(width=w, height=h)

    # Scaling Values to canvas
    x_scaled, y_scaled = scale_points(x_vals, y_vals, width=w, height=h)

    # Drawing points in canvas

    test_canvas = draw_in_canvas(test_canvas, *zip(x_scaled, y_scaled), display_grid=False)

    # Adding title and axis

    test_canvas = add_axis(canvas=test_canvas, x=x_vals, y=y_vals, legend="test legend")
    test_canvas = add_title(test_canvas, title="test title")
    print_chart(test_canvas)
