from abc import ABC, abstractmethod
class Subject(ABC):
    @abstractmethod
    def attach(self, observer):
        pass
    @abstractmethod
    def detach(self, observer):
        pass
    @abstractmethod
    def notify(self):
        pass
    @abstractmethod
    def get_state(self):
        pass
    @abstractmethod
    def set_state(self):
        pass
