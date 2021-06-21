from abc import ABC
import abc

class Display():
    
    @abc.abstractmethod    
    def getColumns() -> int:
        pass

    @abc.abstractmethod
    def getRows() -> int:
        pass

    

