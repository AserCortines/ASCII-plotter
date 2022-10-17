
import numpy as np
from numpy.typing import NDArray
from typing import List, Tuple


def scale_points(x: List[float], y: List[float], width: int, height: int) -> Tuple[NDArray, NDArray]:
    """
    scale points coordinates to fit in StOut Canvas
    :param x:
    :param y:
    :param width: canvas width
    :param height: canvas height
    :return: scaled points
    """
    x, y = np.asarray(x), np.asarray(y)

    x_norm = (x - min(x)) / (max(x) - min(x))
    y_norm = (y - min(y)) / (max(y) - min(y))

    x_new = np.floor(x_norm * width).astype(int)
    y_new = np.floor(y_norm * height).astype(int)

    # Removing values may be equal to height or width
    # mask = (x_new != 0) & (x_new != w) & (y_new != 0) & (y_new != h)
    mask = (x_new != width) & (y_new != height)

    return x_new[mask], y_new[mask]


if __name__ == "__main__":
    scale, n = .1, 10
    x_vals = [scale * i for i in range(n)]
    y_vals = [np.sin(scale * i) for i in range(n)]

    print(scale_points(x_vals, y_vals, 100, 50))
