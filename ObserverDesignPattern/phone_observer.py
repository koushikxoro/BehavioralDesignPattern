from observer import Observer
from subject import Subject
class PhoneObserver(Observer):
    def update(self, subject:Subject):
        print(f"Updating phone observer {subject.get_state()}")