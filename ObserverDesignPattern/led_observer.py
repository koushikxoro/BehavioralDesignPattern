from observer import Observer
from subject import Subject
class LEDObserver(Observer):
    def update(self, subject:Subject):
        print(f"Updating led observer {subject.get_state()}")