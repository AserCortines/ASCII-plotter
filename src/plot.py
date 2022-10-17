"""
StOut plot function
"""

from typing import List, Optional, Tuple
from src.stOutPlotter import print_chart
from src.stOutCanvas import make_canvas, draw_in_canvas
from src.utils import scale_points
from src.canvasAxis import add_axis, add_title


def plot(x: List[float],
         y: List[float],
         height: int = 15,
         width: int = 100,
         display_grid: bool = False,
         title: Optional[str] = None,
         legend: Optional[str] = None,
         primary_color: Tuple[int, int, int] = (0, 0, 255),
         secondary_color: Tuple[int, int, int] = (125, 125, 125)) -> None:

    canvas = make_canvas(width, height, display_grid, secondary_color)

    x_scaled, y_scaled = scale_points(x, y, width, height)

    canvas = draw_in_canvas(canvas,
                            *zip(x_scaled, y_scaled),
                            primary_color=primary_color,
                            display_grid=display_grid)

    canvas = add_axis(canvas, x, y, legend=legend)
    canvas = add_title(canvas, title)

    print_chart(canvas)
    pass


if __name__ == "__main__":
    pass
