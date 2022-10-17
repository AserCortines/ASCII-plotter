"""
Functions to plot canvas in stdOut
"""
from numpy.typing import NDArray


def print_chart(canvas: NDArray) -> None:
    """
    Prints a multidimensional NDArray to the standard output
    :param canvas: 2D character array containing each ASCII character
    :return:
    """

    for row in canvas:
        print("".join(row))
    pass


if __name__ == "__main__":

    import numpy as np

    can = np.array([["+", "-", "-", "-", "+"],
                    ["|", " ", " ", " ", "|"],
                    ["|", " ", " ", " ", "|"],
                    ["+", "-", "-", "-", "+"]])

    print_chart(can)
