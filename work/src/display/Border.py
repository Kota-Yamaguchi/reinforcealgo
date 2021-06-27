from display.Display import Display
from abc import ABC

class Border(Display):
    def __init__(self, display : Display):
        self.display = display
    


# 一番端以外は仕切りをたす
class GridBorders(Border):
    def __init__(self, deco_str : str, display : Display):
        super().__init__(display)
        self.deco_str = deco_str

    def getRows(self) -> int:
        return 1+self.display.getRows()+1

    def getColumns(self) -> int:
        return self.display.getColumns()


    def getRowText(self, i : int, j : int ) -> str: 
        
        if i==0 and j==0:
            return "+"+ self.makeLine("-", self.getColumns()*2-1)+"+"
        elif i==0 and j!=0:
            return ""
        elif self.getRows()-1 == i and j==0:
            return "+"+ self.makeLine("-", self.getColumns()*2-1)+"+" 
        elif self.getRows()-1 == i and j!=0:
            return ""
        elif self.getColumns()-1   == j:
            return self.deco_str + str(self.display.getRowText(i-1, j)) +self.deco_str
        else:
            return self.deco_str + str(self.display.getRowText(i-1, j))
        


    def makeLine(self, string : str, columnNum: int ) -> str:
        stringlist = []
        for i in range(columnNum):
            stringlist.append(string)
        text = "".join(stringlist)
        
        return text

class DirectionBorders(Border):
    def __init__(self, display : Display):
        super().__init__(display)

    def getRows(self) -> int:
        return self.display.getRows()

    def getColumns(self) -> int:
        return self.display.getColumns()


    def getRowText(self, i : int, j : int ) -> str: 
        
        if self.display.getRowText(i, j) == "0":
            return "↓"
        if self.display.getRowText(i, j) == "1":
            return "↑"
        if self.display.getRowText(i, j) == "2":
            return "→"
        if self.display.getRowText(i, j) == "3":
            return "←"
        