
from abc import ABC, abstractmethod

class Fruit(ABC):
    @abstractmethod
    def tast(self):
       raise NotImplementedError