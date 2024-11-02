from subject import Subject
from observer import Observer
class WeatherSubject(Subject):
    def __init__(self):
        self.state=None
        self.observers=[]
    def attach(self, observer:Observer):
        self.observers.append(observer)
    def detach(self, observer:Observer):
        self.observers.remove(observer)
    def notify(self):
        for observer in self.observers:
            observer.update(self)
    def get_state(self):
        return self.state
    def set_state(self, state):
        self.state=state
        self.notify()