from abc import ABC, abstractmethod
class Command(ABC):
    def execute(self):
        pass