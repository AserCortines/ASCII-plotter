def color(text: str, rgb: tuple):
    """
    Returns a colored string using ANSI codes.
    Parameters
    ----------
    :param text: The text to color
    :param rgb: The RGB color components
    """
    r, g, b = rgb
    return f"\033[38;2;{r};{g};{b}m{text}\033[m"
