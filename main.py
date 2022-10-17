
from src import plot
import math


def example1() -> None:

    scale = 0.1
    n = int(8 * math.pi / scale)
    x = [scale * i for i in range(n)]
    y = [math.sin(scale * i) for i in range(n)]

    plot(x,
         y,
         display_grid=True, height=15,
         title="The sine function",
         legend="f(x) = sin(x), where 0 <= x <= 8π",
         primary_color=(255, 0, 0),
         secondary_color=(200, 200, 200))


def example2() -> None:

    scale = 0.1
    n = int(2 * math.pi / scale)
    x = [scale * i for i in range(n)]
    y = [math.cos(scale * i) for i in range(n)]
    plot(x, y,
         width=50,
         title="The cosine function",
         legend="f(x) = cos(x), where 0 <= x <= 2π",
         primary_color=(0, 0, 255),
         secondary_color=(200, 200, 200))


def example3() -> None:

    y = [ord(c) for c in 'ASCII Plotter example']
    n = len(y)
    x = [i for i in range(n)]

    plot(x, y,
         title="Plotting Random Data",
         legend="f(x) = random data",
         primary_color=(0, 0, 255))


if __name__ == "__main__":

     # Example 1
     print("--- Example 1 --- \n")
     example1()

     # Example 2
     print("--- Example 2 --- \n")
     example2()

     # Example 3
     print("--- Example 3 --- \n")
     example3()
