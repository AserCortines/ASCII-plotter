
import numpy as np
from typing import List, Tuple


def scale_points(x: List[float], y: List[float], width: int, height: int) -> Tuple[int]:
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
    scale = .1
    x = [scale * i for i in range(10)]
    y = [np.sin(scale * i) for i in range(10)]

    print(scale_points(x, y, 100, 50))