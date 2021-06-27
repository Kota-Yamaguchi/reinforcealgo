
from Display import Display, GridDisplay
from Border import GridBorders, Border
import time
import os
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

    while(True):
        border.show()
        time.sleep(5)
        os.system("clear")
        time.sleep(1)

main()