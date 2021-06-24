from abc import ABC
import abc

class Display(ABC):
    
    @abc.abstractmethod    
    def getColumns(self) -> int:
        pass

    @abc.abstractmethod
    def getRows(self) -> int:
        pass
    @abc.abstractmethod
    def getRowText(self, i : int, j : int) -> str:
        pass

    def show(self) -> None:
        for i in range(self.getRows()):
            for j in range(self.getColumns()):
                print(self.getRowText(i, j), end="")
            print()

class GridDisplay(Display):
    
    def __init__(self, grid):
        self.grid : list[int][list[int]] = grid

    def getRows(self):
        return len(self.grid)

    def getColumns(self):
        return len(self.grid[0])
    # @abc.abstractmethod
    # def getEnbeded(self) -> str:
    #     pass

    def getRowText(self, i : int, j :int ) -> str:
        return str(self.grid[i][j])

    # def getRowText(self, i: int) -> str:
    #     if (i%2 == 0):
    #         return self.getEnbeded(self)
        
    #     if (i%2 !=0):
    #         return self.getRowText()