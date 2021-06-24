
from Display import Display, GridDisplay
from Border import GridBorders, Border


def main():
    grid = [
        [0, 0, 0, 1, 0, 2, 3],
        [0, 9, 0, -1, 1, 1,1],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]
    display = GridDisplay(grid)

    border : Display = GridBorders("|", display)

    border.show()
main()